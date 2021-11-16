---
title: Non-Linear Image Filtering
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
date: \today
---

# Content

- Order Statistics filters
- Morphological filtering
- Morphological operations for object detection
- Morphological operations for edge detection

# Order-Statistics Filters

Linear filters compute the sum of products between kernel coefficients and the image neighbourhood.

Instead, replace intensity with a measure obtained by ordering the pixel intensities in the neighbourhood.

- Common filters are **median**, **max** and **min**.

---

Crop a part of a larger image to uses as an example.

![Cameraman crop](assets/plots3/region_8x8.png)

---

First, window a region of size 3x3:

![region window](assets/plots3/region_select.png)

---

Sort the intensities in the region:

![ordered values](assets/plots3/region_ordered.png)

---

Sort the intensities in the region, and select the middle value:

![median value](assets/plots3/region_median.png)

---

Max filter is similar to median filter, but selects the maximum value:

![maximum value](assets/plots3/region_max.png)

---

Min filter is again similar, but selects the minimum value:

![minimum value](assets/plots3/region_min.png)

---

Order-statistics filters are good for noise removal where:

- Noise is random
- Noise is not dependent on surrounding pixels

For example, the salt and pepper noise model:

- Noisy pixels are the outliers in the local neighbourhood
- Replace outliers with estimate from image data

---

Aside: What is salt and pepper noise?

- Also called impulse noise.
- Can be hardware dependent - hot pixels or dead pixels.
- Artificially applied by random selecting a subset of pixels and setting to black or white.

## Median Filter

![salt and pepper noise](assets/plots3/salt_pepper.png)
