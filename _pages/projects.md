---
layout: page
title: Projects
permalink: /projects/
description: Research projects grouped by the updated thematic categories in the project portfolio source document.
nav: true
nav_order: 3
display_categories: ["Generative AI (GenAI)", "AI for Remote Sensing & GIS", "AI for Sociology, Humanities & Socio-economics", "Biomedical Engineering & Bio-imaging", "Computer Vision (CV)", "Wearable Technology", "Agrivoltaics & Plant Growth", "Light-based Communications", "Renewable Energy & Smart Grid", "Multispectral Imaging (MSI)"]
---

<link rel="stylesheet" href="{{ '/assets/css/projects-page.css' | relative_url }}">

<div class="projects">
  <p class="projects-page-intro">
    This page reorganizes the active project portfolio into the updated research categories provided in the source document. Each entry includes a short summary here, with a fuller explanation and the relevant visual on the project page itself.
  </p>
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
        <div class="row row-cols-1 row-cols-lg-2">
          {% for project in sorted_projects %}
            {% include projects_horizontal.liquid %}
          {% endfor %}
        </div>
      </section>
    {% endif %}
  {% endfor %}
</div>
