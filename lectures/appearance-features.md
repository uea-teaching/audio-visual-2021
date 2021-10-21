---
title: Lip Reading with Appearance Features
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
date: \today
---

# Content

- DCT Features
- Eigen Faces
- Appearance Models
- Visual Feature Efficacy

## Image-based Features

The main limitation of shape-only features is there is a lot of information missing.

::: incremental

- Modelling only lip-shape discards information about the teeth and tongue for example.
- Why not use the full _appearance_ of the face?

:::

# DCT Features

## Discrete Cosine Transform (DCT)

Performs a similar function to DFT in that it transforms a signal (or image) from the spatial domain to the frequency domain.

- The difference is that it only considers the real-valued cosine components of the DFT.
- We can compact the energy of the signal into the low frequency bins.
- Used in JPEG compression.
- First proposed by Nasir Ahmed in 1972.

## Review: DFT

![Lecture 2, Slide 13: Fourier Transform](assets/img4/lecture_02_slide_13.png){width=80%}

## DCT 1D

$$
X_k = s(k) ~ \sum_{n=0}^{N-1} x_n
cos \left[ \frac{\pi k (2n + 1)}{2N} \right]
$$

Where:

- $X$ is the DCT output
- $x$ is the input signal
- $N$ is the number of samples
- $k = 0, 1, 2, \dots, N-1$
- $s(0) = \sqrt{1/N}, ~ s(k \neq 0) = \sqrt{2/N}$

::: notes
MATLAB has the dct function
:::

---

### 8-Point 1-D DCT Basis

::: columns
::::: column
![](assets/plots2/basis_vectors_1d.png)

:::::
::::: column

$$Y_k = cos \left[ \frac{\pi k (2n + 1)}{2N} \right]$$

$$n = 1, 2, \dots, N-1$$

:::::
:::

## DCT for 1D Signals

Let's look at one 8 x 8 block in an image.

![](assets/plots2/cameraman_block.png)

---

![DCT of each row of the image block](assets/plots2/dct_8x8_block.png)

## DCT for 1D Signals

![](assets/plots2/block_row3.png)

::: {.incremental}

- Most of the energy is concentrated in the low frequency coefficients.
- Images have less high frequency information.

:::

## DCT for 2D Signals

We have only considered vectors so far.

- Images are 2-dimensional (two spatial co-ordinates).
- Apply DCT to both rows and columns of the image.

$$
X_{u, v} = s_u s_v ~ \sum_{x=0}^{N-1} \sum_{y=0}^{N-1} I(x, y) ~
    cos \left[ \frac{\pi u (2x + 1)}{2N} \right]
    cos \left[ \frac{\pi v (2y + 1)}{2N} \right]
$$

## DCT for 2D Signals

::: columns
::::: column

![](assets/img4/DCT_2D_8x8.png)

:::::
::::: column

Rather than basis vectors, we have basis images.

:::::
:::

## DCT for 2D Signals

Let's look again at the same 8 x 8 block in an image.

![](assets/plots2/cameraman_block.png)

## DCT for 2D Signals

Here is the 2D DCT of the block.

![](assets/plots2/dct_2d_block.png)

## DCT for 2D Signals

::: columns
::::: column

![](assets/plots2/dct_2d_values.png)

:::::
::::: column

Let's examine the actual values of the coefficients.

:::::
:::

## DCT for 2D Signals

::: columns
::::: column

![](assets/plots2/dct_2d_values_high.png)

:::::
::::: column

Notice that the most significant values congregate at the top left.

:::::
:::

## DCT for 2D Signals

::: columns
::::: column

![](assets/plots2/dct_2d_values_high.png)

:::::
::::: column

We can stack the top left values to make a feature vector.

$f = (972, 85, 19, -59, \dots)$

:::::
:::

## DCT for 2D Signals

::: columns
::::: column

![](assets/plots2/dct_2d_values_low.png)

:::::
::::: column

If we want to reconstruct the image using the inverse DCT, we can set the low values to zero to view the reconstruction loss.

:::::
:::

## 2D DCT case study

![](assets/plots2/resize_mouth.png)

## 2D DCT case study

![](assets/plots2/restored_mouth.png)
