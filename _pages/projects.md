---
layout: page
title: projects
permalink: /projects/
description: A growing collection of your research projects and grants.
nav: true
nav_order: 3
display_categories: ["Biomedical Signal Processing & Wearable AI", "Smart Grids & Energy Analytics", "Multispectral Imaging & Remote Sensing", "Generative AI & LLMs", "AI for Public Health & Social Impact", "Computer Vision, Robotics & Assisted Navigation", "Optical Wireless Communications"]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
    {% if category == "Biomedical Signal Processing & Wearable AI" %}
      {% assign cat_img = "assets/img/biomedical_wearable_ai.jpg" %}
      {% assign cat_desc = "Advanced wearable devices, fetal movement detection, and biomedical signal analysis for healthcare applications." %}
    {% elsif category == "Smart Grids & Energy Analytics" %}
      {% assign cat_img = "assets/img/smart_grids_energy.jpg" %}
      {% assign cat_desc = "Non-intrusive load monitoring (NILM), photovoltaic integration, and smart distribution systems for sustainable energy management." %}
    {% elsif category == "Multispectral Imaging & Remote Sensing" %}
      {% assign cat_img = "assets/img/multispectral_remote_sensing.jpg" %}
      {% assign cat_desc = "Hyperspectral unmixing, agricultural digital twins, and industrial monitoring using advanced spectral imaging techniques." %}
    {% elsif category == "Generative AI & LLMs" %}
      {% assign cat_img = "assets/img/generative_ai_llms.jpg" %}
      {% assign cat_desc = "Implicit neural representations, audio generation, and large language model insights for multidisciplinary research." %}
    {% elsif category == "AI for Public Health & Social Impact" %}
      {% assign cat_img = "assets/img/public_health_social.jpg" %}
      {% assign cat_desc = "Epidemic modeling, social interaction modeling during pandemics, and educational impact analysis." %}
    {% elsif category == "Computer Vision, Robotics & Assisted Navigation" %}
      {% assign cat_img = "assets/img/computer_vision_robotics.jpg" %}
      {% assign cat_desc = "Visual surveillance, vehicle tracking, robotic path planning, and autonomous navigation in complex environments." %}
    {% elsif category == "Optical Wireless Communications" %}
      {% assign cat_img = "assets/img/optical_communications.jpg" %}
      {% assign cat_desc = "Visible light communication (VLC), underwater optical wireless communication, and energy-autonomous light-based IoT." %}
    {% endif %}

    <div class="category-banner my-5 p-4 rounded shadow-sm" style="background: var(--global-card-bg); border-left: 5px solid var(--global-theme-color); transition: all 0.3s ease;">
      <div style="display: flex; flex-direction: row; align-items: center; justify-content: flex-start; gap: 24px; flex-wrap: nowrap;">
        <div style="flex: 0 0 25%; max-width: 25%; min-width: 150px;">
          <img src="{{ cat_img | relative_url }}" alt="Sector Banner" class="img-fluid rounded premium-banner-class" style="width: 100%; height: 140px; object-fit: cover; box-shadow: 0 4px 8px rgba(0,0,0,0.15);">
        </div>
        <div style="flex: 1 1 auto; min-width: 0;">
          <h2 class="category-title font-weight-bold" style="color: var(--global-text-color); font-size: 1.6rem; margin: 0; word-wrap: break-word;">{{ category }}</h2>
          <p class="category-description text-muted mt-2 mb-0" style="font-size: 0.95rem; line-height: 1.5; word-wrap: break-word;">{{ cat_desc }}</p>
        </div>
      </div>
    </div>

  {% assign categorized_projects = site.projects | where: "category", category %}
  {% assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display projects without categories -->

{% assign sorted_projects = site.projects | sort: "importance" %}

  <!-- Generate cards for each project -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for project in sorted_projects %}
      {% include projects_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
