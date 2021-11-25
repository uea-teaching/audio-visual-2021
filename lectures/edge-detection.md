---
title: Edge Detection
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
date: December 1, 2021
---

# Content

- Edges from image derivatives
- Laplacian matrices
- Line detection operators
- Canny edge detector

# Edges

An edge in an image is a significant local change or discontinuity in the image intensity.

## Edges {data-auto-animate="true"}

::: columns
::::: column
![](assets/plots4/coins_fig.png)
:::::
::::: column

An image is a 2D matrix of intensities.

:::::
:::

## Edges {data-auto-animate="true"}

::: columns
::::: column
![](assets/plots4/coins_row.png)
:::::
::::: column

We can look at those intensities in a single row.

:::::
:::

## Edges {data-auto-animate="true"}

::: columns
::::: column
![](assets/plots4/coins_row.png)
:::::

::::: column

We can see how edges are defined by these changes in intensity.

:::::
:::

## Image Derivatives {data-auto-animate="true"}

The derivative is the rate of change of a function.

- 1D first order derivative: **difference** in consecutive pixels:
  $$\frac{\delta f}{\delta x} \approx f(x + 1) - f(x)$$

- 1D second order derivative: **acceleration** of pixel intensity change:
  $$\frac{\delta^{2}f}{\delta {x}^2} \approx f(x + 1) + f(x - 1) - 2f(x)$$

::: notes
the x is the location along the line of the pixel -
The first derivative, in 1D, can be thought of as a tangent - wth a slope - or gradient.
We used a partial derivative here in order to keep the notation consistent when we consider an image function of two variables.
:::

---

![Example from Gonzalez and Woods.](assets/img4/ramps.png){width=80%}

::: notes

It might be helpful to look at some specific values as a concrete example.

:::

---

## Image Derivatives {data-auto-animate="true"}

Required properties of first derivatives:

::: incremental

- Zero in regions of constant intensity
- Non-zero at onset of a ramp or step
- Non-zero along intensity ramps

:::

::: notes
Derivatives of a digital function are defined in terms of differences. There are various ways to define these differences. However, we require that any definition we use for a derivative has these properties.
:::

## Image Derivatives {data-auto-animate="true"}

Required properties of second derivatives:

::: incremental

- Zero in regions of constant intensity
- Non-zero at the onset **and** end of an intensity step or ramp.
- _Zero_ along intensity ramps.

:::

::: notes
Going back to our row of pixels, we can see how some real data looks.
:::

---

![Intensity, first and second derivatives](assets/plots4/coins_derivatives.png)

## Image Derivatives {data-auto-animate="true"}

For images, we must consider the derivative in both directions:

$$\frac{\delta f}{\delta x} \approx f(x + 1, y) - f(x, y)$$

$$\frac{\delta f}{\delta y} \approx f(x, y + 1) - f(x, y)$$

::: notes
We used a partial derivative here in order to keep the notation consistent when we consider an image function of two variables.
:::

## Image Derivatives {data-auto-animate="true"}

![x and y first derivatives](assets/plots4/cameraman_derivatives.png)

## Image Derivatives {data-auto-animate="true"}

An image _gradient_ is formed of two components:

$$\nabla f = \left[ \frac{\delta f}{\delta x}, \frac{\delta f}{\delta y} \right]$$

::: notes
The first derivative, in 1D, can be thought of as a tangent - wth a slope - or gradient.
:::

## Image Derivatives {data-auto-animate="true"}

Image gradient is a vector:

$$\nabla f = \left[ \frac{\delta f}{\delta x}, \frac{\delta f}{\delta y} \right]$$

## Image Derivatives {data-auto-animate="true"}

A vector has magnitude...

$$|\nabla f| = \sqrt{\left( \frac{\delta f}{\delta x} \right)^{2} + \left( \frac{\delta f}{\delta y} \right)^{2}}$$

Magnitude is the _strength_ of the edge.

## Image Derivatives {data-auto-animate="true"}

A vector has direction...

$$ \theta = \tan^{-1} \left( \frac{\delta f}{\delta x} / \frac{\delta f}{\delta y} \right) $$

Direction of an edge is **perpendicular** to the gradient direction.

## Image Derivatives {data-auto-animate="true"}

::: columns
::::: column
![gradient direction](assets/img4/gradient.png)
:::::
::::: column

::: incremental

- The gradient points in the direction of most rapid change in intensity.
- **Perpendicular** to the edge direction.

:::

:::::
:::

## Image Derivatives {data-auto-animate="true"}

![gradient magnitude as greyscale](assets/plots4/cameraman_mag.png){width=50%}

## Image Derivatives {data-auto-animate="true"}

First order derivatives:

::: incremental

- produce thicker edges in images
- have a stronger response to stepped intensity changes

:::

## Second Order Derivatives {data-auto-animate="true"}

Second order derivatives:

::: incremental

- have a stronger response to fine detail
- are more aggressive at enhancing detail
- Generally, second-order derivatives are _preferred._

:::

## Second Order Derivatives {data-auto-animate="true"}

$$\nabla^{2} f = \frac{\delta^{2} f}{\delta x^{2}} + \frac{\delta^{2} f}{\delta y^{2}}$$

Derivative in this form is known as the **Laplacian**.

::: notes
Derived by computing 2nd order derivatives in each direction and then summing.
:::

# Laplacian {data-auto-animate="true"}

We know:

$$\frac{\delta^{2}f}{\delta {x}^2} \approx f(x + 1) + f(x - 1) - 2f(x)$$

$$\frac{\delta^{2}f}{\delta {y}^2} \approx f(y + 1) + f(y - 1) - 2f(y)$$

## Laplacian {data-auto-animate="true"}

So, the Laplacian is calculated as:

$$\nabla^{2} f = f(x + 1) + f(x - 1) + f(y + 1) + f(y - 1) - 4f(x, y)$$

::: notes
summing the two second order derivatives in each direction.
:::

## Laplacian {data-auto-animate="true"}

$$
\begin{bmatrix}
  0 & 1 & 0 \\
  1 & -4 & 1 \\
  0 & 1 & 0
\end{bmatrix}
$$

The Laplacian can also be calculated by **convolving** the image with this filter.

## Laplacian {data-auto-animate="true"}

![Laplacian](assets/plots4/cameraman_laplacian.png)

## Laplacian {data-auto-animate="true"}

![Gradient magnitude and Laplacian](assets/plots4/mag_grad_laplacian.png)

::: notes
I hope you will agree that the first order derivatives produce thicker edges.
:::

# Line Detection {data-auto-animate="true"}

The Laplacian responds strongly to _any_ detail in the image.

## Line Detection {data-auto-animate="true"}

What if we only wanted to detect lines that point in a certain direction?

$$
\begin{bmatrix}
  -1 & 2 & -1 \\
  -1 & 2 & -1 \\
  -1 & 2 & -1
\end{bmatrix}
$$

## Line Detection {data-auto-animate="true"}

![Line Detection](assets/plots4/laplacian_vert_lines.png)

## Line Detection {data-auto-animate="true"}

What about detecting edges in other directions?

![Line directions](assets/plots4/directions.png)

## Line Detection {data-auto-animate="true"}

What about detecting edges in other directions?

![Line directions](assets/plots4/four_directions.png)

## Line Detection {data-auto-animate="true"}

Previous filter gives strong response along a line.

::: incremental

- **But...** also responds at isolated pixels.
- Edge detector should respond only to edges

:::

## Line Detection {data-auto-animate="true"}

Look either side of candidate pixel...

::: incremental

- but ignore the pixel itself.

:::

## Line Detection {data-auto-animate="true"}

Two popular _first-order_ operators are **Prewitt** and **Sobel**.

Both provide approximations of derivatives.

## Line Detection {data-auto-animate="true"}

![ Prewitt, J.M.S. (1970). "Object Enhancement and Extraction"](assets/plots4/prewitts.png)

## Line Detection {data-auto-animate="true"}

![Prewitt responses](assets/plots4/cameraman_prewitts.png)

## Line Detection {data-auto-animate="true"}

![Sobel, I. (1968) "An Isotropic 3x3 Image Gradient Operator"](assets/plots4/sobels.png)

::: notes
Described in a talk, at the Stanford Artificial Intelligence Project, published rather later.
:::

## Line Detection {data-auto-animate="true"}

![Sobel responses](assets/plots4/cameraman_sobels.png)

::: notes
Described in a talk, at the Stanford Artificial Intelligence Project, published rather later.
:::

---

For each pixel, find the maximum value from all of the filter responses, and then threshold.

![Sobel maximum](assets/plots4/sobel_threshold.png)

::: notes
So, to turn back to detection of edges, we take the max of each directional response, and threshold, maybe 200 for 8 bit images.
:::

## Edge Detection {data-auto-animate="true"}

We rarely observe ideal edges in real images.

::: incremental

- Lens imperfections, sensor noise, etc.
- Edges appear more like noisy gradients

:::

::: notes
These issues present problems for gradient-based edge detection.
:::

## Edge Detection {data-auto-animate="true"}

Four limitations with basic gradient-based edge detection:

::: incremental

- Hard to set the optimal value for the threshold.
- Edges are broken (known as streaking)
- Edges can be poorly localised
- An edge might produce more than one response

:::

# Canny Edge Detector{data-auto-animate="true"}

The **Canny Edge Detector** is _optimal_ with respect to gradient-based limitations.

## Canny Edge Detector

Requirements for a _good_ edge detector:

::: incremental

- Good detection - respond to edges, not noise.
- Good localisation - detected edge near real edge.
- Single response - only one response per edge.

:::

## Canny Edge Detector

Canny provides an elegant solution to edge detection.

::: incremental

- Canny provides a _hacky_ solution to edge detection!

:::

## Canny Edge Detector

1. Convolve image with Gaussians of particular scales.
2. Compute gradient magnitude and direction.
3. Perform **non-maximal** suppression to thin the edges.
4. Threshold edges with **hysteresis**.

::: notes

Smooth the image using a Gaussian with sigma width.

Apply the horizontal and vertical Sobel operators to get the gradients within the image. The edge strength is the norm of the gradient.

Thin potential edges to 1-pixel wide curves. First, find the normal to the edge at each point. This is done by looking at the signs and the relative magnitude of the X-Sobel and Y-Sobel to sort the points into 4 categories: horizontal, vertical, diagonal and antidiagonal. Then look in the normal and reverse directions to see if the values in either of those directions are greater than the point in question. Use interpolation to get a mix of points instead of picking the one that’s the closest to the normal.

Perform a hysteresis thresholding: first label all points above the high threshold as edges. Then recursively label any point above the low threshold that is 8-connected to a labeled point as an edge.

:::
