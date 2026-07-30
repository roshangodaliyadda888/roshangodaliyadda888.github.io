---
layout: page
permalink: /publications/
title: Publications
description: Scholarly publications organized chronologically with selected works highlighted separately.
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

This page presents journal articles, conference papers, datasets, book chapters, and other scholarly outputs. Publications are organized chronologically, with selected works highlighted separately.

## Selected Publications

<div class="publications">

{% bibliography --query @*[selected=true] %}

</div>

## Complete Publications

<div class="publications">

{% bibliography --query @*[selected!=true] %}

</div>
