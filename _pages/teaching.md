---
layout: page
permalink: /teaching/
title: teaching
description: Teaching areas and curricular contributions of Professor G. M. R. I. Godaliyadda.
nav: true
nav_order: 6
calendar: false
---

<section class="teaching-page" aria-labelledby="teaching-title">
  <header class="teaching-page__header">
    <h2 id="teaching-title" class="visually-hidden">Teaching</h2>
    <p>
      Professor Godaliyadda teaches undergraduate and postgraduate courses in electrical engineering, signal
      processing, artificial intelligence, and machine learning. His teaching spans theoretical foundations together
      with modern data-driven methods used in contemporary engineering research.
    </p>
  </header>

  <section class="teaching-page__section" aria-labelledby="teaching-areas-title">
    <h2 id="teaching-areas-title">Teaching Areas</h2>
    <div class="teaching-page__divider" aria-hidden="true"></div>
    <ul class="teaching-page__list" aria-label="Teaching areas">
      <li>Random Signal Analysis</li>
      <li>Stochastic Processes</li>
      <li>Digital Signal Processing</li>
      <li>Computer Vision</li>
      <li>Machine Learning</li>
      <li>Control Systems</li>
      <li>Nonlinear Dynamics</li>
      <li>Information Theory</li>
    </ul>
  </section>
</section>

<style>
  .teaching-page {
    max-width: 44rem;
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

  .teaching-page__header p {
    margin: 0.75rem 0 0;
    line-height: 1.75;
  }

  .teaching-page__section {
    margin-top: 2rem;
  }

  .teaching-page__section h2 {
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
  }

  .teaching-page__divider {
    height: 1px;
    margin-bottom: 0.85rem;
    background: rgba(128, 128, 128, 0.24);
  }

  .teaching-page__list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0 1.5rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .teaching-page__list li {
    padding: 0.7rem 0;
    border-bottom: 1px solid rgba(128, 128, 128, 0.16);
    line-height: 1.6;
  }

  @media (max-width: 700px) {
    .teaching-page__list {
      grid-template-columns: 1fr;
    }
  }
</style>
