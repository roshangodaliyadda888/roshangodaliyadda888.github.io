---
layout: about
title: About
permalink: /
subtitle: Professor, Department of Electrical and Electronic Engineering, University of Peradeniya, Sri Lanka

profile:
  align: right
  image: roshan-godaliyadda.jpg
  image_alt: Professor G. M. R. I. Godaliyadda
  image_circular: false # crops the image to make it circular
  more_info: >
    <div class="professor-sidebar" aria-label="Academic information">
      <p class="professor-sidebar__eyebrow">Professor</p>
      <p class="professor-sidebar__org">Department of Electrical and Electronic Engineering</p>
      <p class="professor-sidebar__org">University of Peradeniya, Sri Lanka</p>
      <div class="professor-sidebar__divider"></div>
      <p class="professor-sidebar__eyebrow">Deputy Director - Research &amp; Innovation</p>
      <p class="professor-sidebar__org">Multidisciplinary AI Research Centre [MARC], University of Peradeniya</p>
      <div class="professor-sidebar__contacts">
        <a href="tel:+94777709035" aria-label="Call Professor G. M. R. I. Godaliyadda at +94 77 770 9035"><span aria-hidden="true">&#9742;</span><span>+94 77 770 9035</span></a>
        <a href="mailto:roshangod@ee.pdn.ac.lk" aria-label="Email roshangod@ee.pdn.ac.lk"><span aria-hidden="true">&#9993;</span><span>roshangod@ee.pdn.ac.lk</span></a>
        <a href="mailto:roshang@eng.pdn.ac.lk" aria-label="Email roshang@eng.pdn.ac.lk"><span aria-hidden="true">&#9993;</span><span>roshang@eng.pdn.ac.lk</span></a>
      </div>
    </div>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: false # custom profile links are rendered in the page body

announcements:
  enabled: false # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<section class="professor-homepage" aria-labelledby="biography-heading">
  <h2 id="biography-heading" class="visually-hidden">Biography</h2>

  <p>G M Roshan Indika Godaliyadda is a Professor in the Department of Electrical and Electronic Engineering at the University of Peradeniya, Sri Lanka. He also serves as Deputy Director - Research &amp; Innovation at the Multidisciplinary AI Research Centre [MARC], University of Peradeniya.</p>

  <p>His research spans signal and image processing, computer vision, machine learning, generative AI, hyperspectral and multispectral imaging, remote sensing, smart grids, renewable-energy integration, biomedical signal processing, wearable sensing, human-motion analysis, computational epidemiology, and AI for social sciences.</p>

  <p>After completing his BSc Engineering Degree in Electrical and Electronic Engineering with first class honours from the University of Peradeniya, he obtained his PhD in Electrical and Computer Engineering from the National University of Singapore. His academic contributions include publications, doctoral supervision, research leadership, and academic program development.</p>
</section>

<section class="professor-homepage__section" aria-labelledby="interests-heading">
  <h2 id="interests-heading">Research Areas</h2>
  <div class="professor-section-divider" aria-hidden="true"></div>
  <ul class="professor-areas" aria-label="Research areas">
    <li>Signal and Image Processing</li>
    <li>Machine Learning</li>
    <li>Computer Vision</li>
    <li>Hyperspectral Imaging</li>
    <li>Remote Sensing</li>
    <li>Smart Grids</li>
    <li>Biomedical Signal Processing</li>
    <li>Generative AI</li>
  </ul>
</section>

<section class="professor-homepage__section" aria-labelledby="profiles-heading">
  <h2 id="profiles-heading">Academic Links</h2>
  <div class="professor-section-divider" aria-hidden="true"></div>
  <div class="professor-links" role="list" aria-label="Academic links">
    {% if site.data.socials.linkedin_url and site.data.socials.linkedin_url != "" %}
      <a class="professor-link" role="listitem" href="{{ site.data.socials.linkedin_url }}" target="_blank" rel="noopener noreferrer" aria-label="Open LinkedIn profile in a new tab" title="LinkedIn">
        <i class="fa-brands fa-linkedin-in" aria-hidden="true"></i>
        <span>LinkedIn</span>
      </a>
    {% endif %}
    {% if site.data.socials.scholar_userid and site.data.socials.scholar_userid != "" %}
      <a class="professor-link" role="listitem" href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}" target="_blank" rel="noopener noreferrer" aria-label="Open Google Scholar profile in a new tab" title="Google Scholar">
        <i class="ai ai-google-scholar" aria-hidden="true"></i>
        <span>Google Scholar</span>
      </a>
    {% endif %}
    {% if site.data.socials.university_profile_url and site.data.socials.university_profile_url != "" %}
      <a class="professor-link" role="listitem" href="{{ site.data.socials.university_profile_url }}" target="_blank" rel="noopener noreferrer" aria-label="Open University of Peradeniya profile in a new tab" title="University Profile">
        <i class="fa-solid fa-building-columns" aria-hidden="true"></i>
        <span>University Profile</span>
      </a>
    {% endif %}
  </div>
</section>

<style>
  .professor-homepage,
  .professor-homepage__section {
    --professor-accent: #6e1f2a;
    --professor-accent-strong: #54141d;
    --professor-accent-soft: rgba(110, 31, 42, 0.08);
    --professor-border: rgba(110, 31, 42, 0.18);
    --professor-text-soft: #4c4c4c;
  }

  .post-title,
  .post-title .font-weight-bold,
  .post-title .font-weight-bolder,
  .post-title strong,
  .post-title b {
    font-weight: 400 !important;
  }

  .professor-homepage {
    max-width: 42rem;
    margin: 0;
    line-height: 1.7;
    color: inherit;
  }

  .professor-homepage p {
    margin: 0 0 1rem;
    font-size: 0.99rem;
  }

  .professor-homepage__section {
    margin-top: 1.6rem;
    max-width: 42rem;
  }

  .professor-homepage__section h2 {
    margin-bottom: 0.55rem;
    font-size: 1.02rem;
    font-weight: 700;
    color: var(--professor-accent-strong);
  }

  .professor-section-divider {
    width: 100%;
    height: 1px;
    margin: 0 0 0.9rem;
    background: rgba(0, 0, 0, 0.1);
  }

  .professor-areas {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0 1.75rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .professor-areas li {
    position: relative;
    margin: 0;
    padding: 0.68rem 0 0.68rem 0.9rem;
    border-bottom: 1px solid rgba(0, 0, 0, 0.08);
    font-size: 0.95rem;
    line-height: 1.65;
    color: inherit;
  }

  .professor-areas li::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.88rem;
    width: 2px;
    height: calc(100% - 1.76rem);
    min-height: 0.8rem;
    background: var(--professor-accent);
    opacity: 0.8;
  }

  .professor-links {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.45rem 0;
    color: inherit;
  }

  .professor-link {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0;
    color: inherit;
    font-size: 0.93rem;
    font-weight: 400;
    line-height: 1.25;
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .professor-link:not(:last-child)::after {
    content: "·";
    margin: 0 0.8rem;
    color: rgba(0, 0, 0, 0.35);
  }

  .professor-link:hover,
  .professor-link:focus-visible {
    color: var(--professor-accent-strong);
    text-decoration: none;
  }

  .professor-link i {
    font-size: 1rem;
    width: 1rem;
    text-align: center;
  }

  .professor-link:focus-visible,
  .professor-sidebar__contacts a:focus-visible {
    outline: 3px solid rgba(110, 31, 42, 0.22);
    outline-offset: 2px;
  }

  .professor-sidebar {
    margin-top: 1rem;
    padding: 1rem 1.1rem;
    border: 1px solid rgba(110, 31, 42, 0.12);
    border-radius: 1rem;
    background: rgba(110, 31, 42, 0.03);
    box-shadow: 0 10px 24px rgba(33, 18, 21, 0.06);
    font-family: inherit;
  }

  .professor-sidebar__eyebrow {
    margin: 0 0 0.35rem;
    color: var(--professor-accent-strong);
    font-size: 0.94rem;
    font-weight: 700;
  }

  .professor-sidebar__org {
    margin: 0;
    color: var(--professor-text-soft);
    font-size: 0.93rem;
    line-height: 1.55;
  }

  .professor-sidebar__divider {
    width: 100%;
    height: 1px;
    margin: 0.85rem 0;
    background: rgba(110, 31, 42, 0.12);
  }

  .professor-sidebar__contacts {
    display: grid;
    gap: 0.55rem;
    margin-top: 0.9rem;
  }

  .professor-sidebar__contacts a {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    color: inherit;
    font-size: 0.92rem;
    line-height: 1.45;
    text-decoration: none;
  }

  .professor-sidebar__contacts a:hover {
    color: var(--professor-accent);
    text-decoration: none;
  }

  .professor-sidebar__contacts span[aria-hidden="true"] {
    width: 1rem;
    text-align: center;
    color: var(--professor-accent);
    font-size: 0.92rem;
  }

  .profile img {
    width: 100%;
    max-width: 320px;
    aspect-ratio: 4 / 5;
    object-fit: cover;
    display: block;
    margin: 0 auto;
    border-radius: 1rem;
    box-shadow: 0 14px 28px rgba(33, 18, 21, 0.12);
  }

  .profile .more-info {
    font-family: inherit;
  }

  .visually-hidden {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }

  html[data-theme="dark"] .professor-homepage,
  html[data-theme="dark"] .professor-homepage__section,
  body[data-theme="dark"] .professor-homepage,
  body[data-theme="dark"] .professor-homepage__section,
  html.dark .professor-homepage,
  html.dark .professor-homepage__section,
  body.dark .professor-homepage,
  body.dark .professor-homepage__section {
    --professor-accent: #c97b86;
    --professor-accent-strong: #f0c7ce;
    --professor-accent-soft: rgba(201, 123, 134, 0.12);
    --professor-border: rgba(201, 123, 134, 0.22);
    --professor-text-soft: #d5d5d5;
  }

  html[data-theme="dark"] .professor-sidebar,
  body[data-theme="dark"] .professor-sidebar,
  html.dark .professor-sidebar,
  body.dark .professor-sidebar {
    background: rgba(201, 123, 134, 0.08);
    box-shadow: none;
  }

  html[data-theme="dark"] .professor-section-divider,
  body[data-theme="dark"] .professor-section-divider,
  html.dark .professor-section-divider,
  body.dark .professor-section-divider,
  html[data-theme="dark"] .professor-areas li,
  body[data-theme="dark"] .professor-areas li,
  html.dark .professor-areas li,
  body.dark .professor-areas li {
    border-color: rgba(255, 255, 255, 0.12);
    background: transparent;
  }

  html[data-theme="dark"] .professor-link:not(:last-child)::after,
  body[data-theme="dark"] .professor-link:not(:last-child)::after,
  html.dark .professor-link:not(:last-child)::after,
  body.dark .professor-link:not(:last-child)::after {
    color: rgba(255, 255, 255, 0.35);
  }

  @media (max-width: 768px) {
    .professor-homepage,
    .professor-homepage__section {
      max-width: 100%;
    }

    .post .profile {
      width: 100%;
      margin: 0 0 1.25rem;
      float: none;
    }

    .post .clearfix {
      display: block;
    }

    .professor-homepage p {
      font-size: 0.97rem;
    }

    .profile img {
      max-width: 100%;
      aspect-ratio: auto;
    }

    .professor-areas {
      grid-template-columns: 1fr;
      gap: 0;
    }

    .professor-link {
      font-size: 0.9rem;
    }

    .professor-link:not(:last-child)::after {
      margin: 0 0.6rem;
    }

    .professor-sidebar {
      padding: 0.95rem 1rem;
      border-radius: 0.85rem;
    }

    .professor-sidebar__contacts a {
      align-items: flex-start;
      word-break: break-word;
    }
  }
</style>

