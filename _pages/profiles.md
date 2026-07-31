---
layout: page
permalink: /people/
title: people
description: PhD students and alumni supervised by Professor G. M. R. I. Godaliyadda.
nav: true
nav_order: 7
chart:
  chartjs: true
---

<section class="student-directory-page" aria-labelledby="students-directory-title">
  <header class="student-directory-page__header">
    <p class="student-directory-page__eyebrow">Research Supervision</p>
    <h1 id="students-directory-title">PhD Students and Alumni</h1>
    <p class="student-directory-page__intro">
      An overview of the PhD students and alumni supervised by Professor G. M. R. I. Godaliyadda, including their academic destinations,
      institutions and current professional affiliations.
    </p>
  </header>

  <section class="student-stats" aria-labelledby="student-stats-title">
    <div class="student-section-heading">
      <h2 id="student-stats-title">Summary Statistics</h2>
      <div class="student-section-divider" aria-hidden="true"></div>
    </div>
    <div class="student-stats__grid" id="student-stats-grid"></div>
  </section>

  <section class="student-analytics" aria-labelledby="student-analytics-title">
    <div class="student-section-heading">
      <h2 id="student-analytics-title">Analytics Overview</h2>
      <div class="student-section-divider" aria-hidden="true"></div>
    </div>

    <div class="student-analytics__grid">
      <article class="student-chart-card">
        <h3>Students by Country</h3>
        <div class="student-chart-card__canvas">
          <canvas id="students-by-country-chart" aria-label="Doughnut chart showing students by country"></canvas>
        </div>
        <div id="students-by-country-summary" class="student-chart-summary"></div>
      </article>

      <article class="student-chart-card">
        <h3>Students by Batch</h3>
        <div class="student-chart-card__canvas student-chart-card__canvas--tall">
          <canvas id="students-by-batch-chart" aria-label="Bar chart showing students by batch"></canvas>
        </div>
        <div id="students-by-batch-summary" class="student-chart-summary"></div>
      </article>

      <article class="student-chart-card student-chart-card--wide">
        <h3>Students by University</h3>
        <div class="student-chart-card__canvas student-chart-card__canvas--wide" id="students-by-university-canvas-wrap">
          <canvas id="students-by-university-chart" aria-label="Horizontal bar chart showing students by university"></canvas>
        </div>
        <div id="students-by-university-summary" class="student-chart-summary"></div>
      </article>

      <article class="student-chart-card" id="students-by-area-card">
        <h3>Students by Academic Area</h3>
        <div class="student-chart-card__canvas">
          <canvas id="students-by-area-chart" aria-label="Chart showing students by academic area"></canvas>
        </div>
        <div id="students-by-area-summary" class="student-chart-summary"></div>
      </article>
    </div>
  </section>

  <section class="student-filters" aria-labelledby="student-filters-title">
    <div class="student-section-heading">
      <h2 id="student-filters-title">Search and Filters</h2>
      <div class="student-section-divider" aria-hidden="true"></div>
    </div>

    <form id="student-filter-form" class="student-filter-form" action="#" novalidate>
      <div class="student-filter-form__field student-filter-form__field--search">
        <label for="student-search">Search by student name</label>
        <input id="student-search" name="student-search" type="search" autocomplete="off" />
      </div>

      <div class="student-filter-form__field">
        <label for="student-country-filter">Country</label>
        <select id="student-country-filter" name="student-country-filter">
          <option value="">All countries</option>
        </select>
      </div>

      <div class="student-filter-form__field">
        <label for="student-batch-filter">Batch</label>
        <select id="student-batch-filter" name="student-batch-filter">
          <option value="">All batches</option>
        </select>
      </div>

      <div class="student-filter-form__field">
        <label for="student-university-filter">University</label>
        <select id="student-university-filter" name="student-university-filter">
          <option value="">All universities</option>
        </select>
      </div>

      <div class="student-filter-form__field">
        <label for="student-area-filter">Academic area</label>
        <select id="student-area-filter" name="student-area-filter">
          <option value="">All academic areas</option>
        </select>
      </div>

      <div class="student-filter-form__actions">
        <button type="button" id="student-filters-reset">Clear filters</button>
      </div>
    </form>
  </section>

  <section class="student-directory" aria-labelledby="student-directory-heading">
    <div class="student-directory__toolbar">
      <h2 id="student-directory-heading">Student Directory</h2>
      <p id="student-result-count" class="student-directory__count" aria-live="polite"></p>
    </div>

    <div id="student-no-results" class="student-directory__empty" hidden>
      No students match the current search and filter settings.
    </div>

    <div id="student-directory-grid" class="student-directory__grid"></div>

    <noscript>
      <div class="student-directory__noscript">
        JavaScript is required for the interactive directory and analytics. The imported student data is available in
        `_data/students.yml`.
      </div>
    </noscript>
  </section>

</section>

<script id="students-data" type="application/json">{{ site.data.students | jsonify }}</script>
<script>
  window.studentDirectoryConfig = {
    imageBase: {{ "/assets/img/students/" | relative_url | jsonify }},
    placeholderImage: {{ "/assets/img/students/placeholder-person.svg" | relative_url | jsonify }}
  };
  window.studentDirectoryRecords = JSON.parse(document.getElementById("students-data").textContent);
</script>
<script>
  (function () {
    function batchKey(batch) {
      const match = String(batch || "").match(/^([A-Z]+)(\d+)(.*)$/i);
      if (!match) return ["ZZZ", Number.MAX_SAFE_INTEGER, ""];
      return [match[1].toUpperCase(), Number(match[2]), match[3] || ""];
    }

    function compareBatches(left, right) {
      const a = batchKey(left);
      const b = batchKey(right);
      if (a[0] !== b[0]) return a[0].localeCompare(b[0]);
      if (a[1] !== b[1]) return a[1] - b[1];
      return a[2].localeCompare(b[2]);
    }

    function countBy(values) {
      return values.reduce((accumulator, value) => {
        if (!value) return accumulator;
        accumulator[value] = (accumulator[value] || 0) + 1;
        return accumulator;
      }, {});
    }

    function getUniversities(record) {
      if (Array.isArray(record.universities) && record.universities.length) {
        return record.universities;
      }
      return record.university ? [record.university] : [];
    }

    function groupCounts(entries, limit, otherLabel) {
      if (entries.length <= limit) return entries;
      const kept = entries.slice(0, limit);
      const remaining = entries.slice(limit);
      const otherTotal = remaining.reduce((sum, entry) => sum + entry[1], 0);
      return kept.concat([[otherLabel, otherTotal]]);
    }

    function getThemeValue(name, fallback) {
      const value = getComputedStyle(document.querySelector(".student-directory-page")).getPropertyValue(name).trim();
      return value || fallback;
    }

    function buildPalette(count) {
      const palette = [
        getThemeValue("--student-accent", "#6e1f2a"),
        "#8a4a54",
        "#a96a74",
        "#c68e97",
        "#d6adb4",
        "#d9c6c1",
        "#b9b9b9",
        "#8a8a8a",
        "#666666",
        "#4d4d4d",
      ];
      return Array.from({ length: count }, (_, index) => palette[index % palette.length]);
    }

    function renderSummaryTable(containerId, entries, total, valueLabel) {
      const container = document.getElementById(containerId);
      if (!container) return;
      const table = document.createElement("table");
      table.innerHTML = `
        <thead>
          <tr>
            <th scope="col">Label</th>
            <th scope="col">${valueLabel}</th>
          </tr>
        </thead>
        <tbody></tbody>
      `;
      const tbody = table.querySelector("tbody");
      entries.forEach(([label, value]) => {
        const row = document.createElement("tr");
        const percent = total ? Math.round((value / total) * 1000) / 10 : 0;
        row.innerHTML = `<td>${label}</td><td>${value} (${percent}%)</td>`;
        tbody.appendChild(row);
      });
      container.innerHTML = "";
      container.appendChild(table);
    }

    function createChart(canvasId, configuration) {
      const canvas = document.getElementById(canvasId);
      if (!canvas || typeof Chart === "undefined") return null;
      return new Chart(canvas, configuration);
    }

    function normalizeText(value) {
      return String(value || "")
        .toLowerCase()
        .replace(/\s+/g, " ")
        .trim();
    }

    function populateSelect(select, values, sortFn) {
      const sortedValues = Array.from(values).sort(sortFn);
      sortedValues.forEach((value) => {
        const option = document.createElement("option");
        option.value = value;
        option.textContent = value;
        select.appendChild(option);
      });
    }

    function createMetaRow(label, value) {
      const row = document.createElement("p");
      row.className = "student-card__meta";
      row.innerHTML = '<span class="student-card__meta-label"></span>';
      row.querySelector("span").textContent = label + ": ";
      row.append(document.createTextNode(value));
      return row;
    }

    function renderCard(record, config) {
      const article = document.createElement("article");
      article.className = "student-card";

      const media = document.createElement("div");
      media.className = "student-card__media";

      const image = document.createElement("img");
      image.loading = "lazy";
      image.src = config.imageBase + record.image;
      image.alt = "Photograph of " + record.name;
      image.addEventListener(
        "error",
        function handleError() {
          image.removeEventListener("error", handleError);
          image.src = config.placeholderImage;
          image.alt = "Profile photograph not yet available for " + record.name;
        },
        { once: true }
      );
      media.appendChild(image);

      const content = document.createElement("div");
      content.className = "student-card__content";

      const name = document.createElement("h3");
      name.className = "student-card__name";
      name.textContent = record.name;
      content.appendChild(name);

      if (record.batch) content.appendChild(createMetaRow("Batch", record.batch));
      if (record.university) content.appendChild(createMetaRow("University", record.university));
      if (record.country) content.appendChild(createMetaRow("Country", record.country));

      if (record.academic_area) {
        const area = document.createElement("p");
        area.className = "student-card__area";
        area.innerHTML = '<span class="student-card__label">Academic area: </span>';
        area.append(document.createTextNode(record.academic_area));
        content.appendChild(area);
      }

      if (record.current_affiliation) {
        const affiliation = document.createElement("p");
        affiliation.className = "student-card__affiliation";
        affiliation.innerHTML = '<span class="student-card__label">Current affiliation: </span>';
        affiliation.append(document.createTextNode(record.current_affiliation));
        content.appendChild(affiliation);
      }

      if (record.profile_url) {
        const link = document.createElement("a");
        link.className = "student-directory__link";
        link.href = record.profile_url;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        link.setAttribute("aria-label", "Open profile for " + record.name + " in a new tab");
        link.innerHTML = '<i class="fa-solid fa-arrow-up-right-from-square" aria-hidden="true"></i><span>Profile</span>';
        content.appendChild(link);
      }

      article.appendChild(media);
      article.appendChild(content);
      return article;
    }

    function initPeopleDirectory() {
      const records = window.studentDirectoryRecords || [];
      const config = window.studentDirectoryConfig || {};
      if (!records.length) return;

      const totalStudents = records.length;
      const totalCountries = new Set(records.map((record) => record.country).filter(Boolean)).size;
      const totalUniversities = new Set(records.flatMap((record) => getUniversities(record)).filter(Boolean)).size;
      const totalBatches = new Set(records.map((record) => record.batch).filter(Boolean)).size;
      const statsGrid = document.getElementById("student-stats-grid");

      if (statsGrid) {
        [
          ["Total Students", totalStudents],
          ["Countries", totalCountries],
          ["Universities", totalUniversities],
          ["Batches", totalBatches],
        ].forEach(([label, value]) => {
          const item = document.createElement("article");
          item.className = "student-stat";
          item.innerHTML = `<p class="student-stat__label">${label}</p><p class="student-stat__value">${value}</p>`;
          statsGrid.appendChild(item);
        });
      }

      const gridColor = getThemeValue("--student-border", "rgba(0,0,0,0.12)");
      const textColor = getThemeValue("--student-muted-strong", "#3e3e3e");
      const reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      const sharedPlugins = {
        legend: {
          labels: {
            color: textColor,
            font: { size: 12 },
          },
        },
        tooltip: {
          callbacks: {
            label: function (context) {
              const data = context.dataset.data || [];
              const total = data.reduce((sum, value) => sum + value, 0);
              const parsed = typeof context.parsed === "object" ? context.parsed.x : context.parsed;
              const value = parsed || 0;
              const percent = total ? ((value / total) * 100).toFixed(1) : "0.0";
              return `${context.label}: ${value} (${percent}%)`;
            },
          },
        },
      };

      const countryEntries = groupCounts(
        Object.entries(countBy(records.map((record) => record.country))).sort((a, b) => b[1] - a[1]),
        6,
        "Other"
      );
      renderSummaryTable("students-by-country-summary", countryEntries, totalStudents, "Count");
      createChart("students-by-country-chart", {
        type: "doughnut",
        data: {
          labels: countryEntries.map(([label]) => label),
          datasets: [
            {
              data: countryEntries.map(([, value]) => value),
              backgroundColor: buildPalette(countryEntries.length),
              borderColor: getThemeValue("--student-surface", "#ffffff"),
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: reducedMotion ? false : { duration: 300 },
          plugins: sharedPlugins,
        },
      });

      const batchEntries = Object.entries(countBy(records.map((record) => record.batch))).sort((a, b) => compareBatches(a[0], b[0]));
      renderSummaryTable("students-by-batch-summary", batchEntries, totalStudents, "Count");
      createChart("students-by-batch-chart", {
        type: "bar",
        data: {
          labels: batchEntries.map(([label]) => label),
          datasets: [
            {
              label: "Students",
              data: batchEntries.map(([, value]) => value),
              backgroundColor: buildPalette(batchEntries.length),
              borderWidth: 0,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          animation: reducedMotion ? false : { duration: 300 },
          plugins: { ...sharedPlugins, legend: { display: false } },
          scales: {
            x: { ticks: { color: textColor }, grid: { color: gridColor } },
            y: {
              beginAtZero: true,
              ticks: { color: textColor, precision: 0 },
              grid: { color: gridColor },
            },
          },
        },
      });

      const universityEntries = groupCounts(
        Object.entries(countBy(records.flatMap((record) => getUniversities(record)))).sort((a, b) => b[1] - a[1]),
        10,
        "Other"
      );
      renderSummaryTable("students-by-university-summary", universityEntries, totalStudents, "Count");
      const universityWrap = document.getElementById("students-by-university-canvas-wrap");
      if (universityWrap) {
        universityWrap.style.minHeight = Math.max(320, universityEntries.length * 38) + "px";
      }
      createChart("students-by-university-chart", {
        type: "bar",
        data: {
          labels: universityEntries.map(([label]) => label),
          datasets: [
            {
              label: "Students",
              data: universityEntries.map(([, value]) => value),
              backgroundColor: buildPalette(universityEntries.length),
              borderWidth: 0,
            },
          ],
        },
        options: {
          indexAxis: "y",
          responsive: true,
          maintainAspectRatio: false,
          animation: reducedMotion ? false : { duration: 300 },
          plugins: { ...sharedPlugins, legend: { display: false } },
          scales: {
            x: {
              beginAtZero: true,
              ticks: { color: textColor, precision: 0 },
              grid: { color: gridColor },
            },
            y: { ticks: { color: textColor }, grid: { display: false } },
          },
        },
      });

      const areaValues = records.map((record) => record.academic_area).filter(Boolean);
      const areaCard = document.getElementById("students-by-area-card");
      if (areaValues.length >= Math.ceil(records.length * 0.7)) {
        const areaEntries = Object.entries(countBy(areaValues)).sort((a, b) => b[1] - a[1]);
        renderSummaryTable("students-by-area-summary", areaEntries, totalStudents, "Count");
        createChart("students-by-area-chart", {
          type: "bar",
          data: {
            labels: areaEntries.map(([label]) => label),
            datasets: [
              {
                label: "Students",
                data: areaEntries.map(([, value]) => value),
                backgroundColor: buildPalette(areaEntries.length),
                borderWidth: 0,
              },
            ],
          },
          options: {
            indexAxis: "y",
            responsive: true,
            maintainAspectRatio: false,
            animation: reducedMotion ? false : { duration: 300 },
            plugins: { ...sharedPlugins, legend: { display: false } },
            scales: {
              x: {
                beginAtZero: true,
                ticks: { color: textColor, precision: 0 },
                grid: { color: gridColor },
              },
              y: { ticks: { color: textColor }, grid: { display: false } },
            },
          },
        });
      } else if (areaCard) {
        areaCard.hidden = true;
      }

      const grid = document.getElementById("student-directory-grid");
      const noResults = document.getElementById("student-no-results");
      const resultCount = document.getElementById("student-result-count");
      const searchInput = document.getElementById("student-search");
      const countryFilter = document.getElementById("student-country-filter");
      const batchFilter = document.getElementById("student-batch-filter");
      const universityFilter = document.getElementById("student-university-filter");
      const areaFilter = document.getElementById("student-area-filter");
      const resetButton = document.getElementById("student-filters-reset");

      populateSelect(countryFilter, new Set(records.map((record) => record.country).filter(Boolean)));
      populateSelect(batchFilter, new Set(records.map((record) => record.batch).filter(Boolean)), compareBatches);
      populateSelect(
        universityFilter,
        new Set(records.flatMap((record) => getUniversities(record)).filter(Boolean)),
        (left, right) => left.localeCompare(right)
      );
      populateSelect(areaFilter, new Set(records.map((record) => record.academic_area).filter(Boolean)));

      function applyFilters() {
        const query = normalizeText(searchInput.value);
        const selectedCountry = countryFilter.value;
        const selectedBatch = batchFilter.value;
        const selectedUniversity = universityFilter.value;
        const selectedArea = areaFilter.value;

        const filtered = records
          .filter((record) => {
            if (query && !normalizeText(record.name).includes(query)) return false;
            if (selectedCountry && record.country !== selectedCountry) return false;
            if (selectedBatch && record.batch !== selectedBatch) return false;
            if (selectedUniversity && !getUniversities(record).includes(selectedUniversity)) return false;
            if (selectedArea && record.academic_area !== selectedArea) return false;
            return true;
          })
          .sort((left, right) => {
            const batchComparison = compareBatches(left.batch, right.batch);
            if (batchComparison !== 0) return batchComparison;
            return left.name.localeCompare(right.name);
          });

        grid.innerHTML = "";
        if (!filtered.length) {
          noResults.hidden = false;
        } else {
          noResults.hidden = true;
          filtered.forEach((record) => grid.appendChild(renderCard(record, config)));
        }
        resultCount.textContent = "Showing " + filtered.length + " of " + records.length + " students.";
      }

      [searchInput, countryFilter, batchFilter, universityFilter, areaFilter].forEach((element) => {
        element.addEventListener("input", applyFilters);
        element.addEventListener("change", applyFilters);
      });

      resetButton.addEventListener("click", function () {
        searchInput.value = "";
        countryFilter.value = "";
        batchFilter.value = "";
        universityFilter.value = "";
        areaFilter.value = "";
        applyFilters();
        searchInput.focus();
      });

      applyFilters();
    }

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", initPeopleDirectory);
    } else {
      initPeopleDirectory();
    }
  })();
</script>

<style>
  .student-directory-page {
    --student-accent: #6e1f2a;
    --student-accent-soft: rgba(110, 31, 42, 0.08);
    --student-accent-border: rgba(110, 31, 42, 0.18);
    --student-border: rgba(24, 24, 24, 0.12);
    --student-surface: rgba(255, 255, 255, 0.98);
    --student-muted: #5c5c5c;
    --student-muted-strong: #3e3e3e;
    --student-grid-gap: 1.25rem;
    display: grid;
    gap: 2rem;
  }

  .student-directory-page__header {
    max-width: 46rem;
  }

  .student-directory-page__eyebrow {
    margin: 0 0 0.4rem;
    font-size: 0.92rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--student-accent);
  }

  .student-directory-page__header h1 {
    margin-bottom: 0.75rem;
    font-size: clamp(2rem, 3vw, 2.5rem);
    font-weight: 600;
  }

  .student-directory-page__intro,
  .student-data-note p {
    max-width: 46rem;
    margin: 0;
    font-size: 1rem;
    line-height: 1.7;
    color: var(--student-muted-strong);
  }

  .student-section-heading h2,
  .student-directory__toolbar h2 {
    margin: 0;
    font-size: 1.08rem;
    font-weight: 600;
  }

  .student-section-divider {
    width: 100%;
    height: 1px;
    margin-top: 0.65rem;
    background: var(--student-border);
  }

  .student-stats__grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1rem;
  }

  .student-stat {
    padding: 0.9rem 0;
    border-top: 1px solid var(--student-border);
  }

  .student-stat__label {
    margin: 0 0 0.35rem;
    font-size: 0.88rem;
    color: var(--student-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .student-stat__value {
    margin: 0;
    font-size: 1.75rem;
    font-weight: 600;
    color: inherit;
  }

  .student-analytics__grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: var(--student-grid-gap);
  }

  .student-chart-card {
    border: 1px solid var(--student-border);
    border-radius: 8px;
    padding: 1rem;
    background: var(--student-surface);
  }

  .student-chart-card--wide {
    grid-column: 1 / -1;
  }

  .student-chart-card h3 {
    margin: 0 0 0.85rem;
    font-size: 0.98rem;
    font-weight: 600;
  }

  .student-chart-card__canvas {
    position: relative;
    min-height: 260px;
  }

  .student-chart-card__canvas--tall {
    min-height: 320px;
  }

  .student-chart-card__canvas--wide {
    min-height: 360px;
  }

  .student-chart-summary {
    margin-top: 1rem;
  }

  .student-chart-summary table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.92rem;
  }

  .student-chart-summary th,
  .student-chart-summary td {
    padding: 0.45rem 0;
    border-bottom: 1px solid var(--student-border);
    text-align: left;
    vertical-align: top;
  }

  .student-chart-summary th:last-child,
  .student-chart-summary td:last-child {
    text-align: right;
  }

  .student-filter-form {
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 1rem;
    align-items: end;
  }

  .student-filter-form__field {
    display: grid;
    gap: 0.45rem;
  }

  .student-filter-form__field--search {
    grid-column: span 3;
  }

  .student-filter-form__field:not(.student-filter-form__field--search) {
    grid-column: span 2;
  }

  .student-filter-form label {
    font-size: 0.9rem;
    font-weight: 500;
  }

  .student-filter-form input,
  .student-filter-form select,
  .student-filter-form button {
    width: 100%;
    min-height: 2.75rem;
    padding: 0.6rem 0.8rem;
    border: 1px solid var(--student-border);
    border-radius: 6px;
    background: transparent;
    color: inherit;
    font: inherit;
  }

  .student-filter-form button {
    cursor: pointer;
  }

  .student-filter-form__actions {
    grid-column: span 1;
  }

  .student-filter-form button:hover,
  .student-filter-form button:focus-visible,
  .student-filter-form input:focus-visible,
  .student-filter-form select:focus-visible,
  .student-directory__link:focus-visible {
    outline: 3px solid rgba(110, 31, 42, 0.22);
    outline-offset: 2px;
    border-color: var(--student-accent-border);
  }

  .student-directory__toolbar {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .student-directory__count {
    margin: 0;
    font-size: 0.94rem;
    color: var(--student-muted);
  }

  .student-directory__empty,
  .student-directory__noscript {
    padding: 1rem;
    border: 1px solid var(--student-border);
    border-radius: 8px;
    color: var(--student-muted-strong);
  }

  .student-directory__grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: var(--student-grid-gap);
  }

  .student-card {
    display: grid;
    grid-template-columns: 108px minmax(0, 1fr);
    gap: 1rem;
    padding: 1rem;
    border: 1px solid var(--student-border);
    border-radius: 8px;
    background: var(--student-surface);
  }

  .student-card__media {
    width: 108px;
    aspect-ratio: 1 / 1;
    border-radius: 8px;
    overflow: hidden;
    background: #f3f0ee;
  }

  .student-card__media img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .student-card__content {
    min-width: 0;
  }

  .student-card__name {
    margin: 0 0 0.35rem;
    font-size: 1rem;
    font-weight: 600;
  }

  .student-card__meta,
  .student-card__affiliation,
  .student-card__area {
    margin: 0.2rem 0 0;
    font-size: 0.93rem;
    line-height: 1.6;
    color: var(--student-muted-strong);
    overflow-wrap: anywhere;
  }

  .student-card__meta-label,
  .student-card__label {
    font-weight: 500;
    color: inherit;
  }

  .student-directory__link {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    margin-top: 0.55rem;
    color: inherit;
    font-size: 0.92rem;
    text-decoration: none;
  }

  .student-directory__link:hover {
    color: var(--student-accent);
    text-decoration: none;
  }

  .student-directory__link i {
    font-size: 0.95rem;
  }

  #students-by-area-card[hidden] {
    display: none;
  }

  @media (max-width: 1100px) {
    .student-filter-form {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .student-filter-form__field,
    .student-filter-form__field--search,
    .student-filter-form__actions {
      grid-column: auto;
    }
  }

  @media (max-width: 900px) {
    .student-stats__grid,
    .student-analytics__grid,
    .student-directory__grid {
      grid-template-columns: 1fr;
    }

    .student-chart-card--wide {
      grid-column: auto;
    }
  }

  @media (max-width: 640px) {
    .student-stats__grid,
    .student-filter-form {
      grid-template-columns: 1fr;
    }

    .student-directory__toolbar {
      flex-direction: column;
      align-items: flex-start;
    }

    .student-card {
      grid-template-columns: 1fr;
    }

    .student-card__media {
      width: 100%;
      max-width: 132px;
    }
  }

  html[data-theme="dark"] .student-directory-page,
  body[data-theme="dark"] .student-directory-page,
  html.dark .student-directory-page,
  body.dark .student-directory-page {
    --student-accent: #d69aa3;
    --student-accent-soft: rgba(214, 154, 163, 0.09);
    --student-accent-border: rgba(214, 154, 163, 0.26);
    --student-border: rgba(255, 255, 255, 0.14);
    --student-surface: rgba(255, 255, 255, 0.02);
    --student-muted: #c3c3c3;
    --student-muted-strong: #e0e0e0;
  }
</style>
