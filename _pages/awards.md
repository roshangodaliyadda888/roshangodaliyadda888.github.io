---
layout: page
permalink: /awards/
title: Awards & Grants
nav_title: awards
description: Awards, recognitions, and funded research activity.
nav: true
nav_order: 5
---

{% assign awards = site.data.awards_grants.awards %}
{% assign grants = site.data.awards_grants.grants %}

<div class="awards-grants-page">
  <p class="section-intro">
    Prof. Roshan Godaliyadda’s remarkable academic journey is defined by a continuous commitment to research excellence. This section highlights his prestigious accolades, including multiple President's Awards and international Best Paper honors, alongside significant research grants secured from prominent organizations like the NSF and IDRC.
  </p>

  <nav class="section-links" aria-label="Awards and grants sections">
    <a href="#awards-heading">Awards</a>
    <a href="#grants-heading">Grants</a>
  </nav>

  <section class="awards-grants-section" aria-labelledby="awards-heading">
    <h2 id="awards-heading">Awards</h2>
    <div class="section-rule"></div>
    <div class="entry-list" role="list">
      {% for award in awards %}
        <article class="entry-row" role="listitem">
          <div class="entry-year">{{ award.year }}</div>
          <div class="entry-body">
            <h3>{{ award.title }}</h3>
            <p class="entry-meta">
              {% if award.organization != blank %}{{ award.organization }}{% else %}Organization not specified in source{% endif %}
              {% if award.category != blank %}<span class="meta-separator">•</span>{{ award.category }}{% endif %}
            </p>
            {% if award.notes != blank %}
              <p class="entry-notes">{{ award.notes }}</p>
            {% endif %}
            {% if award.citations %}
              <ul class="award-citations">
                {% for citation in award.citations %}
                  <li>{{ citation }}</li>
                {% endfor %}
              </ul>
            {% endif %}
          </div>
        </article>
      {% endfor %}
    </div>
  </section>

  <section class="awards-grants-section" aria-labelledby="grants-heading">
    <h2 id="grants-heading">Research Grants</h2>
    <div class="section-rule"></div>
    <div class="entry-list" role="list">
      {% for grant in grants %}
        <article class="entry-row grant-row" role="listitem">
          <div class="entry-body">
            <h3>{{ grant.title }}</h3>
            <p class="entry-meta">
              {{ grant.funding_organization }}
              {% if grant.grant_number != blank %}<span class="meta-separator">•</span>Grant No. {{ grant.grant_number }}{% endif %}
            </p>
            <p class="grant-details">
              <span>{{ grant.role }}</span>
              {% if grant.funding_period != blank %}<span class="meta-separator">•</span><span>{{ grant.funding_period }}</span>{% endif %}
              {% if grant.amount != blank %}<span class="meta-separator">•</span><span>{% if grant.currency != blank %}{{ grant.currency }} {% endif %}{{ grant.amount }}</span>{% endif %}
              {% if grant.status != blank %}<span class="meta-separator">•</span><span>{{ grant.status }}</span>{% endif %}
            </p>
            {% if grant.notes != blank %}
              <p class="entry-notes">{{ grant.notes }}</p>
            {% endif %}
          </div>
        </article>
      {% endfor %}
    </div>
  </section>
</div>

<style>
  .awards-grants-page {
    max-width: 54rem;
  }

  .awards-grants-page .section-intro {
    margin-bottom: 1rem;
    color: var(--global-text-color);
    line-height: 1.75;
  }

  .awards-grants-page .section-links {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 2rem;
  }

  .awards-grants-page .section-links a {
    color: var(--global-text-color);
    text-decoration: none;
    border-bottom: 1px solid rgba(128, 128, 128, 0.35);
    padding-bottom: 0.1rem;
  }

  .awards-grants-page .section-links a:hover,
  .awards-grants-page .section-links a:focus-visible {
    color: var(--global-theme-color);
    border-bottom-color: var(--global-theme-color);
  }

  .awards-grants-page .awards-grants-section + .awards-grants-section {
    margin-top: 2.5rem;
  }

  .awards-grants-page h2 {
    margin-bottom: 0.5rem;
  }

  .awards-grants-page .section-rule {
    height: 1px;
    margin-bottom: 0.75rem;
    background: rgba(128, 128, 128, 0.28);
  }

  .awards-grants-page .entry-list {
    border-top: 1px solid rgba(128, 128, 128, 0.18);
  }

  .awards-grants-page .entry-row {
    display: grid;
    grid-template-columns: 5.5rem minmax(0, 1fr);
    gap: 1.25rem;
    padding: 1rem 0;
    border-bottom: 1px solid rgba(128, 128, 128, 0.18);
  }

  .awards-grants-page .grant-row {
    grid-template-columns: minmax(0, 1fr);
  }

  .awards-grants-page .entry-year {
    color: var(--global-theme-color);
    font-weight: 600;
    letter-spacing: 0.01em;
  }

  .awards-grants-page .entry-body h3 {
    margin: 0 0 0.35rem;
    font-size: 1.08rem;
    font-weight: 600;
    line-height: 1.45;
  }

  .awards-grants-page .entry-meta,
  .awards-grants-page .grant-details,
  .awards-grants-page .entry-notes {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.7;
    color: var(--global-text-color);
  }

  .awards-grants-page .entry-notes {
    margin-top: 0.25rem;
    opacity: 0.82;
  }

  .awards-grants-page .award-citations {
    margin: 0.6rem 0 0;
    padding-left: 1.15rem;
  }

  .awards-grants-page .award-citations li {
    margin: 0.35rem 0;
    line-height: 1.65;
    color: var(--global-text-color);
  }

  .awards-grants-page .meta-separator {
    display: inline-block;
    margin: 0 0.55rem;
    opacity: 0.6;
  }

  @media (max-width: 700px) {
    .awards-grants-page .entry-row {
      grid-template-columns: minmax(0, 1fr);
      gap: 0.45rem;
    }

    .awards-grants-page .entry-year {
      font-size: 0.95rem;
    }
  }
</style>
