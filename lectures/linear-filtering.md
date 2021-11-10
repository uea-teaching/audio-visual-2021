---
title: Linear Image Filtering
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
date: \today
---

# Content

- 2D Convolutions
- Smoothing Filter
- Sharpening and Unsharp Masking
- Template Matching

## What is Image Filtering? {data-auto-animate="true"}

Filtering replaces each pixel with a value based on some function performed on it’s local neighbourhood.

## What is Image Filtering? {data-auto-animate="true"}

Used for smoothing and sharpening.

IMAGE HERE

## What is Image Filtering? {data-auto-animate="true"}

Estimating gradients.

IMAGE HERE

## What is Image Filtering? {data-auto-animate="true"}

Removing noise.

IMAGE HERE

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

## Convolution

Kernel matrix coordinate origin is in the _centre_.

![](assets/plots3/kernel_coords.png)

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

![](assets/plots3/kernel_11_00.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_11_01.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_11_02.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_11_03.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_11_04.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_11_all.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_11_g11.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_12_g12.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_13_g13.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_21_g21.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_28_g28.png)

## Convolution {data-auto-animate="true"}

![](assets/plots3/kernel_88_g88.png)

## Images Edges

![](assets/plots3/conv_edge_00.png){width=55%}

## More Kernel Examples

There is a nice interactive tool to view kernel operations here:
[https://setosa.io/ev/image-kernels/](https://setosa.io/ev/image-kernels/)
