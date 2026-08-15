---
layout: page
title: Projects
permalink: /projects/
description:
nav: true
nav_order: 3
display_categories: ["Generative AI (GenAI)", "AI for Remote Sensing & GIS", "AI for Sociology, Humanities & Socio-economics", "Biomedical Engineering & Bio-imaging", "Computer Vision (CV)", "Wearable Technology", "Agrivoltaics & Plant Growth", "Light-based Communications", "Renewable Energy & Smart Grid", "Multispectral Imaging (MSI)"]
---

<link rel="stylesheet" href="{{ '/assets/css/projects-page.css' | relative_url }}">

<div class="projects">
  <p class="projects-page-intro">
    Selected funded research projects and major multidisciplinary research initiatives led or co-led by Professor G. M. R. I. Godaliyadda.
    The projects span generative AI, remote sensing and GIS, sociology and socio-economics, biomedical engineering and bio-imaging, computer vision, wearable technology, agrivoltaics and plant growth, light-based communications, renewable energy and smart-grid systems, and multispectral imaging.
  </p>
  <section class="projects-highlight-ribbon" aria-label="Research highlight carousel">
    <div class="projects-highlight-ribbon__viewport">
      <div class="projects-highlight-ribbon__track">
        <figure class="projects-highlight-ribbon__slide">
          <img src="{{ '/assets/img/projects/carousel/01-generative-ai-genai.webp' | relative_url }}" alt="Generative AI research highlight" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide">
          <img src="{{ '/assets/img/projects/carousel/02-ai-for-socio-economics-public-health.webp' | relative_url }}" alt="AI for socio-economics and public health research highlight" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide">
          <img src="{{ '/assets/img/projects/carousel/03-agrivoltaics-plant-modeling.webp' | relative_url }}" alt="Agrivoltaics and plant modeling research highlight" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide">
          <img src="{{ '/assets/img/projects/carousel/04-gis-remote-sensing.webp' | relative_url }}" alt="GIS and remote sensing research highlight" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide">
          <img src="{{ '/assets/img/projects/carousel/05-wearable-technology.webp' | relative_url }}" alt="Wearable technology research highlight" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide">
          <img src="{{ '/assets/img/projects/carousel/06-light-based-communications.webp' | relative_url }}" alt="Light-based communications research highlight" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide" aria-hidden="true">
          <img src="{{ '/assets/img/projects/carousel/01-generative-ai-genai.webp' | relative_url }}" alt="" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide" aria-hidden="true">
          <img src="{{ '/assets/img/projects/carousel/02-ai-for-socio-economics-public-health.webp' | relative_url }}" alt="" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide" aria-hidden="true">
          <img src="{{ '/assets/img/projects/carousel/03-agrivoltaics-plant-modeling.webp' | relative_url }}" alt="" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide" aria-hidden="true">
          <img src="{{ '/assets/img/projects/carousel/04-gis-remote-sensing.webp' | relative_url }}" alt="" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide" aria-hidden="true">
          <img src="{{ '/assets/img/projects/carousel/05-wearable-technology.webp' | relative_url }}" alt="" class="projects-highlight-ribbon__image">
        </figure>
        <figure class="projects-highlight-ribbon__slide" aria-hidden="true">
          <img src="{{ '/assets/img/projects/carousel/06-light-based-communications.webp' | relative_url }}" alt="" class="projects-highlight-ribbon__image">
        </figure>
      </div>
    </div>
  </section>
  {% for category in page.display_categories %}
    {% case category %}
      {% when "Generative AI (GenAI)" %}
        {% assign cat_desc = "Research on large language models, diffusion models, and implicit neural representations for trustworthy AI, imaging, cultural heritage, and computational biology." %}
      {% when "AI for Remote Sensing & GIS" %}
        {% assign cat_desc = "Geospatial and remote-sensing research spanning change analysis, socio-hydrology, and hyperspectral interpretation for environmentally grounded decision support." %}
      {% when "AI for Sociology, Humanities & Socio-economics" %}
        {% assign cat_desc = "Interdisciplinary AI and statistical modelling for demographic analysis, behavioural simulation, and socially relevant population-level insight." %}
      {% when "Biomedical Engineering & Bio-imaging" %}
        {% assign cat_desc = "Clinical and translational work on preterm birth risk assessment, respiratory monitoring, dermatology AI, and multimodal stroke recovery modelling." %}
      {% when "Computer Vision (CV)" %}
        {% assign cat_desc = "Computer-vision projects covering activity understanding, surgical planning, irradiance-aware visual analysis, and energy-efficient foveated perception." %}
      {% when "Wearable Technology" %}
        {% assign cat_desc = "Wearable sensing systems for gait analysis, posture evaluation, biomechanics, and sports-performance monitoring outside conventional laboratory settings." %}
      {% when "Agrivoltaics & Plant Growth" %}
        {% assign cat_desc = "Digital-twin and plant-modelling research for sustainable agrivoltaic environments, tea growth monitoring, and data-driven resource optimization." %}
      {% when "Light-based Communications" %}
        {% assign cat_desc = "Optical wireless and light-based IoT research centered on energy-aware indoor networking, battery-free sensing, and data-energy co-optimization." %}
      {% when "Renewable Energy & Smart Grid" %}
        {% assign cat_desc = "AI-enabled energy research on appliance-level load disaggregation and efficient monitoring for scalable smart-grid deployment." %}
      {% when "Multispectral Imaging (MSI)" %}
        {% assign cat_desc = "In-house optical sensing systems for non-destructive assessment of soils, food quality, edible oils, and material characterization." %}
    {% endcase %}

    {% assign sorted_projects = site.projects | where: "category", category | sort: "importance" %}
    {% if sorted_projects.size > 0 %}
      <section class="project-category">
        <div class="project-category__header">
          <h2 class="project-category__title">{{ category }}</h2>
          <p class="project-category__description">{{ cat_desc }}</p>
        </div>
        <div class="project-category__content">
          <p class="project-category__sublabel">Projects in this area</p>
          <div class="row row-cols-1 row-cols-lg-2 project-category__projects">
          {% for project in sorted_projects %}
            {% include projects_horizontal.liquid %}
          {% endfor %}
          </div>
        </div>
      </section>
    {% endif %}
  {% endfor %}
</div>
