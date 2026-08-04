---
layout: page
title: Projects
permalink: /projects/
description: This page presents selected funded research projects and major multidisciplinary research initiatives led or co-led by Professor G. M. R. I. Godaliyadda. The projects span biomedical sensing, artificial intelligence, smart energy systems, imaging, public health, robotics, and optical communications.
nav: true
nav_order: 3
display_categories: ["Biomedical Signal Processing & Wearable AI", "Computer Vision, Robotics & Assisted Navigation", "Smart Grids & Sustainable Energy", "Multispectral Imaging & Remote Sensing", "AI for Public Health, Education & Society", "Optical Wireless Communications", "AI Foundations & Generative Models"]
horizontal: false
---

<link rel="stylesheet" href="{{ '/assets/css/projects-page.css' | relative_url }}">

<div class="projects">
{% if site.enable_project_categories and page.display_categories %}
  <p class="projects-page-intro">
    This page presents selected funded research projects and major multidisciplinary research initiatives led or co-led by Professor G. M. R. I. Godaliyadda. The projects span biomedical sensing, artificial intelligence, smart energy systems, imaging, public health, robotics, and optical communications.
  </p>

  <!-- Display categorized projects -->
  {% for category in page.display_categories %}
    {% if category == "Biomedical Signal Processing & Wearable AI" %}
      {% assign cat_img = "assets/img/biomedical_wearable_ai.jpg" %}
      {% assign cat_alt = "Biomedical sensing and wearable health technologies" %}
      {% assign cat_desc = "Wearable sensing, physiological-signal analysis, maternal and fetal monitoring, and AI-assisted assessment of health and human performance." %}
    {% elsif category == "Computer Vision, Robotics & Assisted Navigation" %}
      {% assign cat_img = "assets/img/computer_vision_robotics.jpg" %}
      {% assign cat_alt = "Computer vision, robotics, and assisted navigation" %}
      {% assign cat_desc = "Visual intelligence, scene understanding, activity recognition, robotic navigation, and decision-support systems." %}
    {% elsif category == "Smart Grids & Sustainable Energy" %}
      {% assign cat_img = "assets/img/smart_grids_energy.jpg" %}
      {% assign cat_alt = "Smart grids and sustainable energy systems" %}
      {% assign cat_desc = "Data-driven monitoring, load disaggregation, renewable-energy integration, distribution-system analysis, and intelligent energy management." %}
    {% elsif category == "Multispectral Imaging & Remote Sensing" %}
      {% assign cat_img = "assets/img/multispectral_remote_sensing.jpg" %}
      {% assign cat_alt = "Multispectral imaging and remote sensing" %}
      {% assign cat_desc = "Imaging and machine-learning methods for agriculture, food quality, infrastructure monitoring, environmental sensing, and remote observation." %}
    {% elsif category == "AI for Public Health, Education & Society" %}
      {% assign cat_img = "assets/img/public_health_social.jpg" %}
      {% assign cat_alt = "Artificial intelligence for public health, education, and society" %}
      {% assign cat_desc = "Multidisciplinary AI and data-driven modelling for public health, education, social research, policy analysis, and societal resilience." %}
    {% elsif category == "Optical Wireless Communications" %}
      {% assign cat_img = "assets/img/optical_communications.jpg" %}
      {% assign cat_alt = "Optical wireless communication systems and light-based IoT" %}
      {% assign cat_desc = "Optical communication systems, light-based IoT, underwater links, energy-aware networking, and related communication technologies." %}
    {% elsif category == "AI Foundations & Generative Models" %}
      {% assign cat_img = "assets/img/generative_ai_llms.jpg" %}
      {% assign cat_alt = "AI foundations and generative modelling" %}
      {% assign cat_desc = "Research on generative modelling, implicit neural representations, computational acceleration, and emerging machine-learning architectures." %}
    {% endif %}

    {% include project_sector_banner.liquid title=category description=cat_desc image=cat_img alt=cat_alt %}

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
