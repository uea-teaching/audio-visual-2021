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

_Aside_: What is salt and pepper noise?

- Also called impulse noise.
- Can be hardware dependent - hot pixels or dead pixels.
- Artificially applied by random selecting a subset of pixels and setting to black or white.

## Median Filter

![salt and pepper noise, $P=0.1$](assets/plots3/salt_pepper.png)

## Median Filter

![noisy and median filtered images](assets/plots3/sp_median_filtered.png)

## Median Filter

![original and median filtered images](assets/plots3/orig_median_filtered.png)

## Median Filter

![difference image](assets/plots3/orig_median_difference.png){width=50%}

## Median Filter

![gaussian and median filtered images](assets/plots3/gauss_median_filtered.png)

## Noise removal

::: columns
::::: column
![pixel values](assets/img4/noise-01.png)
:::::
::::: column
If we consider this 5 pixel neighbourhood, what will the median filter do?
:::::
:::

## Noise removal

::: columns
::::: column
![median filter](assets/img4/noise-02.png)
:::::
::::: column
The median filter removes spike noise.

::: incremental

- What will the gaussian filter do?

:::
:::::
:::

## Noise removal

::: columns
::::: column
![Gaussian filter](assets/img4/noise-03.png)
:::::
::::: column
The Gaussian filter amplifies noise.
:::::
:::
