---
layout: page
permalink: /publications/
title: Publications
description: Journal articles, conference papers, datasets, book chapters, and other scholarly outputs.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

## Selected Work

<div class="publications">

{% bibliography --query @*[selected=true] %}

</div>

## Complete Publications

<div class="publications">

{% bibliography --query @*[selected!=true] %}

</div>
