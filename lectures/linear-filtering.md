---
title: Linear Image Filtering
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
date: November 22, 2021
---

# Content

- 2D Convolutions
- Smoothing Filters
- Sharpening and Unsharp Masking
- Template Matching

## What is Image Filtering? {data-auto-animate="true"}

**Filtering** replaces each pixel with a value based on some function performed on it’s _local neighbourhood_.

## What is Image Filtering? {data-auto-animate="true"}

Used for smoothing and sharpening...

![Sharpen Example](assets/plots3/sharp_example.png)

## What is Image Filtering? {data-auto-animate="true"}

Estimating gradients...

![Gradient Example](assets/plots3/gradient_example.png)

## What is Image Filtering? {data-auto-animate="true"}

Removing noise...

![Noise Example](assets/plots3/noise_example.png)

## Linear Filtering

Linear Filtering is defined as a convolution.

This is a _sum of products_ between an image region and a **kernel** matrix:

$$g(i, j) = \sum_{m=-a}^{a}\sum_{n=-b}^{b} f(i - m, j - n) h(m, n)$$

where $g$ is the filtered image, $f$ is the original image, $h$ is the kernel, and $i$ and $j$ are the image coordinates.

## Convolution

Typically:

$$a=\lfloor \frac{h_{rows}}{2} \rfloor, ~ b=\lfloor \frac{h_{cols}}{2} \rfloor$$

So for a 3x3 kernel:

$$ \text{both } m, n = -1, 0, 1$$

::: notes
Kernel does not need to be square - but often are.
:::

## Kernel Matrix

![The kernel origin is in the _centre_.](assets/plots3/kernel_coords.png)

::: notes
Recall: the image coordinate origin is in the top left.
:::

## Convolution {data-auto-animate="true"}

1. Scan image with a sub-window centred at each pixel.

   - The sub-window is known as the kernel, or mask.

2. Replace the pixel with the sum of products between the kernel coefficients and all of the pixels beneath the kernel.

   - Sum of products only for linear filters

3. Slide the kernel so it’s centred on the next pixel and repeat for all pixels in the image.

## Convolution {data-auto-animate="true"}

![The kernel is positioned at (1,1) in input image.](assets/plots3/kernel_11_00.png)

## Convolution {data-auto-animate="true"}

![We iterate the values of $m$ and $n$.](assets/plots3/kernel_11_01.png)

## Convolution {data-auto-animate="true"}

![$m=-1, ~n=0$](assets/plots3/kernel_11_02.png)

## Convolution {data-auto-animate="true"}

![$m=-1, ~n=1$](assets/plots3/kernel_11_03.png)

## Convolution {data-auto-animate="true"}

![$m=0, ~n=1$](assets/plots3/kernel_11_04.png)

## Convolution {data-auto-animate="true"}

![Iteration is complete.](assets/plots3/kernel_11_all.png)

## Convolution {data-auto-animate="true"}

![The product sum is assigned to the output image.](assets/plots3/kernel_11_g11.png)

## Convolution {data-auto-animate="true"}

![Slide the kernel along the row.](assets/plots3/kernel_12_g12.png)

## Convolution {data-auto-animate="true"}

![Slide the kernel along the row.](assets/plots3/kernel_13_g13.png)

## Convolution {data-auto-animate="true"}

![Move the kernel to the next row.](assets/plots3/kernel_21_g21.png)

## Convolution {data-auto-animate="true"}

![Continue sliding.](assets/plots3/kernel_28_g28.png)

## Convolution {data-auto-animate="true"}

![The image is completely covered.](assets/plots3/kernel_88_g88.png)

## What about the edges? {data-auto-animate="true"}

::: columns
::::: column

![](assets/plots3/conv_edge_00.png)

:::::
::::: column

The filter window falls off the edge of the image.

:::::
:::

## What about the edges? {data-auto-animate="true"}

::: columns
::::: column

![](assets/plots3/conv_edge_zeros.png)

:::::
::::: column

A common strategy is to pad with zeros.

The image is effectively larger than the original.

:::::
:::

## What about the edges? {data-auto-animate="true"}

::: columns
::::: column

![](assets/plots3/conv_edge_wrap.png)

:::::
::::: column

We could _wrap_ the pixels, from each edge to the opposite.

Again, the image is effectively larger.

:::::
:::

## What about the edges? {data-auto-animate="true"}

::: columns
::::: column

![](assets/plots3/conv_edge_repeat.png)

:::::
::::: column

Alternatively, we could _repeat_ the pixels, extending each edge outward.

:::::
:::

# Linear Kernels

---

What would the filtered image look like?

![kernel 1](assets/plots3/kernel1_q.png)

---

No change!

![kernel 1](assets/plots3/kernel1_a.png)

---

What would the filtered image look like?

![kernel 2](assets/plots3/kernel2_q.png)

---

Shifted left by 1 pixel.

![kernel 2](assets/plots3/kernel2_a.png)

---

What would the filtered image look like?

![kernel 3](assets/plots3/kernel3_q.png)

---

Blurred...

![kernel 3](assets/plots3/kernel3_a.png)

# Smoothing Filters

## Mean Filter {data-auto-animate="true"}

replace each pixel with the mean of local neighbours:

$$
h = \frac{1}{9}\times
   \begin{bmatrix}
      1 & 1 & 1 \\
      1 & 1 & 1 \\
      1 & 1 & 1
   \end{bmatrix}
$$

## Mean Filter {data-auto-animate="true"}

![Mean filtered with 3 x 3 kernel](assets/plots3/mean_3x3.png)

## Mean Filter {data-auto-animate="true"}

we can increase the size of the kernel to get a smoother image:

$$
h = \frac{1}{25}\times
   \begin{bmatrix}
      1 & 1 & 1 & 1 & 1 \\
      1 & 1 & 1 & 1 & 1 \\
      1 & 1 & 1 & 1 & 1 \\
      1 & 1 & 1 & 1 & 1 \\
      1 & 1 & 1 & 1 & 1
   \end{bmatrix}
$$

## Mean Filter {data-auto-animate="true"}

![Mean filtered with 5 x 5 kernel](assets/plots3/mean_5x5.png)

## Mean Filter {data-auto-animate="true"}

![Mean filtered with 7 x 7 kernel](assets/plots3/mean_7x7.png)

## Gaussian blur {data-auto-animate="true"}

Similar to mean filter:

- Replace intensities with a weighted average of neighbours.
- Pixels closer to the centre of the kernel have more influence.

## Gaussian blur {data-auto-animate="true"}

::: {style="font-size:1.5em"}

$$
g(x,y) = \frac{1}{2\pi\sigma^2}~ {\rm  e}^{ - \frac{x^2+y^2}{2\sigma^2} }
$$

:::

## Gaussian blur {data-auto-animate="true"}

![Gaussian kernel](assets/plots3/2d_gaussian.png)

## Gaussian blur {data-auto-animate="true"}

![Mean and Gaussian blur](assets/plots3/cameraman_filtered.png)

## Image Smoothing

Smoothing effectively _low pass_ filters the image.

- Only really practical for small kernels
- Blurring also destroys image information
- Difference between the mean and Gaussian filter is subtle, but Gaussian is usually preferred

::: notes
Dampens high frequency information so that edges and noise are less prominent
:::

## Image Smoothing

If we have many images of the same scene:

- Use idea of averaging to reduce noise.
- Average pixel intensities across images rather than across the spatial neighbour.

## Image Smoothing

- Effectively increases the signal-to-noise ratio.
- Useful in applications where image signal is low.
  - E.g., imaging astronomical objects.

# Image Sharpening

---

What would the filtered image look like?

![kernel 4](assets/plots3/kernel4_q.png)

---

![kernel 4](assets/plots3/kernel4_a.png)

## Image Sharpening

We can control the _amount_ of sharpening:

$$
h_{sharp} =
\begin{bmatrix}
   0 & 0 & 0\\
   0 & 1 & 0\\
   0 & 0 & 0
\end{bmatrix}
+
\begin{bmatrix}
   0 & -1 & 0\\
   -1 & 4 & -1\\
   0 & -1 & 0
\end{bmatrix}
* amount
$$

::: notes
If anyone has ever developed film - similar to a high acutance developer formula...
:::

## More Kernel Examples

There is a nice interactive tool to view kernel operations here:
[https://setosa.io/ev/image-kernels/](https://setosa.io/ev/image-kernels/)

The ImageMagick documentation has a nice list of kernels:
[https://legacy.imagemagick.org/Usage/convolve/](https://legacy.imagemagick.org/Usage/convolve/)

## Unsharp Masking

A _high pass_ filter formed from a _low pass_ filtered image.

- Usually preferred over kernel sharpening filter.
- A legacy of the pre-digital period.

## Unsharp Masking

Low pass filter removes high-frequency detail.

::: incremental

- Difference between original and filtered images is what the filter removed.
  - high frequency information.
- Add difference to original image to enhance edges, etc.

:::

::: notes
Known as unsharp masking.
:::

## Unsharp Masking

![Unsharp masking 7x7 Gaussian kernel](assets/plots3/unsharp_diff.png)

::: notes
The difference image is the unsharp mask!
:::

## Unsharp Masking

The **sharpened** image is the original image plus the _unsharp mask_ multiplied by some factor.

- The difference image is the unsharp mask!

## Unsharp Masking

![Unsharp masking 2D and 5D](assets/plots3/unsharp_mask7x7.png)

## Unsharp Masking

![Unsharp masking 11x11 Gaussian kernel](assets/plots3/unsharp_diff_11x11.png)

## Unsharp Masking

![Unsharp masking 2D and 5D](assets/plots3/unsharp_mask11x11.png)

## Unsharp Masking

Generally don’t want to boost all fine detail as noise would also be enhanced.

- Adjust the Gaussian parameters.
- Threshold the difference image.
- Care is required to avoid artefacts (e.g. halos).

# Image Filters as Templates {data-auto-animate="true"}

2D Convolution can be thought of as comparing a little picture (the filter kernel) against all local regions in the image.

## Image Filters as Templates {data-auto-animate="true"}

If the filter kernel contains a picture of something you want to locate inside the image (a template), the filter response should be maximised at the local region that most closely matches it.

- We can use image filtering for object location
- Known as Template Matching.

## Image Filters as Templates {data-auto-animate="true"}

Algorithm:

- subtract the mean from the image and template
- convolve the template with the image
- find the location of the maximum response

## Image Filters as Templates {data-auto-animate="true"}

![Select a region to form a template.](assets/plots3/template_region.png)

::: notes
The region must be rotated for a convolution operation.
:::

## Image Filters as Templates {data-auto-animate="true"}

![Perform the convolution operation.](assets/plots3/template_response.png)

::: notes
The region must be rotated for a convolution operation.
:::

## Image Filters as Templates {data-auto-animate="true"}

![Locate the maximum filter response.](assets/plots3/template_max.png)

::: notes
This is the highest pixel value in the output image.
:::

# Summary

- 2D Convolutions
- Smoothing Filters
- Sharpening and Unsharp masking
- Template matching
