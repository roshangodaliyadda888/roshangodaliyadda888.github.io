#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


NAMESPACES = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pkgrel": "http://schemas.openxmlformats.org/package/2006/relationships",
}

PLACEHOLDER_VALUES = {"", "-", "—", "n/a", "na", "nan", "none", "null", "nil"}

COUNTRY_NORMALIZATIONS = {
    "usa": "United States",
    "u.s.a.": "United States",
    "us": "United States",
    "u.s.": "United States",
    "united states of america": "United States",
    "uk": "United Kingdom",
    "u.k.": "United Kingdom",
    "great britain": "United Kingdom",
    "uae": "United Arab Emirates",
    "austrailia": "Australia",
    "australia": "Australia",
    "canada": "Canada",
    "germany": "Germany",
    "finland": "Finland",
}

UNIVERSITY_NORMALIZATIONS = {
    "university of new south wales, sydney": "University of New South Wales",
    "university of new south wales": "University of New South Wales",
    "the university of melbourne": "University of Melbourne",
    "university of melbourne": "University of Melbourne",
    "university of maryland": "University of Maryland, College Park",
    "university of maryland college park": "University of Maryland, College Park",
    "university of maryland, college park": "University of Maryland, College Park",
    "university of maryland, college park.": "University of Maryland, College Park",
    "the university of maryland": "University of Maryland, College Park",
    "the university of maryland, college park": "University of Maryland, College Park",
    "university of maryland-college park": "University of Maryland, College Park",
    "university of california san diego": "University of California, San Diego",
    "university of california, san diego": "University of California, San Diego",
    "university of california, los angeles": "University of California, Los Angeles",
    "tu munich": "Technical University of Munich",
    "johns hopkings university": "Johns Hopkins University",
    "johns hopkins": "Johns Hopkins University",
    "johns hopkins university": "Johns Hopkins University",
    "tennesse tech": "Tennessee Technological University",
    "rensselaer polytechnic institute, new york": "Rensselaer Polytechnic Institute",
    "university of technology sydney": "University of Technology Sydney",
    "university of british columbia": "University of British Columbia",
    "ohio state university": "Ohio State University",
    "university of illinois at urbana-champaign": "University of Illinois Urbana-Champaign",
    "rutgers university": "Rutgers University",
    "princeton university": "Princeton University",
    "swinburne university of technology": "Swinburne University of Technology",
    "state university of new york at albany": "University at Albany, SUNY",
    "australia national university": "Australian National University",
    "western illinios university": "Western Illinois University",
}

UNIVERSITY_COUNTRY_REFERENCE = {
    "Australian National University": "Australia",
    "Boston University": "United States",
    "Clemson University": "United States",
    "Columbia University": "United States",
    "Cornell University": "United States",
    "Johns Hopkins University": "United States",
    "Monash University": "Australia",
    "Northeastern University": "United States",
    "Ohio State University": "United States",
    "Princeton University": "United States",
    "Purdue University": "United States",
    "Rensselaer Polytechnic Institute": "United States",
    "Rutgers University": "United States",
    "Simon Fraser University": "Canada",
    "Southern Illinois University": "United States",
    "State University of New York at Albany": "United States",
    "Swinburne University of Technology": "Australia",
    "Technical University of Munich": "Germany",
    "Tennessee Technological University": "United States",
    "The University of Melbourne": "Australia",
    "TU Munich": "Germany",
    "University at Albany, SUNY": "United States",
    "University of Alberta": "Canada",
    "University of British Columbia": "Canada",
    "University of California, San Diego": "United States",
    "University of Illinois Urbana-Champaign": "United States",
    "University of Illinois at Urbana-Champaign": "United States",
    "University of Manitoba": "Canada",
    "University of Maryland, College Park": "United States",
    "University of Melbourne": "Australia",
    "University of Michigan-Ann Arbor": "United States",
    "University of New South Wales": "Australia",
    "University of Oulu": "Finland",
    "University of Technology Sydney": "Australia",
    "University of Western Ontario": "Canada",
    "University of Wollongong": "Australia",
    "Virginia Tech": "United States",
    "Western University": "Canada",
}

MULTI_UNIVERSITY_SEPARATORS = [" / ", "/", ", "]
INSTITUTION_KEYWORDS = (
    "university",
    "institute",
    "college",
    "tech",
    "polytechnic",
    "schule",
    "tu ",
)

CAMPUS_LOCATION_SUFFIXES = {
    "college park",
    "san diego",
    "new york",
    "sydney",
    "los angeles",
    "ontario",
}

AREA_BY_SHEET = {
    "Elec": "Electrical and Electronic Engineering",
    "Computer": "Computer Engineering",
}

STREAM_AREA_MAP = {
    "chemical": "Chemical Engineering",
    "mechanical": "Mechanical Engineering",
    "science": "Science and Interdisciplinary Fields",
    "agriculture/geography": "Science and Interdisciplinary Fields",
    "agriculture": "Science and Interdisciplinary Fields",
    "geography": "Science and Interdisciplinary Fields",
}


def collapse_whitespace(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    value = value.replace("\r\n", "\n").replace("\r", "\n").replace("\u00a0", " ")
    value = value.replace("\u200b", "").replace("\ufeff", "")
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n\s*", "\n", value)
    return value.strip()


def clean_cell(value: object) -> str:
    if value is None:
        return ""
    text = collapse_whitespace(str(value))
    if text.lower() in PLACEHOLDER_VALUES:
        return ""
    return text


def col_to_index(ref: str) -> int:
    match = re.match(r"([A-Z]+)", ref or "")
    if not match:
        return 0
    index = 0
    for char in match.group(1):
        index = index * 26 + (ord(char) - 64)
    return index - 1


def trim_row(row: list[str]) -> list[str]:
    cleaned = [clean_cell(cell) for cell in row]
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return cleaned


def normalize_header_token(value: str) -> str:
    token = re.sub(r"[^a-z0-9]+", " ", clean_cell(value).lower()).strip()
    return token


def detect_header_row(rows: list[list[str]]) -> int:
    required = {"name", "batch", "university"}
    best_index = -1
    best_score = -1
    for index, row in enumerate(rows[:12]):
        tokens = {normalize_header_token(cell) for cell in row if clean_cell(cell)}
        score = sum(1 for token in tokens if token in {"name", "batch", "university", "country", "current affiliation", "stream"})
        if required.issubset(tokens):
            score += 10
        if score > best_score:
            best_index = index
            best_score = score
    return best_index


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_value.lower()).strip("-")
    return slug or "student"


def normalize_name(name: str) -> str:
    return clean_cell(name)


def normalize_batch(batch: str, warnings: dict[str, list[str]], source_label: str) -> str:
    value = clean_cell(batch)
    if not value:
        warnings["missing_batch"].append(source_label)
        return ""
    compact = re.sub(r"\s+", "", value).upper()
    match = re.fullmatch(r"([A-Z]+)(\d{2})(.*)", compact)
    if match:
        prefix, digits, suffix = match.groups()
        normalized = f"{prefix}{digits}{suffix}"
        if normalized != value:
            warnings["normalized_batches"].append(f"{source_label}: {value} → {normalized}")
        if suffix:
            warnings["uncertain_batches"].append(f"{source_label}: {normalized}")
        return normalized
    warnings["uncertain_batches"].append(f"{source_label}: {value}")
    return value


def normalize_country(country: str, warnings: dict[str, list[str]], source_label: str) -> str:
    value = clean_cell(country)
    if not value:
        warnings["missing_countries"].append(source_label)
        return ""
    key = value.lower().rstrip(".")
    normalized = COUNTRY_NORMALIZATIONS.get(key, value)
    if normalized != value:
        warnings["country_corrections"].append(f"{source_label}: {value} → {normalized}")
    return normalized


def normalize_degree_terms(text: str) -> str:
    text = re.sub(r"\bPh\.?D\.?\b", "PhD", text, flags=re.IGNORECASE)
    return text


def normalize_affiliation(value: str) -> str:
    text = clean_cell(value)
    if not text:
        return ""
    text = normalize_degree_terms(text)
    text = re.sub(r"\s*,\s*", ", ", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip(" ,")


def split_universities(value: str) -> list[str]:
    text = clean_cell(value)
    if not text:
        return []
    if "/" in text:
        return [segment.strip() for segment in text.split("/") if segment.strip()]
    if ";" in text:
        return [segment.strip() for segment in text.split(";") if segment.strip()]
    if ", " in text:
        segments = [segment.strip() for segment in text.split(", ") if segment.strip()]
        if len(segments) == 2:
            left, right = segments
            right_key = right.lower().strip(" .")
            if right_key in CAMPUS_LOCATION_SUFFIXES:
                return [text]
            if any(keyword in left.lower() for keyword in INSTITUTION_KEYWORDS) and any(
                keyword in right.lower() for keyword in INSTITUTION_KEYWORDS
            ):
                return segments
    return [text]


def normalize_university_piece(value: str, warnings: dict[str, list[str]], source_label: str) -> str:
    text = clean_cell(value).strip(" .")
    if not text:
        return ""
    text = re.sub(r"\s*,\s*", ", ", text)
    text = re.sub(r"\s{2,}", " ", text)
    raw_key = text.lower()
    normalized = UNIVERSITY_NORMALIZATIONS.get(raw_key, text)
    if normalized != text:
        warnings["university_corrections"].append(f"{source_label}: {text} → {normalized}")
    if normalized.endswith("(Pure Maths)"):
        normalized = "University of Illinois Urbana-Champaign"
        warnings["university_corrections"].append(f"{source_label}: {text} → {normalized}")
    if normalized.endswith("(Physics)"):
        normalized = "Ohio State University"
        warnings["university_corrections"].append(f"{source_label}: {text} → {normalized}")
    return normalized


def normalize_university(value: str, warnings: dict[str, list[str]], source_label: str) -> tuple[str, list[str]]:
    if not clean_cell(value):
        warnings["missing_universities"].append(source_label)
        return "", []
    parts = split_universities(value)
    universities = []
    for part in parts:
        normalized_part = normalize_university_piece(part, warnings, source_label)
        if normalized_part:
            universities.append(normalized_part)
    universities = list(dict.fromkeys(universities))
    if len(universities) > 1:
        warnings["multi_university_records"].append(f"{source_label}: {'; '.join(universities)}")
    display = "; ".join(universities)
    return display, universities


def normalize_area(sheet_name: str, stream_value: str, warnings: dict[str, list[str]], source_label: str) -> str:
    if sheet_name in AREA_BY_SHEET:
        return AREA_BY_SHEET[sheet_name]
    stream = clean_cell(stream_value).lower()
    if stream in STREAM_AREA_MAP:
        return STREAM_AREA_MAP[stream]
    if stream:
        warnings["uncertain_categories"].append(f"{source_label}: {stream_value}")
        return "Other Engineering Fields"
    warnings["uncertain_categories"].append(f"{source_label}: missing stream")
    return "Other Engineering Fields"


def logical_batch_key(batch: str) -> tuple[str, int, str]:
    match = re.match(r"([A-Z]+)(\d+)(.*)", batch or "")
    if match:
        prefix, digits, suffix = match.groups()
        return prefix, int(digits), suffix
    return batch or "ZZZ", 9999, ""


def normalize_for_duplicate_check(value: str) -> str:
    value = slugify(value)
    return value


def yaml_escape(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def write_yaml(records: list[dict], output_path: Path) -> None:
    lines: list[str] = []
    for record in records:
        lines.append(f"- name: {yaml_escape(record['name'])}")
        for key in [
            "slug",
            "batch",
            "university",
            "country",
            "academic_area",
            "current_affiliation",
            "status",
            "sort_name",
            "image",
            "profile_url",
        ]:
            lines.append(f"  {key}: {yaml_escape(record.get(key, ''))}")
        universities = record.get("universities", [])
        if universities:
            lines.append("  universities:")
            for university in universities:
                lines.append(f"    - {yaml_escape(university)}")
        else:
            lines.append("  universities: []")
        lines.append(f"  source_sheet: {yaml_escape(record.get('source_sheet', ''))}")
        lines.append(f"  source_row: {record.get('source_row', 0)}")
        lines.append("")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def load_workbook_rows(workbook_path: Path) -> list[dict]:
    with zipfile.ZipFile(workbook_path) as archive:
        shared_strings: list[str] = []
        if "xl/sharedStrings.xml" in archive.namelist():
            shared_root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            for shared_item in shared_root.findall("main:si", NAMESPACES):
                shared_strings.append("".join(node.text or "" for node in shared_item.iterfind(".//main:t", NAMESPACES)))

        workbook_root = ET.fromstring(archive.read("xl/workbook.xml"))
        rels_root = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
        relations = {
            relation.attrib["Id"]: relation.attrib["Target"]
            for relation in rels_root.findall("pkgrel:Relationship", NAMESPACES)
        }

        sheets: list[dict] = []
        for sheet in workbook_root.find("main:sheets", NAMESPACES):
            relation_id = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
            target = relations[relation_id]
            sheet_path = "xl/" + target if not target.startswith("xl/") else target
            sheet_root = ET.fromstring(archive.read(sheet_path))
            rows: list[list[str]] = []
            for row in sheet_root.findall(".//main:sheetData/main:row", NAMESPACES):
                values: dict[int, str] = {}
                max_index = -1
                for cell in row.findall("main:c", NAMESPACES):
                    column_index = col_to_index(cell.attrib.get("r", ""))
                    max_index = max(max_index, column_index)
                    cell_type = cell.attrib.get("t")
                    value = ""
                    if cell_type == "inlineStr":
                        value = "".join(node.text or "" for node in cell.iterfind(".//main:t", NAMESPACES))
                    else:
                        value_node = cell.find("main:v", NAMESPACES)
                        if value_node is not None and value_node.text is not None:
                            raw_value = value_node.text
                            value = shared_strings[int(raw_value)] if cell_type == "s" else raw_value
                    values[column_index] = value
                row_values = [values.get(index, "") for index in range(max_index + 1)] if max_index >= 0 else []
                rows.append(trim_row(row_values))
            sheets.append({"name": sheet.attrib["name"], "rows": rows})
        return sheets


def build_records(workbook_path: Path, image_dir: Path) -> tuple[list[dict], dict[str, list[str]], dict[str, int]]:
    sheets = load_workbook_rows(workbook_path)
    warnings: dict[str, list[str]] = defaultdict(list)
    stats = {
        "source_rows": 0,
        "valid_records": 0,
        "removed_empty_rows": 0,
        "missing_photo_count": 0,
        "missing_affiliation_count": 0,
    }
    records: list[dict] = []
    slug_counts: Counter[str] = Counter()
    duplicate_buckets: defaultdict[tuple[str, str, str], list[str]] = defaultdict(list)
    name_buckets: defaultdict[str, list[str]] = defaultdict(list)

    for sheet in sheets:
        rows = sheet["rows"]
        stats["removed_empty_rows"] += sum(1 for row in rows if not any(clean_cell(cell) for cell in row))
        nonempty_rows = [row for row in rows if any(clean_cell(cell) for cell in row)]
        header_index = detect_header_row(nonempty_rows)
        if header_index < 0:
            warnings["unimported_rows"].append(f"{sheet['name']}: could not detect header row")
            continue

        header_row = nonempty_rows[header_index]
        header_map: dict[str, int] = {}
        for index, value in enumerate(header_row):
            token = normalize_header_token(value)
            if token in {"name", "batch", "university", "country", "current affiliation", "stream"}:
                header_map[token] = index

        for relative_index, row in enumerate(nonempty_rows[header_index + 1 :], start=header_index + 2):
            if not any(clean_cell(cell) for cell in row):
                continue
            name = clean_cell(row[header_map.get("name", 0)] if header_map.get("name", 0) < len(row) else "")
            if not name:
                warnings["missing_names"].append(f"{sheet['name']} row {relative_index}")
                continue
            stats["source_rows"] += 1
            source_label = f"{sheet['name']} row {relative_index} ({name})"
            batch = normalize_batch(row[header_map.get("batch", 0)] if header_map.get("batch", 0) < len(row) else "", warnings, source_label)
            university, universities = normalize_university(
                row[header_map.get("university", 0)] if header_map.get("university", 0) < len(row) else "",
                warnings,
                source_label,
            )
            country = normalize_country(
                row[header_map.get("country", 0)] if header_map.get("country", 0) < len(row) else "",
                warnings,
                source_label,
            )
            stream = row[header_map.get("stream", 0)] if header_map.get("stream", 0) < len(row) else ""
            academic_area = normalize_area(sheet["name"], stream, warnings, source_label)
            current_affiliation = normalize_affiliation(
                row[header_map.get("current affiliation", 0)] if header_map.get("current affiliation", 0) < len(row) else ""
            )
            if not current_affiliation:
                stats["missing_affiliation_count"] += 1

            for institution in universities:
                expected_country = UNIVERSITY_COUNTRY_REFERENCE.get(institution)
                if expected_country and country and expected_country != country:
                    warnings["university_country_conflicts"].append(
                        f"{source_label}: {institution} is usually associated with {expected_country}, workbook says {country}"
                    )

            normalized_name = normalize_name(name)
            base_slug = slugify(normalized_name)
            if slug_counts[base_slug]:
                suffix_source = batch or str(relative_index)
                unique_slug = slugify(f"{base_slug}-{suffix_source}")
            else:
                unique_slug = base_slug
            slug_counts[unique_slug] += 1

            duplicate_key = (
                normalize_for_duplicate_check(normalized_name),
                batch.upper(),
                normalize_for_duplicate_check(university),
            )
            duplicate_buckets[duplicate_key].append(source_label)
            name_buckets[normalize_for_duplicate_check(normalized_name)].append(source_label)

            image_name = f"{unique_slug}.jpg"
            photo_exists = any((image_dir / f"{unique_slug}{extension}").exists() for extension in [".jpg", ".jpeg", ".png", ".webp"])
            if not photo_exists:
                stats["missing_photo_count"] += 1

            record = {
                "name": normalized_name,
                "slug": unique_slug,
                "batch": batch,
                "university": university,
                "universities": universities,
                "country": country,
                "academic_area": academic_area,
                "current_affiliation": current_affiliation,
                "status": "",
                "sort_name": normalized_name,
                "image": image_name,
                "profile_url": "",
                "source_sheet": sheet["name"],
                "source_row": relative_index,
            }
            records.append(record)

    for key, labels in duplicate_buckets.items():
        if len(labels) > 1:
            warnings["possible_duplicates"].append(" / ".join(labels))
    for _, labels in name_buckets.items():
        if len(labels) > 1:
            warnings["possible_duplicates"].append(" / ".join(labels))

    stats["valid_records"] = len(records)
    records.sort(key=lambda record: (logical_batch_key(record["batch"]), record["name"].lower()))
    return records, warnings, stats


def write_cleanup_report(report_path: Path, workbook_path: Path, records: list[dict], warnings: dict[str, list[str]], stats: dict[str, int]) -> None:
    country_counts = Counter(record["country"] for record in records if record["country"])
    university_counts = Counter(university for record in records for university in record.get("universities", []))
    lines = [
        "# Student Data Cleanup Report",
        "",
        f"- Source workbook: `{workbook_path}`",
        f"- Source rows inspected: {stats['source_rows']}",
        f"- Valid student records: {stats['valid_records']}",
        f"- Removed empty worksheet rows: {stats['removed_empty_rows']}",
        "",
        "## Automatically corrected formatting",
        "",
        f"- Internal whitespace normalization applied across text fields.",
        f"- Degree terminology normalized to `PhD` where it appeared in free-text fields.",
        f"- Comma spacing normalized in affiliations and institution names where safe.",
        "",
    ]

    def add_section(title: str, items: Iterable[str]) -> None:
        entries = list(items)
        lines.append(f"## {title}")
        lines.append("")
        if entries:
            lines.extend(f"- {item}" for item in entries)
        else:
            lines.append("- None")
        lines.append("")

    normalized_items = (
        [f"Country corrections applied: {len(warnings['country_corrections'])}"]
        + [f"University corrections applied: {len(warnings['university_corrections'])}"]
        + [f"Batch normalizations applied: {len(warnings['normalized_batches'])}"]
    )
    add_section("Normalized values", normalized_items)

    add_section("Possible duplicate records", warnings["possible_duplicates"])
    add_section("Country spelling corrections", warnings["country_corrections"])
    add_section("Standardized country names", [f"{country}: {count}" for country, count in sorted(country_counts.items())])
    add_section("Standardized university names", [f"{university}: {count}" for university, count in university_counts.most_common()])
    add_section("University-country conflicts", warnings["university_country_conflicts"])
    add_section("Missing student names", warnings["missing_names"])
    add_section("Missing batch values", warnings["missing_batch"])
    add_section("Missing universities", warnings["missing_universities"])
    add_section("Missing countries", warnings["missing_countries"])
    add_section("Uncertain academic categories", warnings["uncertain_categories"])
    add_section("Records with multiple listed universities", warnings["multi_university_records"])
    add_section("Items requiring professor or MARC-team confirmation", warnings["uncertain_batches"] + warnings["unimported_rows"])

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Import Professor Godaliyadda's student workbook into Jekyll data.")
    parser.add_argument(
        "--input",
        default=r"C:\Users\USER\Downloads\Prof Godaliyadda PhD Students.xlsx",
        help="Path to the source workbook.",
    )
    parser.add_argument("--output", default="_data/students.yml", help="Path to the generated YAML file.")
    parser.add_argument(
        "--report",
        default="data/student_data_cleanup_report.md",
        help="Path to the generated cleanup report.",
    )
    parser.add_argument(
        "--image-dir",
        default="assets/img/students",
        help="Directory containing student profile photographs.",
    )
    args = parser.parse_args()

    workbook_path = Path(args.input)
    output_path = Path(args.output)
    report_path = Path(args.report)
    image_dir = Path(args.image_dir)

    records, warnings, stats = build_records(workbook_path, image_dir)
    write_yaml(records, output_path)
    write_cleanup_report(report_path, workbook_path, records, warnings, stats)

    summary = {
        "records": len(records),
        "missing_photos": stats["missing_photo_count"],
        "missing_affiliations": stats["missing_affiliation_count"],
        "possible_duplicates": len(warnings["possible_duplicates"]),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
