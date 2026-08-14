---
layout: page
title: News
permalink: /news/
description: Highlights, workshops, and recent paper acceptances from Professor G. M. R. I. Godaliyadda’s research group.
nav: true
nav_order: 2
---

{% assign spotlight_image = '/assets/img/news/756846618_10164767004669533_2330629612247282933_n.jpg' %}
{% assign workshop_image = '/assets/img/news/WhatsApp Image 2026-08-03 at 6.57.19 PM (1).JPG' %}
{% assign paper_image = '/assets/img/news/684204995_122214122228553732_159175010113833264_n.jpg' %}
{% assign spotlight_asset = site.static_files | where: "path", spotlight_image | first %}
{% assign workshop_asset = site.static_files | where: "path", workshop_image | first %}
{% assign paper_asset = site.static_files | where: "path", paper_image | first %}

<div class="news-page">
  <p class="news-page__intro">
    Recent highlights from Professor G. M. R. I. Godaliyadda’s research group, including major student achievements,
    academic outreach, and new publication milestones.
  </p>

  <section class="news-group" aria-labelledby="spotlight-heading">
    <div class="news-group__header">
      <h2 id="spotlight-heading"><strong>In the Spotlight</strong></h2>
      <div class="news-group__rule" aria-hidden="true"></div>
    </div>
    <article class="news-feature news-feature--spotlight">
      {% if spotlight_asset %}
        <div class="news-feature__media news-feature__media--image">
          <img src="{{ spotlight_image | relative_url }}" alt="Global placements for the Fall 2026 PhD cohort" loading="lazy">
        </div>
      {% else %}
        <div class="news-feature__media news-feature__media--fallback" aria-label="Spotlight image placeholder">
          <div class="news-feature__fallback-label">Spotlight</div>
        </div>
      {% endif %}
      <div class="news-feature__content">
        <h3>Celebrating Global Placements for the Fall 2026 PhD Cohort</h3>
        <p>
          We are thrilled to announce the remarkable achievements of our Fall 2026 PhD cohort. This year,
          fourteen dedicated researchers from Prof. Godaliyadda&apos;s research group are embarking on their
          postgraduate journeys at top-tier global universities across the United States, Canada, and Australia.
        </p>
        <p>
          Accompanied by prestigious scholarships, these talented scholars will pursue advanced doctoral degrees
          in highly competitive programs, including Electrical and Computer Engineering, Computer Science, and
          Mechanical Engineering. These placements are a direct result of years of perseverance, collaborative
          inquiry, and high-impact scholarship cultivated within the research group.
        </p>
        <p>
          As these fourteen innovators transition into exciting new chapters worldwide, they proudly carry forward
          the research group&apos;s enduring spirit of excellence, deep curiosity, and global discovery.
        </p>
      </div>
    </article>
  </section>

  <section class="news-group" aria-labelledby="workshops-heading">
    <div class="news-group__header">
      <h2 id="workshops-heading"><strong>Workshops</strong></h2>
      <div class="news-group__rule" aria-hidden="true"></div>
    </div>
    <article class="news-feature">
      {% if workshop_asset %}
        <div class="news-feature__media news-feature__media--image">
          <img src="{{ workshop_image | relative_url }}" alt="AI workshop conducted for Sri Lanka Army Special Forces" loading="lazy">
        </div>
      {% else %}
        <div class="news-feature__media news-feature__media--fallback" aria-label="Workshop image placeholder">
          <div class="news-feature__fallback-label">Workshop</div>
        </div>
      {% endif %}
      <div class="news-feature__content">
        <h3>Exclusive AI Workshop Conducted for Sri Lanka Army Special Forces</h3>
        <p>
          On July 30th, the Multidisciplinary AI Research Centre (MARC) at the University of Peradeniya conducted
          an exclusive workshop on Artificial Intelligence and its practical implementations for the Sri Lanka Army
          Special Forces.
        </p>
        <p>
          The highly engaging session took place at the Special Forces Regimental Headquarters in Naula. Organized
          under the leadership of Major General Kanchana Weerasekara, the workshop was designed to share cutting-edge
          AI knowledge and explore strategic, real-world applications with the elite military unit.
        </p>
        <p>
          The event fostered dynamic discussions, reflecting the Special Forces&apos; commitment to continuous excellence
          and technological modernization. Prof. Roshan Godaliyadda along with an expert team from the MARC conducted
          a dedicated session to share his expertise on practical AI integration.
        </p>
      </div>
    </article>
  </section>

  <section class="news-group" aria-labelledby="papers-heading">
    <div class="news-group__header">
      <h2 id="papers-heading"><strong>Paper Acceptances</strong></h2>
      <div class="news-group__rule" aria-hidden="true"></div>
    </div>
    <article class="news-feature">
      {% if paper_asset %}
        <div class="news-feature__media news-feature__media--image">
          <img src="{{ paper_image | relative_url }}" alt="Paper acceptance on hyperspectral scale correction in IEEE JSTARS" loading="lazy">
        </div>
      {% else %}
        <div class="news-feature__media news-feature__media--fallback" aria-label="Paper acceptance image placeholder">
          <div class="news-feature__fallback-label">Publication</div>
        </div>
      {% endif %}
      <div class="news-feature__content">
        <h3>Groundbreaking Q1 Publication: Solving Hyperspectral Scale Distortions with Geometry</h3>
        <p>
          We are thrilled to announce a major paper acceptance in IEEE JSTARS (Q1, SCIE; Impact Factor: 5.3)
          from Prof. Roshan Godaliyadda&apos;s research group at the Multidisciplinary AI Research Centre (MARC),
          University of Peradeniya.
        </p>
        <p>
          The publication, <em>Preprocessing Algorithm Leveraging Geometric Modeling for Scale Correction in
          Hyperspectral Images for Improved Unmixing Performance</em>, addresses a critical bottleneck in remote
          sensing. Under the expert guidance of Prof. Godaliyadda, alongside co-supervisors Prof. Parakrama
          Ekanayake and Prof. Vijitha Herath, the research team developed an innovative unsupervised preprocessing
          algorithm.
        </p>
        <p>
          Rather than relying on computationally heavy neural networks to handle noise from natural illumination
          variations, this method utilizes a rigorous mathematical framework to restore foundational data geometry.
          This breakthrough acts as a corrective lens, reducing abundance estimation errors by approximately 50%
          across state-of-the-art algorithms. Congratulations to undergraduate researchers Praveen Sumanasekara,
          Athulya Rathnayake, Buddhi Wijenayake, and alumni collaborator Keshawa Lasith for driving this exceptional,
          mathematically grounded AI research.
        </p>
      </div>
    </article>
  </section>
</div>

<style>
  .news-page {
    max-width: 60rem;
  }

  .news-page__intro {
    margin-bottom: 2rem;
    line-height: 1.75;
    text-align: justify;
  }

  .news-group + .news-group {
    margin-top: 2.75rem;
  }

  .news-group__header h2 {
    margin-bottom: 0.45rem;
    font-weight: 700;
  }

  .news-group__rule {
    height: 1px;
    margin-bottom: 1rem;
    background: rgba(128, 128, 128, 0.24);
  }

  .news-feature {
    display: grid;
    grid-template-columns: minmax(15rem, 19rem) minmax(0, 1fr);
    gap: 1.5rem;
    align-items: start;
  }

  .news-feature__media {
    aspect-ratio: 4 / 3;
    width: 100%;
    overflow: hidden;
    border: 1px solid rgba(128, 128, 128, 0.18);
    background: rgba(128, 128, 128, 0.04);
  }

  .news-feature__media--image {
    aspect-ratio: auto;
    overflow: visible;
  }

  .news-feature__media img {
    width: 100%;
    height: auto;
    object-fit: contain;
    object-position: center;
    display: block;
  }

  .news-feature__media--fallback {
    display: flex;
    align-items: center;
    justify-content: center;
    background:
      linear-gradient(135deg, rgba(128, 0, 0, 0.1), rgba(128, 128, 128, 0.08)),
      rgba(128, 128, 128, 0.06);
  }

  .news-feature__fallback-label {
    padding: 0.5rem 0.85rem;
    border: 1px solid rgba(128, 128, 128, 0.22);
    font-size: 0.9rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }

  .news-feature__content h3 {
    margin: 0 0 0.75rem;
    font-size: 1.2rem;
    line-height: 1.45;
    font-weight: 700;
    color: #000;
  }

  .news-feature__content p {
    margin: 0 0 0.95rem;
    line-height: 1.75;
    text-align: justify;
  }

  .news-feature__content p:last-child {
    margin-bottom: 0;
  }

  @media (max-width: 860px) {
    .news-page {
      max-width: 100%;
    }

    .news-page__intro {
      margin-bottom: 1.5rem;
    }

    .news-group + .news-group {
      margin-top: 2rem;
    }

    .news-feature {
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    .news-feature__media {
      max-width: 100%;
    }

    .news-feature__content h3 {
      font-size: 1.08rem;
    }
  }

  html[data-theme="dark"] .news-feature__content h3,
  body[data-theme="dark"] .news-feature__content h3,
  html.dark .news-feature__content h3,
  body.dark .news-feature__content h3 {
    color: #fff;
  }
</style>
