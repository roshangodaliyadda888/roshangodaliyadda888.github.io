---
layout: page
title: Virtual Surgical Planning for Mandibular and Maxillary Reconstruction
description: Open-source surgical planning pipeline for jaw reconstruction using CBCT scans, reconstruction simulation, and printable guides.
importance: 20
category: Computer Vision (CV)
---

## Overview

Virtual Surgical Planning Tool for Mandibular and Maxillary Reconstruction




Reconstructing the jaw after cancer surgery or severe trauma is one of the most complex
procedures in craniomaxillofacial surgery — and the software that plans it (Materialise ProPlan,
KLS Martin IPS) costs tens of thousands of dollars, putting it out of reach for most hospitals in
low-resource settings. This project is building a fully open-source virtual surgical planning (VSP)
pipeline for mandible and maxilla reconstruction using fibula free flaps. Surgeons upload CBCT
scans of the mandible, maxilla, and fibula; the system segments the bone, simulates the
reconstruction, and automatically generates 3D-printable cutting guide STL files along with a
surgical planning PDF report. Built on the open-source 3D Slicer platform, the tool aims to make
advanced reconstructive planning accessible to hospitals worldwide, not just those who can
afford commercial licenses — while contributing a citable, validated pipeline to the surgical
research community.

![Virtual Surgical Planning]({{ '/assets/img/projects/cv-dental.png' | relative_url }}){: .img-fluid .rounded .z-depth-1 .mb-4 .project-detail-image }
