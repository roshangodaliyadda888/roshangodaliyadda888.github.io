---
layout: page
permalink: /publications/
title: Publications
description: High-impact publication audit aligned to the curated PDF structure.
nav: true
nav_order: 2
---

{% assign audit = site.data.high_impact_publications %}
{% assign journal_groups = audit.groups | where_exp: "group", "group.name != 'Tier-1 conference publication'" %}

<div class="impact-audit">
  <section class="impact-audit__hero" aria-labelledby="impact-audit-title">
    <p class="impact-audit__eyebrow">Publication Impact Screen</p>
    <h1 id="impact-audit-title">Q1 Journal and Tier-1 Conference Publications</h1>
    <p class="impact-audit__subtitle">
      A ranking-verified, deduplicated filter of the January 2026 long-form CV of Professor G. M. R. I.
      Godaliyadda.
    </p>
  </section>

  <section class="impact-audit__summary" aria-labelledby="impact-summary-title">
    <div class="impact-audit__heading">
      <h2 id="impact-summary-title">1. Audit Outcome and Screening Basis</h2>
      <div class="impact-audit__divider" aria-hidden="true"></div>
    </div>

    <div class="impact-audit__stats" role="list" aria-label="Audit summary statistics">
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">{{ audit.summary.q1_journals }}</p>
        <p class="impact-audit__stat-label">Q1 journal articles</p>
      </article>
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">{{ audit.summary.tier1_conferences }}</p>
        <p class="impact-audit__stat-label">Tier-1 conference paper</p>
      </article>
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">{{ audit.summary.distinct_q1_journals }}</p>
        <p class="impact-audit__stat-label">Distinct Q1 journals</p>
      </article>
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">{{ audit.summary.high_impact_fields }}</p>
        <p class="impact-audit__stat-label">High-impact fields</p>
      </article>
    </div>

    <div class="impact-audit__note">
      <p>
        This page mirrors the curated high-impact audit order: reverse-chronological within each field, limited to
        the screened Q1 journal set and the qualifying Tier-1 conference paper.
      </p>
    </div>
  </section>

  <section class="impact-audit__section" aria-labelledby="impact-q1-title">
    <div class="impact-audit__heading">
      <h2 id="impact-q1-title">2. Q1 Journal Publications</h2>
      <div class="impact-audit__divider" aria-hidden="true"></div>
    </div>

    {% for group in journal_groups %}
      <section class="impact-field" aria-labelledby="impact-field-{{ forloop.index }}">
        <h3 id="impact-field-{{ forloop.index }}">{{ group.name }} ({{ group.count }})</h3>

        <div class="impact-field__list">
          {% for item in group.items %}
            <article class="impact-item">
              <div class="impact-item__id">{{ item.id }}</div>
              <div class="impact-item__body">
                <p class="impact-item__year">{{ item.year }}</p>
                <h4>{{ item.title }}</h4>
                <p class="impact-item__authors">{{ item.authors_abbrev }}</p>
                <p class="impact-item__venue">{{ item.venue_line }}</p>
              </div>
            </article>
          {% endfor %}
        </div>
      </section>
    {% endfor %}
  </section>

  <section class="impact-audit__section" aria-labelledby="impact-tier1-title">
    <div class="impact-audit__heading">
      <h2 id="impact-tier1-title">3. Tier-1 Conference Publication</h2>
      <div class="impact-audit__divider" aria-hidden="true"></div>
    </div>

    <article class="impact-item impact-item--conference">
      <div class="impact-item__id">{{ audit.tier1.id }}</div>
      <div class="impact-item__body">
        <p class="impact-item__year">{{ audit.tier1.year }}</p>
        <h4>{{ audit.tier1.title }}</h4>
        <p class="impact-item__authors">{{ audit.tier1.authors_abbrev }}</p>
        <p class="impact-item__venue">{{ audit.tier1.venue_line }}</p>
      </div>
    </article>
  </section>
</div>

<style>
  .impact-audit {
    max-width: 60rem;
    margin: 0 auto;
  }

  .impact-audit__hero {
    margin-bottom: 2.5rem;
    padding-bottom: 1.25rem;
    border-bottom: 1px solid rgba(128, 128, 128, 0.16);
  }

  .impact-audit__eyebrow {
    margin: 0 0 0.45rem;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--global-theme-color);
  }

  .impact-audit__hero h1 {
    margin: 0;
    font-size: 2.15rem;
    line-height: 1.15;
    letter-spacing: -0.02em;
  }

  .impact-audit__subtitle {
    max-width: 46rem;
    margin: 1rem 0 0;
    font-size: 1rem;
    line-height: 1.8;
    color: var(--global-text-color);
    opacity: 0.92;
  }

  .impact-audit__section + .impact-audit__section,
  .impact-field + .impact-field {
    margin-top: 2.5rem;
  }

  .impact-audit__heading h2 {
    margin: 0;
    font-size: 1.14rem;
    font-weight: 600;
    letter-spacing: -0.01em;
  }

  .impact-audit__divider {
    width: 100%;
    height: 1px;
    margin-top: 0.75rem;
    background: rgba(128, 128, 128, 0.22);
  }

  .impact-audit__stats {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.1rem;
    margin-top: 1.4rem;
  }

  .impact-audit__stat {
    padding: 1rem 1rem 0.95rem;
    border: 1px solid rgba(128, 128, 128, 0.16);
    border-radius: 10px;
    background: rgba(128, 128, 128, 0.03);
  }

  .impact-audit__stat-value {
    margin: 0;
    font-size: 1.7rem;
    font-weight: 600;
    line-height: 1.1;
  }

  .impact-audit__stat-label,
  .impact-audit__note p,
  .impact-item__authors,
  .impact-item__venue,
  .impact-item__year {
    margin: 0;
    line-height: 1.7;
    color: var(--global-text-color);
  }

  .impact-audit__note {
    max-width: 48rem;
    margin-top: 1.15rem;
    margin-bottom: 1.75rem;
  }

  .impact-field h3 {
    display: inline-flex;
    align-items: center;
    margin: 0.65rem 0 0.95rem;
    padding-left: 0.8rem;
    position: relative;
    font-size: 1.02rem;
    font-weight: 600;
    line-height: 1.45;
  }

  .impact-field h3::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.2rem;
    bottom: 0.2rem;
    width: 3px;
    border-radius: 999px;
    background: var(--global-theme-color);
  }

  .impact-field__list {
    display: grid;
    gap: 0;
    padding: 0.2rem 1.1rem 0.15rem;
    border: 1px solid rgba(128, 128, 128, 0.14);
    border-radius: 12px;
    background: rgba(128, 128, 128, 0.025);
  }

  .impact-item {
    display: grid;
    grid-template-columns: 4.5rem minmax(0, 1fr);
    gap: 1.15rem;
    padding: 1rem 0;
    border-bottom: 1px solid rgba(128, 128, 128, 0.14);
  }

  .impact-field__list .impact-item:first-child,
  .impact-audit__section > .impact-item {
    border-top: 1px solid rgba(128, 128, 128, 0.14);
  }

  .impact-item__id {
    padding-top: 0.1rem;
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--global-theme-color);
    letter-spacing: 0.04em;
  }

  .impact-item__year {
    font-size: 0.92rem;
    opacity: 0.8;
  }

  .impact-item h4 {
    max-width: 48rem;
    margin: 0.18rem 0 0.4rem;
    font-size: 1.03rem;
    font-weight: 500;
    line-height: 1.5;
    letter-spacing: -0.01em;
  }

  .impact-item__authors {
    margin-top: 0.1rem;
  }

  .impact-item__venue {
    margin-top: 0.05rem;
    opacity: 0.88;
  }

  .impact-item:hover h4 {
    color: var(--global-theme-color);
  }

  html[data-theme="dark"] .impact-audit__hero,
  body[data-theme="dark"] .impact-audit__hero,
  html.dark .impact-audit__hero,
  body.dark .impact-audit__hero {
    border-bottom-color: rgba(255, 255, 255, 0.12);
  }

  html[data-theme="dark"] .impact-audit__stat,
  body[data-theme="dark"] .impact-audit__stat,
  html.dark .impact-audit__stat,
  body.dark .impact-audit__stat {
    border-color: rgba(255, 255, 255, 0.12);
    background: rgba(255, 255, 255, 0.03);
  }

  html[data-theme="dark"] .impact-field__list,
  body[data-theme="dark"] .impact-field__list,
  html.dark .impact-field__list,
  body.dark .impact-field__list {
    border-color: rgba(255, 255, 255, 0.12);
    background: rgba(255, 255, 255, 0.02);
  }

  @media (max-width: 900px) {
    .impact-audit__stats {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 640px) {
    .impact-audit__stats,
    .impact-item {
      grid-template-columns: 1fr;
    }

    .impact-audit__hero {
      margin-bottom: 2rem;
      padding-bottom: 1rem;
    }

    .impact-audit__hero h1 {
      font-size: 1.8rem;
    }

    .impact-item {
      gap: 0.45rem;
      padding: 0.9rem 0;
    }
  }
</style>
