---
layout: page
title: Foveated Vision
description: Energy-efficient multi-camera perception that activates high-resolution views only where added information justifies the cost.
importance: 21
category: Computer Vision (CV)
---

<div class="project-overview" markdown="1">

## Overview

This project develops an energy-efficient vision system for always-on edge applications. Instead
of continuously running multiple high-resolution cameras, a low-power camera continuously
monitors the wider scene and identifies where motion or important activity is occurring. The
system then selectively activates only the high-resolution cameras needed to capture those
regions in greater detail. An adaptive controller evaluates the expected visual information gain
against the additional energy and computational cost before activating each camera. The
captured high-resolution regions are then combined with the wider low-resolution view to create
a detailed representation of the scene. By focusing camera and computing resources only
where they are needed, the system reduces unnecessary power consumption and processing
while maintaining useful visual information. This approach is suitable for applications such as
robotics, smart surveillance, drones, and other battery-powered edge vision systems that
require continuous environmental awareness and efficient real-time processing.
</div>

![Foveated Vision]({{ '/assets/img/projects/foveated-vision.png' | relative_url }}){: .img-fluid .rounded .z-depth-1 .mb-4 .project-detail-image }


