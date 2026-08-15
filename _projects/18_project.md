---
layout: page
title: Data-Centric Dermatology AI
description: Fair, robust dermatology AI using controlled generative augmentation and validated lesion segmentation pipelines.
importance: 18
category: Biomedical Engineering & Bio-imaging
---

<div class="project-overview" markdown="1">

## Overview

This ongoing research project focuses on data-centric artificial intelligence for dermatology,
aiming to improve the fairness, reliability, and real-world robustness of automated skin-disease
analysis. Conducted in collaboration with MedirAI, a Canada-based medical-AI company, the
work addresses a key limitation of current dermatology AI: models are trained on large but
highly imbalanced datasets, where common conditions dominate while rare diseases and darker
skin tones remain under-represented. The research follows two complementary directions. The
first develops generative data-augmentation methods, centered on GAN and diffusion-based
image generation, to synthesize clinically valid dermatology images that are controllable by
condition, skin tone, and Fitzpatrick type, closing the gaps left by scarce real data. The second
develops skin-lesion segmentation methods that accurately outline lesions despite
surrounding clutter and remain robust on smartphone and edge-device images, trained on a
dataset in which every mask is explicitly validated. Together, they form a general-purpose
framework for equitable, deployment-ready dermatological image analysis across diverse
patient populations.
</div>

![Data-Centric Dermatology AI]({{ '/assets/img/projects/dermatology-ai.png' | relative_url }}){: .img-fluid .rounded .z-depth-1 .mb-4 .project-detail-image }


