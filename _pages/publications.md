---
layout: page
permalink: /publications/
title: Publications
description: High-impact publication audit aligned to the curated PDF structure.
nav: true
nav_order: 2
---

{% assign audit = site.data.high_impact_publications %}
{% assign journal_groups = audit.groups | where_exp: "group", "group.name != 'Tier-1 conference publication'" %}

<div class="impact-audit">
  <section class="impact-audit__hero" aria-labelledby="impact-audit-title">
    <p class="impact-audit__eyebrow">Publication Impact Screen</p>
    <h1 id="impact-audit-title">Q1 Journal and Top-tier Conference Publications</h1>
    <p class="impact-audit__subtitle">
     
    </p>
  </section>

  <section class="impact-audit__summary" aria-labelledby="impact-summary-title">
    <div class="impact-audit__heading">
      <h2 id="impact-summary-title">1. Audit Outcome and Screening Basis</h2>
      <div class="impact-audit__divider" aria-hidden="true"></div>
    </div>

    <div class="impact-audit__stats" role="list" aria-label="Audit summary statistics">
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">{{ audit.summary.q1_journals }}</p>
        <p class="impact-audit__stat-label">Q1 journal articles</p>
      </article>
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">23</p>
        <p class="impact-audit__stat-label">Top-tier conference papers</p>
      </article>
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">{{ audit.summary.distinct_q1_journals }}</p>
        <p class="impact-audit__stat-label">Distinct Q1 journals</p>
      </article>
      <article class="impact-audit__stat" role="listitem">
        <p class="impact-audit__stat-value">{{ audit.summary.high_impact_fields }}</p>
        <p class="impact-audit__stat-label">High-impact fields</p>
      </article>
    </div>

    <div class="impact-audit__note">
      <p>
        This page mirrors the curated high-impact audit order: reverse-chronological within each field, limited to
        the screened Q1 journal set and the selected top-tier conference publications.
      </p>
    </div>
  </section>

  <section class="impact-audit__section" aria-labelledby="impact-q1-title">
    <div class="impact-audit__heading">
      <h2 id="impact-q1-title">2. Q1 Journal Publications</h2>
      <div class="impact-audit__divider" aria-hidden="true"></div>
    </div>

    {% for group in journal_groups %}
      <section class="impact-field" aria-labelledby="impact-field-{{ forloop.index }}">
        <h3 id="impact-field-{{ forloop.index }}">{{ group.name }} ({{ group.count }})</h3>

        <div class="impact-field__list">
          {% for item in group.items %}
            <article class="impact-item">
              <div class="impact-item__id">{{ item.id }}</div>
              <div class="impact-item__body">
                <p class="impact-item__year">{{ item.year }}</p>
                <h4>{{ item.title }}</h4>
                <p class="impact-item__authors">{{ item.authors_abbrev }}</p>
                <p class="impact-item__venue">{{ item.venue_line }}</p>
              </div>
            </article>
          {% endfor %}
        </div>
      </section>
    {% endfor %}
  </section>

  <section class="impact-audit__section" aria-labelledby="impact-tier1-title">
    <div class="impact-audit__heading">
      <h2 id="impact-tier1-title">3. Top-tier Conference Publications</h2>
      <div class="impact-audit__divider" aria-hidden="true"></div>
    </div>

    <section class="impact-field" aria-labelledby="impact-conf-1">
      <h3 id="impact-conf-1">Generative AI, Signal Processing, and Image Processing (Diffusion, INR and LLMs) – Algorithmic and Fundamental Theory</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C01</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">Harshana Weligampola, Gihan Jayatilaka, Suren Sritharan, Parakrama Ekanayake, Roshan Ragel, Vijitha Herath, Roshan Godaliyadda, “An Optical physics inspired CNN approach for intrinsic image decomposition,” IEEE ICIP 2021, Anchorage, Alaska, USA, September, 2021.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C02</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">P. Thennakoon, A. Ranasinghe, M. de Silva, B. Epakanda, R. Godaliyadda, M. P. B. Ekanayake, and V. R. Herath, “COSMO-INR: Complex Sinusoidal Modulation for Implicit Neural Representations,” in proceedings of the 14th International Conference on Learning Representations (ICLR 2026). Rio de Janeiro, Brazil, April 2026.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="impact-field" aria-labelledby="impact-conf-2">
      <h3 id="impact-conf-2">Smart Grid: NILM, Forecasting, Agrovoltaics and PV Integration</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C03</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">H. G. C. P. Dinesh, P. H. Perera, G. M. R. I. Godaliyadda, M. P. B. Ekanayake, J. B. Ekanayake, “Residential Appliance Monitoring based on Low Frequency Smart Meter Measurements,” 6th IEEE International Conference on Smart grid Communications (IEEE SmartGridComm), Miami, Florida, USA, November, 2015.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="impact-field" aria-labelledby="impact-conf-3">
      <h3 id="impact-conf-3">Remote Sensing and Hyperspectral Imaging</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C04</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">Mevan Ekanayake, Hasantha Ekanayake, Anusha Rathnayake, Sajani Vithana, Vijitha Herath, Roshan Godaliyadda and Parakrama Ekanayake, “A Semi-Supervised Algorithm to Map Major Vegetation Zones using Satellite Hyperspectral Data,” in 9th Workshop on Hyperspectral Image and Signal Processing (WHISPERS 2018), Amsterdam, The Netherlands, Sep. 2018.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C05</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">Mevan Ekanayake; Bhathiya Rathnayake; Hasantha Ekanayake; Anusha Rathnayake; Vijitha Herath; Roshan Godaliyadda; Parakrama Ekanayake; “Enhanced Hyperspectral Unmixing via Non-Negative Matrix Factorization Incorporating the End Member Independence”, in IEEE International Geoscience and Remote Sensing Symposium (IGARSS-2019), Yokohama, Japan, August, 2019.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C06</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">N. Wasalathilaka, D. Perea, O. Samarakoon, B. Wijenayake, R. Godaliyadda, V. Herath, and P. Ekanayake, “A Controlled Benchmark of Visual State-Space Backbones with Domain-Shift and Boundary Analysis for Remote-Sensing Segmentation,” in the 2026 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2026), Washington, D.C., USA, August 2026.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C07</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">B. Wijenayake, N. Wasalathilake, R. Godaliyadda, V. Herath, P. Ekanayake, and V. M. Patel, “Mitigating Long-Tail Bias via Prompt-Controlled Diffusion Augmentation,” in the 2026 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2026), Washington, D.C., USA, August 2026.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="impact-field" aria-labelledby="impact-conf-4">
      <h3 id="impact-conf-4">Multispectral Imaging for Food, Agriculture, and Manufacturing Quality</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C08</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">G. W. K. Prabhath, W. G. C. Bandara, D. W. S. C. B. Dissanayake, H. M. V. R. Hearath, G. M. R. I. Godaliyadda, M. P. B. Ekanayake, S. M. D. Demini, and T. Madhujith, "Multispectral Imaging for Detection of Adulterants in Turmeric Powder," in Optical Sensors and Sensing Congress (ES, FTS, HISE, Sensors), OSA Technical Digest (Optical Society of America, 2019), paper HTu3B.3., San Jose, California, USA, June, 2019.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C09</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">H. M. H. K. Weerasooriya, H. M. S. Lakmal, D. Y. L. Ranasinghe, W. G. C. Bandara, H. M. V. R. Herath, G. M. R. I. Godaliyadda, M. P. B. Ekanayake, and T. Madujith, "Transmittance Multispectral Imaging for Edible Oil Quality Assessment," in Imaging and Applied Optics Congress, OSA Technical Digest (Optical Society of America, 2020), paper JW5C.8., Vancouver, Canada, June, 2020.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="impact-field" aria-labelledby="impact-conf-5">
      <h3 id="impact-conf-5">Optical Wireless Communications</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C10</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">K. W. S. Palitharathna, R. I. Godaliyadda, V. R. Herath, and H. A. Suraweera, "Relay-assisted optical wireless communications in turbid water," in Proc. 13th ACM International Conference on Underwater Networks and Systems (WUWNET '18), Shenzhen, China, Dec. 2018.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C11</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">K. W. S. Palitharathna, H. A. Suraweera, R. I. Godaliyadda, V. R. Herath and Z. Ding, "Impact of receiver orientation on full-duplex relay aided NOMA underwater optical wireless systems," in Proc. IEEE International Conference on Communications (ICC 2020), Dublin, Ireland, June, 2020.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C12</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">K. W. S. Palitharathna, H. A. Suraweera, R. I. Godaliyadda, V. R. Herath and J.S. Thompson, "Multi-AUV Placement for Coverage Maximization in Underwater Optical Wireless Sensor Networks," in Proc. Global OCEANS 2020 MTS/IEEE, Marina Bay, Singapore, October, 2020.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C13</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">A. Perera, M. Katz, R. Godaliyadda, J. Hakkinen, E. Strommer, “Light-based Internet of Things: Implementation of an Optically Connected Energy-autonomous node”, IEEE Wireless Communications and Networking Conference (IEEE WCNC 2021), Nanjing, China, April, 2021.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C14</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">K. W. S. Palitharathna, H. A. Suraweera, R. I. Godaliyadda, V. R. Herath, "Rate Maximization for Lightwave Power Transfer-Enabled Cooperative Half/Full-Duplex UOWC Systems," in Proc. 2021 IEEE 22nd International Workshop on Signal Processing Advances in Wireless Communications (SPAWC 2021), Lucca, Italy, September, 2021.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="impact-field" aria-labelledby="impact-conf-6">
      <h3 id="impact-conf-6">Computer Vision, Machine Vision, Robotics, and Assisted Navigation</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C15</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">S. Narthana, S. Sivasthigan, M. Thamayanthi, R. Godaliyadda, P. Ekanayake, and V. Herath, “A Structured Analysis and Taxonomy of Scene Graph Representations for Group Activity Understanding,” in Proceedings of the SG4SI Workshop, IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), Tucson, Arizona, March 2026.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C16</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">S. Narthana, S. Sivasthigan, R. Godaliyadda, P. Ekanayake, and V. Herath, “Efficient and Intrinsically Interpretable Spatiotemporal Transformer with Gated Fusion for Group Activity Recognition,” in Proceedings of the 2nd SAUAFG (Second International Workshop on AI-driven Skilled Activity Understanding, Assessment &amp; Feedback Generation) Workshop, CVPR Workshops, Denver, Colorado, June 2026.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="impact-field" aria-labelledby="impact-conf-7">
      <h3 id="impact-conf-7">Image and Signal Processing for Enhancement, Recognition, and Localization</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C17</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">G.M.R.I. Godaliyadda and H.K. Garg, “Analysis of Super Resolution Spectral Estimation Techniques for Indoor Positioning Applications,” in Proc. 9th International Conference on Signal Processing (ICSP’08), Beijing, China, October, 2008.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C18</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">G.M.R.I. Godaliyadda and H.K. Garg, “Versatile Algorithms for Accurate Indoor Geolocation,” in Proc. 16th International Conference on Digital Signal Processing (DSP ‘09), Santorini, Greece, July, 2009.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C19</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">G.M.R.I. Godaliyadda and H.K. Garg, “A Time Domain Eigen Value Method for Indoor Localization,” in Proc. 9th Annual Wireless Telecommunications Symposium (WTS’10), Tampa, Florida, USA, April, 2010.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C20</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">T.A. Ratnayake, N.N. Pollwaththage, D.B.W. Nettasinghe, G.M.R.I. Godaliyadda, M.P.B. Ekanayake, J.V. Wijayakulasooriya, “Material based Acoustic Signal Classification- A Subspace-based Approach,” TENCON-2013, Xian, China, October, 2013.</p>
          </div>
        </article>
      </div>
    </section>

    <section class="impact-field" aria-labelledby="impact-conf-8">
      <h3 id="impact-conf-8">Spectral Imaging and Remote Sensing for Environmental and Industrial Monitoring</h3>
      <div class="impact-field__list">
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C21</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">A. Wijesinghe, D. Wickramsinghe, C. Wijedasa, Y. Ranasinghe, V. Herath, R. Godaliyadda, P. Ekanayake, S. Jinadasa, “Transmittance Multispectral Imaging System to Estimate Potable Water Quality Parameters,” OSA Imaging and Applied Optics Congress, OSA Virtual Meeting, July, 2021.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C22</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">L. Ramanayake, N. Senerath, D. Jayasundara, K. Prabath, K. Weerasooriya, M. Fernando, S. Kumara, V. Herath, R. Godaliyadda, P. Ekanayake, S. Athukorala, “Reflectance Multispectral Imaging for Identification of Algae Contamination in High Voltage Insulators,” OSA Imaging and Applied Optics Congress, OSA Virtual Meeting, July, 2021.</p>
          </div>
        </article>
        <article class="impact-item impact-item--conference">
          <div class="impact-item__id">C23</div>
          <div class="impact-item__body">
            <p class="impact-item__venue">I.Z.M. Zumri, M.L.A.S. Mahmood, Bandara S., M.A.R.M. Fernando, G.M.R.I. Godaliyadda, H.M.V.R. Herath, M.P.B. Ekanayake, J.R.S. Kumara, K.M.K.S. Bandara, “Spectral Imaging based Condition Assessment of Field Aged Power Transformers,” Imaging Systems and Applications, Optica Imaging Congress, Boston, Massachusetts, USA, August, 2023.</p>
          </div>
        </article>
      </div>
    </section>
  </section>
</div>

<style>
  .impact-audit {
    max-width: 60rem;
    margin: 0 auto;
  }

  .impact-audit__hero {
    margin-bottom: 2.5rem;
    padding-bottom: 1.25rem;
    border-bottom: 1px solid rgba(128, 128, 128, 0.16);
  }

  .impact-audit__eyebrow {
    margin: 0 0 0.45rem;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--global-theme-color);
  }

  .impact-audit__hero h1 {
    margin: 0;
    font-size: 2.15rem;
    line-height: 1.15;
    letter-spacing: -0.02em;
  }

  .impact-audit__subtitle {
    max-width: 46rem;
    margin: 1rem 0 0;
    font-size: 1rem;
    line-height: 1.8;
    color: var(--global-text-color);
    opacity: 0.92;
  }

  .impact-audit__section + .impact-audit__section,
  .impact-field + .impact-field {
    margin-top: 2.5rem;
  }

  .impact-audit__heading h2 {
    margin: 0;
    font-size: 1.14rem;
    font-weight: 600;
    letter-spacing: -0.01em;
  }

  .impact-audit__divider {
    width: 100%;
    height: 1px;
    margin-top: 0.75rem;
    background: rgba(128, 128, 128, 0.22);
  }

  .impact-audit__stats {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.1rem;
    margin-top: 1.4rem;
  }

  .impact-audit__stat {
    padding: 1rem 1rem 0.95rem;
    border: 1px solid rgba(128, 128, 128, 0.16);
    border-radius: 10px;
    background: rgba(128, 128, 128, 0.03);
  }

  .impact-audit__stat-value {
    margin: 0;
    font-size: 1.7rem;
    font-weight: 600;
    line-height: 1.1;
  }

  .impact-audit__stat-label,
  .impact-audit__note p,
  .impact-item__authors,
  .impact-item__venue,
  .impact-item__year {
    margin: 0;
    line-height: 1.7;
    color: var(--global-text-color);
  }

  .impact-audit__note {
    max-width: 48rem;
    margin-top: 1.15rem;
    margin-bottom: 1.75rem;
  }

  .impact-field h3 {
    display: inline-flex;
    align-items: center;
    margin: 0.65rem 0 0.95rem;
    padding-left: 0.8rem;
    position: relative;
    font-size: 1.02rem;
    font-weight: 600;
    line-height: 1.45;
  }

  .impact-field h3::before {
    content: "";
    position: absolute;
    left: 0;
    top: 0.2rem;
    bottom: 0.2rem;
    width: 3px;
    border-radius: 999px;
    background: var(--global-theme-color);
  }

  .impact-field__list {
    display: grid;
    gap: 0;
    padding: 0.2rem 1.1rem 0.15rem;
    border: 1px solid rgba(128, 128, 128, 0.14);
    border-radius: 12px;
    background: rgba(128, 128, 128, 0.025);
  }

  .impact-item {
    display: grid;
    grid-template-columns: 4.5rem minmax(0, 1fr);
    gap: 1.15rem;
    padding: 1rem 0;
    border-bottom: 1px solid rgba(128, 128, 128, 0.14);
  }

  .impact-field__list .impact-item:first-child,
  .impact-audit__section > .impact-item {
    border-top: 1px solid rgba(128, 128, 128, 0.14);
  }

  .impact-item__id {
    padding-top: 0.1rem;
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--global-theme-color);
    letter-spacing: 0.04em;
  }

  .impact-item__year {
    font-size: 0.92rem;
    opacity: 0.8;
  }

  .impact-item h4 {
    max-width: 48rem;
    margin: 0.18rem 0 0.4rem;
    font-size: 1.03rem;
    font-weight: 500;
    line-height: 1.5;
    letter-spacing: -0.01em;
  }

  .impact-item__authors {
    margin-top: 0.1rem;
  }

  .impact-item__venue {
    margin-top: 0.05rem;
    opacity: 0.88;
  }

  .impact-item:hover h4 {
    color: var(--global-theme-color);
  }

  html[data-theme="dark"] .impact-audit__hero,
  body[data-theme="dark"] .impact-audit__hero,
  html.dark .impact-audit__hero,
  body.dark .impact-audit__hero {
    border-bottom-color: rgba(255, 255, 255, 0.12);
  }

  html[data-theme="dark"] .impact-audit__stat,
  body[data-theme="dark"] .impact-audit__stat,
  html.dark .impact-audit__stat,
  body.dark .impact-audit__stat {
    border-color: rgba(255, 255, 255, 0.12);
    background: rgba(255, 255, 255, 0.03);
  }

  html[data-theme="dark"] .impact-field__list,
  body[data-theme="dark"] .impact-field__list,
  html.dark .impact-field__list,
  body.dark .impact-field__list {
    border-color: rgba(255, 255, 255, 0.12);
    background: rgba(255, 255, 255, 0.02);
  }

  @media (max-width: 900px) {
    .impact-audit__stats {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 640px) {
    .impact-audit__stats,
    .impact-item {
      grid-template-columns: 1fr;
    }

    .impact-audit__hero {
      margin-bottom: 2rem;
      padding-bottom: 1rem;
    }

    .impact-audit__hero h1 {
      font-size: 1.8rem;
    }

    .impact-audit__heading h2 {
      font-size: 1.04rem;
      line-height: 1.4;
    }

    .impact-field h3 {
      font-size: 0.96rem;
      padding-left: 0.7rem;
    }

    .impact-item {
      gap: 0.45rem;
      padding: 0.9rem 0;
    }

    .impact-field__list {
      padding: 0.15rem 0.85rem 0.1rem;
      border-radius: 10px;
    }
  }
</style>
