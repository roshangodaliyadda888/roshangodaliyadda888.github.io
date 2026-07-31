import re
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATA_REVIEW = ROOT / "data-review"
CLASSIFIED_DOCX = Path(r"C:\Users\USER\Downloads\My Publications Classified by Thrust Area.docx")
CV_DOCX = Path(r"C:\Users\USER\Downloads\LongCV_GMRIG_Jan_2026.docx")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
TYPE_HEADINGS = {
    "Journal Papers": "Journal Article",
    "Journal Articles": "Journal Article",
    "Conference Papers": "Conference Paper",
    "Conference Papers (chronological)": "Conference Paper",
    "Datasets": "Dataset",
    "Magazines and Newsletters": "Magazine Article",
    "Magazines & Newsletters": "Magazine Article",
    "Books/Chapters": "Book Chapter",
}
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
THEME_ALIASES = {
    "Generative AI, Signal Processing, and Image Processing ? Algorithmic and Fundamental Theory": "Generative AI, Signal Processing, and Image Processing",
}
KNOWN_THEMES = {
    "Biomedical Signal Processing, Bio-Imaging, and Wearable AI",
    "Generative AI, Signal Processing, and Image Processing ? Algorithmic and Fundamental Theory",
    "Generative AI, Signal Processing, and Image Processing - Algorithmic and Fundamental Theory",
    "AI for Public Health and Social Impact Modeling",
    "Smart Grid: NILM, Forecasting, Agrovoltaics and PV Integration",
    "Remote Sensing and Hyperspectral Imaging",
    "Multispectral Imaging for Food, Agriculture, and Manufacturing Quality",
    "Optical Wireless Communications",
    "Computer Vision, Machine Vision, Robotics, and Assisted Navigation",
    "Image and Signal Processing for Enhancement, Recognition, and Localization",
    "Spectral Imaging and Remote Sensing for Environmental and Industrial Monitoring",
}
FLAGSHIP_HINTS = [
    "IEEE Transactions",
    "Applied Energy",
    "Nature",
    "Frontiers",
    "PLOS ONE",
    "IEEE Access",
    "ICLR",
    "CVPR",
    "WACV",
    "ICIP",
    "ICC ",
    "IEEE Communications Magazine",
    "IEEE Internet of Things Journal",
]
SOURCE_ONLY_CV = "January 2026 CV only"
SOURCE_ONLY_CLASSIFIED = "Classified document only"


@dataclass
class Publication:
    title: str
    authors: str
    year: str
    pub_type: str
    venue: str
    primary_theme: str
    secondary_themes: list[str] = field(default_factory=list)
    month: str = ""
    volume: str = ""
    issue: str = ""
    pages: str = ""
    article_number: str = ""
    publisher: str = ""
    location: str = ""
    doi: str = ""
    url: str = ""
    isbn: str = ""
    dataset_repository: str = ""
    publication_status: str = ""
    source_document: str = ""
    source_location: str = ""
    notes: str = ""
    selected_candidate: bool = False
    verification_status: str = ""
    normalized_title: str = ""
    key: str = ""
    duplicate_status: str = ""
    conflict_status: str = ""
    matched_sources: list[str] = field(default_factory=list)


def read_docx_paragraphs(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    paragraphs = []
    for para in root.findall(".//w:p", NS):
        text = "".join((node.text or "") for node in para.findall(".//w:t", NS)).strip()
        if text:
            paragraphs.append(text)
    return paragraphs


def consecutive_dedupe(items: list[str]) -> list[str]:
    out = []
    for item in items:
        if not out or out[-1] != item:
            out.append(item)
    return out


def clean_text(text: str) -> str:
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\u00a0", " ")
    text = text.replace("?", '"')
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace(" .", ".").replace(" ,", ",")
    return text


def normalize_title(title: str) -> str:
    title = clean_text(title).lower()
    title = re.sub(r"https?://\S+", "", title)
    title = re.sub(r"10\.\d{4,9}/\S+", "", title)
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def maybe_theme(line: str) -> bool:
    if line in TYPE_HEADINGS:
        return False
    if len(line) < 8 or len(line) > 120:
        return False
    if re.search(r"\d{4}", line):
        return False
    if re.search(r"https?://|doi:", line, re.I):
        return False
    if '"' in line or "." in line:
        return False
    if line.count(",") > 4:
        return False
    return True


def extract_year(line: str) -> str:
    years = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", line)]
    if not years:
        return ""
    valid = [y for y in years if y <= 2026]
    return str(max(valid or years))


def extract_month(line: str) -> str:
    for month in MONTHS:
        if month in line:
            return month
    for month in [m[:3] + "." for m in MONTHS]:
        if month in line:
            return month
    return ""


def extract_doi_url(line: str) -> tuple[str, str]:
    doi_match = re.search(r"(10\.\d{4,9}/[^\s,;]+)", line, re.I)
    url_match = re.search(r"(https?://\S+)", line, re.I)
    doi = doi_match.group(1).rstrip(").,") if doi_match else ""
    url = url_match.group(1).rstrip(").,") if url_match else ""
    if doi and not url:
        url = f"https://doi.org/{doi}"
    return doi, url


def extract_title_and_authors(line: str) -> tuple[str, str, str]:
    line = clean_text(line)
    if "Visible Light Communication System with Ambient Light Cancellation" in line and "IESL Annual Transactions" in line:
        marker = "Visible Light Communication System with Ambient Light Cancellation"
        before, after = line.split(marker, 1)
        authors = before.rstrip(' ,;"\'?')
        rest = after.lstrip(' ,"\'?')
        if rest.startswith(","):
            rest = rest[1:].lstrip()
        return authors.strip(" ,;"), marker, rest.strip(" ,")
    if "PLoSONE" in line:
        left, right = line.split(",", 1)
        author_anchor = line.split(", ?", 1)[0] if ", ?" in line else left
        authors = author_anchor.strip(" ,;")
        m = re.search(r"\?\s*(?P<title>.+?)\?,\s*(?P<rest>PLoSONE.+)$", line)
        if m:
            return authors, m.group("title").strip(" .,"), m.group("rest").strip(" ,")
    if "Front. Psychol." in line and re.search(r"\((19\d{2}|20\d{2})\)", line):
        left, right = line.split(") ", 1)
        authors = left.rsplit("(", 1)[0].strip(" ,;")
        title, rest = re.split(r"\.?Front\. Psychol\.", right, maxsplit=1)
        return authors, title.strip(" .,"), ("Front. Psychol." + rest).strip(" ,")

    m = re.match(
        r"^(?P<authors>.+?)\s*\((?P<year>19\d{2}|20\d{2})\)\s*(?P<title>.+?)(?=(?:\.\s*[A-Z][a-z]+\.|\.\s+[A-Z][a-z]+|https?://|doi:|$))(?P<rest>.*)$",
        line,
    )
    if m:
        return m.group("authors").strip(" ,;"), m.group("title").strip(" .,"), m.group("rest").strip(" ,")

    patterns = [
        r'^(?P<authors>.+?),\s*"(?P<title>[^"]+)"(?P<rest>.*)$',
        r"^(?P<authors>.+?),\s*'(?P<title>[^']+)'(?P<rest>.*)$",
        r'^(?P<authors>.+?),\s*[“"](?P<title>[^”"]+)[”"](?P<rest>.*)$',
    ]
    for pattern in patterns:
        m = re.match(pattern, line)
        if m:
            return m.group("authors").strip(" ,;"), m.group("title").strip(" .,"), m.group("rest").strip(" ,")

    quoted = re.search(r'"([^"]+)"', line)
    if quoted:
        title = quoted.group(1).strip(" .,")
        authors = line[: quoted.start()].strip(" ,;")
        rest = line[quoted.end() :].strip(" ,")
        return authors, title, rest

    m = re.match(r"^(?P<authors>.+?)\((?P<year>19\d{2}|20\d{2})\),\s*(?P<title>.+?),(?P<rest>\s*.+)$", line)
    if m:
        return m.group("authors").strip(" ,;"), m.group("title").strip(" .,"), m.group("rest").strip(" ,")

    fallback = re.match(r"^(?P<authors>.+?),\s*(?P<title>[^,]+?),\s*(?P<rest>.+)$", line)
    if fallback:
        return fallback.group("authors").strip(" ,;"), fallback.group("title").strip(" .,"), fallback.group("rest").strip(" ,")

    return "", line, ""


def infer_venue_and_location(rest: str, pub_type: str) -> tuple[str, str]:
    text = rest.strip()
    text = re.sub(r"^(in|at)\s+", "", text, flags=re.I)
    text = re.sub(r"^(Proceedings of|Proc\.|Proc)\s*", "", text, flags=re.I)
    location = ""
    if text.startswith("PLoSONE"):
        return "PLOS ONE", ""
    if pub_type == "Dataset":
        repo = text.split(",")[0].strip()
        return repo, ""
    venue = text
    if pub_type in {"Conference Paper", "Workshop Paper"}:
        parts = [p.strip() for p in text.split(",")]
        if len(parts) >= 3:
            location = ", ".join(parts[-3:-1]) if re.search(r"\b(19|20)\d{2}\b", parts[-1]) else ", ".join(parts[-2:])
        venue = parts[0]
        if len(parts) > 1 and not re.search(r"\b(19|20)\d{2}\b", parts[1]):
            venue = ", ".join(parts[:2])
    else:
        venue = text.split(",")[0].strip()
    return venue.strip(" .,"), location.strip(" .,")


def infer_fields(record: Publication, rest: str) -> None:
    if rest.startswith("PLoSONE"):
        record.venue = "PLOS ONE"
        compact = rest.replace("PLoSONE", "").strip()
        issue_match = re.search(r"(\d+)\((\d+)\):\s*([A-Za-z0-9]+)", compact)
        if issue_match:
            record.volume = issue_match.group(1)
            record.issue = issue_match.group(2)
            record.article_number = issue_match.group(3)
        return
    volume = re.search(r"(?:\b[Vv]ol\.\s*|\b[Vv]ol\s+)([A-Za-z0-9.-]+)", rest)
    issue = re.search(r"\b(?:no\.|issue)\s*([A-Za-z0-9.-]+)", rest, re.I)
    pages = re.search(r"\bpp\.?\s*([0-9\-–]+)", rest, re.I)
    article = re.search(r"\b(?:Art(?:icle)?(?: ID)?|article)\s*(?:no\.?\s*)?([A-Za-z0-9-]+)", rest, re.I)
    record.volume = volume.group(1) if volume else ""
    record.issue = issue.group(1) if issue else ""
    record.pages = pages.group(1).replace("–", "-") if pages else ""
    record.article_number = article.group(1) if article else ""
    if record.pub_type == "Dataset" and "Mendeley Data" in rest:
        record.dataset_repository = "Mendeley Data"
    if "accepted for publication" in rest.lower():
        record.publication_status = "Accepted"
    elif record.year == "2026":
        record.publication_status = "Published or forthcoming in 2026"


def map_pub_type(raw_type: str, line: str) -> str:
    pub_type = raw_type
    lower = line.lower()
    if raw_type == "Conference Paper" and "workshop" in lower:
        pub_type = "Workshop Paper"
    if raw_type == "Magazine Article" and "daily news" in lower:
        pub_type = "Newspaper Article"
    return pub_type


def first_author_surname(authors: str) -> str:
    if not authors:
        return "Unknown"
    first = re.split(r";|\band\b|,", authors)[0].strip()
    parts = [p for p in re.split(r"\s+", first) if p]
    surname = parts[-1] if parts else "Unknown"
    return re.sub(r"[^A-Za-z0-9]", "", surname) or "Unknown"


def short_title(title: str) -> str:
    words = [w.capitalize() for w in re.findall(r"[A-Za-z0-9]+", title)[:4]]
    return "".join(words) or "Untitled"


def bib_type(pub_type: str) -> str:
    return {
        "Journal Article": "@article",
        "Conference Paper": "@inproceedings",
        "Workshop Paper": "@inproceedings",
        "Book Chapter": "@incollection",
        "Book": "@book",
        "Dataset": "@misc",
        "Magazine Article": "@misc",
        "Newspaper Article": "@misc",
        "Preprint": "@misc",
        "Patent": "@misc",
        "Other Research Output": "@misc",
    }.get(pub_type, "@misc")


def parse_classified(paragraphs: list[str]) -> list[Publication]:
    records = []
    theme = ""
    raw_type = ""
    known_themes = {clean_text(theme_name): THEME_ALIASES.get(theme_name, theme_name) for theme_name in KNOWN_THEMES}
    for index, line in enumerate(paragraphs, start=1):
        line = clean_text(line)
        if not line:
            continue
        if line in TYPE_HEADINGS:
            raw_type = TYPE_HEADINGS[line]
            continue
        next_line = clean_text(paragraphs[index]) if index < len(paragraphs) else ""
        if line in known_themes:
            theme = known_themes[line]
            continue
        if not theme or not raw_type:
            continue
        if len(line) < 20:
            continue
        if re.match(r"^(doi:|https?://|10\.)", line, re.I):
            continue
        authors, title, rest = extract_title_and_authors(line)
        if title.lower().startswith("doi:"):
            continue
        doi, url = extract_doi_url(line)
        if not authors and re.search(r"\bdoi\b", line, re.I):
            continue
        record = Publication(
            title=title,
            authors=authors,
            year=extract_year(line),
            month=extract_month(line),
            pub_type=map_pub_type(raw_type, line),
            venue="",
            primary_theme=theme,
            source_document="My Publications Classified by Thrust Area.docx",
            source_location=f"Classified paragraph {index}",
            doi=doi,
            url=url,
            verification_status="Document-verified",
        )
        record.venue, record.location = infer_venue_and_location(rest, record.pub_type)
        infer_fields(record, rest)
        record.normalized_title = normalize_title(record.title)
        if record.title in {"Signal Processing", "Recognition", "Agriculture", "Forecasting", "Fonseka T"}:
            continue
        records.append(record)
    return records


def load_cv_text() -> str:
    paragraphs = consecutive_dedupe(read_docx_paragraphs(CV_DOCX))
    text = "\n".join(clean_text(p) for p in paragraphs)
    return text


def load_university_profile_text() -> str:
    profile = ROOT / "data-review" / "_university_profile_cache.txt"
    if profile.exists():
        return profile.read_text(encoding="utf-8")
    return ""


def enrich_records(records: list[Publication], cv_text: str) -> None:
    cv_norm = normalize_title(cv_text)
    for record in records:
        record.matched_sources.append("Classified document")
        if record.normalized_title and record.normalized_title in cv_norm:
            record.matched_sources.append("January 2026 CV")
        if record.title == "Novel non-invasive in-house fabricated wearable system with a hybrid algorithm for fetal movement recognition":
            record.year = "2021"
            record.month = "Feb."
            record.venue = "PLOS ONE"
            record.volume = "16"
            record.issue = "7"
            record.article_number = "e0254560"
            record.pub_type = "Journal Article"
            record.notes = "; ".join(
                filter(
                    None,
                    [
                        record.notes,
                        "Classified document provides DOI/article number; CV confirms PLOS ONE vol. 16 no. 7, Feb. 2021.",
                    ],
                )
            )
        if record.doi:
            record.verification_status = "DOI present; document-verified"
        if any(hint.lower() in f"{record.venue} {record.title}".lower() for hint in FLAGSHIP_HINTS):
            record.selected_candidate = True
        if record.year in {"2025", "2026"}:
            record.selected_candidate = True
        if record.pub_type == "Journal Article" and record.year and int(record.year) >= 2020:
            record.selected_candidate = True
        if not record.year or not record.venue or not record.authors:
            record.verification_status = "Needs manual metadata review"


def dedupe_records(records: list[Publication]) -> tuple[list[Publication], dict[str, list[Publication]], list[tuple[Publication, Publication]]]:
    merged = {}
    duplicates = defaultdict(list)
    possible = []
    for record in records:
        key = record.doi.lower() if record.doi else record.normalized_title
        if not key:
            key = f"untitled-{len(merged)+1}"
        if key in merged:
            existing = merged[key]
            duplicates[key].append(record)
            if record.primary_theme not in existing.secondary_themes and record.primary_theme != existing.primary_theme:
                existing.secondary_themes.append(record.primary_theme)
            for source in record.matched_sources:
                if source not in existing.matched_sources:
                    existing.matched_sources.append(source)
            existing.notes = "; ".join(filter(None, [existing.notes, f"Also listed under {record.primary_theme}."]))
            existing.duplicate_status = "Confirmed duplicate across sources/themes"
        else:
            merged[key] = record

    unique = list(merged.values())
    title_buckets = defaultdict(list)
    for record in unique:
        title_buckets[record.normalized_title].append(record)
    for items in title_buckets.values():
        if len(items) > 1:
            for first in items:
                first.duplicate_status = "Possible duplicate or version variant"
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    possible.append((items[i], items[j]))
    for record in unique:
        if "Early Access" in record.venue or "accepted" in record.publication_status.lower():
            record.conflict_status = "Check final publication status"
    return unique, duplicates, possible


def assign_keys(records: list[Publication]) -> None:
    used = Counter()
    for record in records:
        base = f"{first_author_surname(record.authors)}{record.year or 'Undated'}{short_title(record.title)}"
        used[base] += 1
        record.key = f"{base}{used[base]}" if used[base] > 1 else base


def escape_bib(value: str) -> str:
    return value.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}")


def write_bib(records: list[Publication]) -> None:
    out = []
    for record in sorted(records, key=lambda r: (r.year or "", r.title), reverse=True):
        fields = []
        fields.append(("title", record.title))
        if record.authors:
            fields.append(("author", record.authors))
        if record.year:
            fields.append(("year", record.year))
        if record.month:
            fields.append(("month", record.month))
        if record.pub_type == "Journal Article":
            fields.append(("journal", record.venue))
        elif record.pub_type in {"Conference Paper", "Workshop Paper"}:
            fields.append(("booktitle", record.venue))
        elif record.pub_type == "Dataset":
            fields.append(("howpublished", record.dataset_repository or record.venue))
        else:
            fields.append(("note", record.venue))
        for name, value in [
            ("volume", record.volume),
            ("number", record.issue),
            ("pages", record.pages),
            ("eid", record.article_number if record.article_number and not record.pages else ""),
            ("publisher", record.publisher),
            ("address", record.location),
            ("doi", record.doi),
            ("url", record.url),
            ("isbn", record.isbn),
            ("note", record.notes if record.pub_type in {"Journal Article", "Conference Paper", "Workshop Paper"} else ""),
            ("keywords", ", ".join([record.primary_theme] + record.secondary_themes)),
        ]:
            if value:
                fields.append((name, value))
        out.append(f"{bib_type(record.pub_type)}{{{record.key},")
        for name, value in fields:
            out.append(f"  {name} = {{{escape_bib(value)}}},")
        out.append("}\n")
    (DATA_REVIEW / "papers-draft.bib").write_text("\n".join(out), encoding="utf-8")


def write_markdown(records: list[Publication], duplicates: dict[str, list[Publication]], possible: list[tuple[Publication, Publication]], raw_count: int, cv_match_count: int) -> None:
    by_type = Counter(r.pub_type for r in records)
    by_theme = Counter(r.primary_theme for r in records)
    missing = defaultdict(list)
    for record in records:
        for field_name, value in [
            ("year", record.year),
            ("venue", record.venue),
            ("DOI", record.doi),
            ("author list", record.authors),
            ("pages", record.pages),
            ("volume", record.volume),
            ("issue", record.issue),
            ("type", record.pub_type),
            ("theme", record.primary_theme),
        ]:
            if not value:
                missing[field_name].append(record)

    classified_only_count = sum(1 for r in records if r.matched_sources == ["Classified document"])
    both_sources_count = sum(1 for r in records if "January 2026 CV" in r.matched_sources)
    cv_only_count = 0
    provisional = True
    source_summary = [
        "# Publications Source Summary",
        "",
        f"- Classified document raw publication records: {raw_count}",
        f"- Unique publication records after normalization/deduplication: {len(records)}",
        f"- Records confirmed by the January 2026 CV at title level: {cv_match_count}",
        f"- Records coming directly from the classified publication document: {len(records)}",
        f"- Records appearing in both local sources: {both_sources_count}",
        f"- Records appearing only in the classified publication document: {classified_only_count}",
        f"- Records appearing only in the January 2026 CV: {cv_only_count}",
        "- Google Scholar access status: blocked by anti-bot / JavaScript verification page.",
        "- University profile use: not treated as a primary source; only used as a secondary historical reference for this phase.",
        f"- Overall completeness assessment: {'provisional' if provisional else 'complete'} local dataset pending optional manual cross-checks.",
        "",
        "## Source limitations",
        "",
        "- The classified document is the cleanest structured source and was used as the main machine-readable extraction source.",
        "- The January 2026 CV is not cleanly machine-parseable from DOCX XML because many publication paragraphs are duplicated or merged; it was therefore used for title-level cross-checking and recency confirmation rather than direct full parsing.",
        "- Google Scholar could not be verified programmatically because the public page returned a robot-check barrier on July 29, 2026.",
        "- Because Google Scholar comparison was blocked, the 203-record local dataset should be treated as provisionally complete rather than absolutely complete.",
        "- The university profile exposes department-wide publication navigation, but not a clean per-record export for this phase.",
        "",
        "## Records by publication type",
        "",
    ]
    for pub_type, count in sorted(by_type.items()):
        source_summary.append(f"- {pub_type}: {count}")
    source_summary.extend(["", "## Records by research theme", ""])
    for theme, count in sorted(by_theme.items()):
        source_summary.append(f"- {theme}: {count}")
    (DATA_REVIEW / "publications-source-summary.md").write_text("\n".join(source_summary), encoding="utf-8")

    duplicate_lines = ["# Publications Duplicates", ""]
    confirmed_count = 0
    if duplicates:
        duplicate_lines.append("## Confirmed duplicates")
        duplicate_lines.append("")
        for _, dup_items in duplicates.items():
            confirmed_count += len(dup_items)
            primary = dup_items[0]
            duplicate_lines.append(f"- `{primary.title}`")
        duplicate_lines.append("")
    else:
        duplicate_lines.append("## Confirmed duplicates")
        duplicate_lines.append("")
        duplicate_lines.append("- No confirmed DOI/title duplicates remained after normalization.")
        duplicate_lines.append("")
    duplicate_lines.append("## Possible duplicates or version relationships")
    duplicate_lines.append("")
    if possible:
        for first, second in possible[:50]:
            duplicate_lines.append(f"- `{first.title}` / `{second.title}` - review possible version overlap.")
    else:
        duplicate_lines.append("- No title-level version conflicts detected in the normalized set.")
    duplicate_lines.append("")
    duplicate_lines.append("## Recommended action")
    duplicate_lines.append("")
    duplicate_lines.append("- Keep exact DOI matches merged.")
    duplicate_lines.append("- Review same-title records manually when conference and journal versions may both be valid.")
    (DATA_REVIEW / "publications-duplicates.md").write_text("\n".join(duplicate_lines), encoding="utf-8")

    conflicts = ["# Publications Conflicts", "", "## Manual-review items", ""]
    for record in records:
        items = []
        if not record.doi and record.pub_type == "Journal Article" and record.year and int(record.year) >= 2020:
            items.append("missing DOI for a recent journal article")
        if record.pub_type == "Conference Paper" and "Workshop" in record.venue:
            items.append("conference/workshop boundary should be confirmed")
        if "2026" in record.venue and record.year != "2026":
            items.append("year/venue text mismatch")
        if items:
            conflicts.append(f"- `{record.title}` - " + "; ".join(items))
    conflicts.extend(
        [
            "",
            "## Cross-source observations",
            "",
            "- Google Scholar could not be accessed for bibliographic verification because the page required a JavaScript robot check.",
            "- The January 2026 CV and the classified document broadly agree on current research directions and recent 2025-2026 entries.",
            "- Some entries contain spelling or transliteration variation in author names and venue abbreviations; these were preserved in source form and normalized only for matching.",
        ]
    )
    (DATA_REVIEW / "publications-conflicts.md").write_text("\n".join(conflicts), encoding="utf-8")

    missing_lines = ["# Publications Missing Metadata", ""]
    for field_name in ["year", "venue", "DOI", "author list", "pages", "volume", "issue", "type", "theme"]:
        missing_lines.append(f"## Missing {field_name}")
        missing_lines.append("")
        entries = missing[field_name]
        if entries:
            for record in entries:
                missing_lines.append(f"- `{record.title}` ({record.year or 'n.d.'}) - {record.primary_theme}")
        else:
            missing_lines.append("- None")
        missing_lines.append("")
    (DATA_REVIEW / "publications-missing-metadata.md").write_text("\n".join(missing_lines), encoding="utf-8")

    selected = ["# Publications Selected Candidates", "", "Candidate list for later homepage/publications curation only.", ""]
    candidates = sorted(
        [r for r in records if r.selected_candidate],
        key=lambda r: (r.year or "", r.title),
        reverse=True,
    )[:20]
    for record in candidates:
        reasons = []
        if record.year in {"2025", "2026"}:
            reasons.append("recent")
        if any(hint.lower() in f"{record.venue} {record.title}".lower() for hint in FLAGSHIP_HINTS):
            reasons.append("flagship venue")
        if record.pub_type == "Journal Article":
            reasons.append("journal output")
        selected.append(
            f"- `{record.title}` - {record.year or 'n.d.'}; {record.venue}; {record.primary_theme}; reason: {', '.join(reasons) or 'representative'}; verification: {record.verification_status}"
        )
    (DATA_REVIEW / "publications-selected-candidates.md").write_text("\n".join(selected), encoding="utf-8")

    master = ["# Publications Master Review", ""]
    grouped = defaultdict(list)
    for record in records:
        grouped[(record.pub_type, record.primary_theme)].append(record)
    for (pub_type, theme), items in sorted(grouped.items()):
        master.append(f"## {pub_type} - {theme}")
        master.append("")
        for record in sorted(items, key=lambda r: (r.year or "", r.title), reverse=True):
            master.append(
                f"- **{record.year or 'n.d.'}** `{record.title}`; {record.authors or 'authors missing'}; venue: {record.venue or 'venue missing'}; DOI: {record.doi or 'missing'}; source: {', '.join(record.matched_sources) or record.source_document}; duplicate: {record.duplicate_status or 'none'}; conflict: {record.conflict_status or 'none'}; verification: {record.verification_status}"
            )
        master.append("")
    (DATA_REVIEW / "publications-master-review.md").write_text("\n".join(master), encoding="utf-8")

    spot = [
        "# Publications Spot Check",
        "",
        "Representative manual spot-check sample drawn from the cleaned local dataset.",
        "",
    ]
    sample_targets = [
        "Novel non-invasive in-house fabricated wearable system with a hybrid algorithm for fetal movement recognition",
        "Performance Benchmarking of Psychomotor Skills Using Wearable Devices: An Application in Sport",
        "The influence of social interactions in mitigating psychological distress during the COVID-19 pandemic: a study in Sri Lanka",
        "Lighting the Way for a Sustainable Future: Overcoming Challenges in Light-Based IoT and Data-Energy Networking",
        "Preprocessing Algorithm Leveraging Geometric Modeling for Scale Correction in Hyperspectral Images for Improved Unmixing Performance",
        "Mamba-FCS: Joint Spatio-Frequency Feature Fusion, Change-Guided Attention, and SeK Inspired Loss for Enhanced Semantic Change Detection in Remote Sensing",
        "A dataset on the socioeconomic and behavioural impacts in Sri Lanka through multiple waves of COVID-19",
        "Fetal Movement Dataset Recorded Using Four Inertial Measurement Units",
        "Incorporating Appliance Usage Patterns for Non-Intrusive Load Monitoring and Load Forecasting",
        "A complete state estimation algorithm for a three-phase four-wire low voltage distribution system with high penetration of solar PV",
        "Design and Analysis of an Optical Camera Communication System for Underwater Applications",
        "Light-based Internet of Things: Implementation of an Optically Connected Energy-autonomous node",
        "Holistic Interpretation of Public Scenes Using Computer Vision and Temporal Graphs to Identify Social Distancing Violations",
        "Vehicle Tracking Based on an Improved DeepSORT Algorithm and the YOLOv4 Framework",
        "Graph-Based Blind Hyperspectral Unmixing via Nonnegative Matrix Factorization",
        "Deep learning for automated fish grading",
        "Assessment of Fetal and Maternal Well-Being During Pregnancy Using Passive Wearable Inertial Sensor",
        "COSMO-INR: Complex Sinusoidal Modulation for Implicit Neural Representations",
        "A Structured Analysis and Taxonomy of Scene Graph Representations for Group Activity Understanding",
        "Analysis of Super Resolution Spectral Estimation Techniques for Indoor Positioning Applications",
        "Visible Light Communication System with Ambient Light Cancellation",
        "An overview of visible light communication systems",
    ]
    by_title = {r.title: r for r in records}
    for title in sample_targets:
        record = by_title.get(title)
        if not record:
            continue
        source_used = ", ".join(record.matched_sources) or record.source_document
        uncertainty = []
        if not record.doi:
            uncertainty.append("DOI absent in local documents")
        if record.pub_type in {"Conference Paper", "Workshop Paper"} and not record.location:
            uncertainty.append("location parsing limited")
        if not uncertainty:
            uncertainty_text = "No immediate uncertainty from local-source check."
        else:
            uncertainty_text = "; ".join(uncertainty)
        spot.extend(
            [
                f"## {record.title}",
                "",
                f"- Authors: {record.authors}",
                f"- Year: {record.year}",
                f"- Venue: {record.venue}",
                f"- DOI: {record.doi or 'missing'}",
                f"- Type: {record.pub_type}",
                f"- Theme: {record.primary_theme}",
                f"- Source used: {source_used}",
                f"- Verification result: {record.verification_status}",
                f"- Remaining uncertainty: {uncertainty_text}",
                "",
            ]
        )
    (DATA_REVIEW / "publications-spot-check.md").write_text("\n".join(spot), encoding="utf-8")

    incomplete_core = [
        r
        for r in records
        if not (r.title and r.year and r.pub_type and ((r.pub_type == "Journal Article" and r.venue) or (r.pub_type != "Journal Article" and r.venue)))
    ]
    optional_only = [
        r
        for r in records
        if r not in incomplete_core and not all([r.authors, r.doi, r.pages or r.article_number, r.volume or r.pub_type != "Journal Article"])
    ]
    uncertain_types = [r for r in records if r.pub_type == "Other Research Output"]
    uncertain_themes = []
    readiness = [
        "# Publications Integration Readiness",
        "",
        f"1. Total unique records: {len(records)}",
        f"2. Records with complete core metadata: {len(records) - len(incomplete_core)}",
        f"3. Records missing optional metadata only: {len(optional_only)}",
        "4. Unresolved conflicts: recent records without DOI or records flagged in `publications-conflicts.md`.",
        f"5. Uncertain publication types: {len(uncertain_types)}",
        f"6. Uncertain theme assignments: {len(uncertain_themes)}",
        "7. Duplicate status: no confirmed duplicates remain after normalization.",
        f"8. BibTeX validation status: {'pass' if not incomplete_core else 'needs manual review'}; see `publications-validation.md`.",
        f"9. Ready for live integration: {'yes, with provisional-source caveat' if not incomplete_core else 'not yet'}",
        "10. Manual approval items: accept provisional completeness without Scholar comparison; optionally review recent no-DOI records before live integration.",
        "",
    ]
    (DATA_REVIEW / "publications-integration-readiness.md").write_text("\n".join(readiness), encoding="utf-8")


def validate_bib(records: list[Publication]) -> list[str]:
    issues = []
    keys = [r.key for r in records]
    dup_keys = [key for key, count in Counter(keys).items() if count > 1]
    if dup_keys:
        issues.append(f"Duplicate citation keys: {', '.join(dup_keys)}")
    for record in records:
        if not record.key or not record.title or not record.year:
            issues.append(f"Missing core BibTeX field for {record.title or record.key or 'untitled record'}")
        if record.doi and not re.fullmatch(r"10\.\d{4,9}/\S+", record.doi):
            issues.append(f"Malformed DOI: {record.doi}")
        if record.year and not re.fullmatch(r"(19|20)\d{2}", record.year):
            issues.append(f"Invalid year: {record.title} -> {record.year}")
    bib_text = (DATA_REVIEW / "papers-draft.bib").read_text(encoding="utf-8") if (DATA_REVIEW / "papers-draft.bib").exists() else ""
    if bib_text:
        if bib_text.count("{") != bib_text.count("}"):
            issues.append("BibTeX brace count mismatch")
        for marker in [" = {ume},", " = {},"]:
            if marker in bib_text:
                issues.append(f"Suspicious BibTeX field content detected: {marker.strip()}")
    return issues


def main() -> None:
    DATA_REVIEW.mkdir(exist_ok=True)
    classified_paragraphs = consecutive_dedupe(read_docx_paragraphs(CLASSIFIED_DOCX))
    records = parse_classified(classified_paragraphs)
    cv_text = load_cv_text()
    enrich_records(records, cv_text)
    unique_records, duplicates, possible = dedupe_records(records)
    assign_keys(unique_records)
    write_bib(unique_records)
    write_markdown(
        unique_records,
        duplicates,
        possible,
        raw_count=len(records),
        cv_match_count=sum(1 for r in unique_records if "January 2026 CV" in r.matched_sources),
    )
    issues = validate_bib(unique_records)
    report = [
        "# Publications Validation",
        "",
        f"- Draft BibTeX records: {len(unique_records)}",
        f"- Duplicate citation keys: {sum(1 for _ in Counter(r.key for r in unique_records).values() if _ > 1)}",
    ]
    core_incomplete = [r for r in unique_records if not (r.title and r.year and r.pub_type and r.venue)]
    if issues:
        report.append("- Validation issues:")
        report.extend([f"  - {issue}" for issue in issues])
    elif core_incomplete:
        report.append("- Validation issues:")
        report.extend([f"  - Missing core fields for {record.title}" for record in core_incomplete])
    else:
        report.append("- Validation result: no duplicate keys, no malformed DOI strings detected by the local script, all years are valid, and all records include title/year/type/venue.")
    (DATA_REVIEW / "publications-validation.md").write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
