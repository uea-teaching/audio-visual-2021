---
title: Shape Features
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
date: \today
---

# Content

- Speech recognition models
- Visual Features
- Image segmentation
- Point distribution models
- Fourier descriptors

# Speech Recognition Models

## Acoustic Speech Recognition

The task of a speech recogniser is to determine the most likely word sequence given a new sequence of (acoustic) feature vectors.

::: notes
Lets just remind ourselves about the acoustic speech recognition process...
:::

## Acoustic Speech Recognition

An elegant way to compute this is using hidden Markov models.

$$ P(W | Y) = \frac{P(Y | W) P(W)}{P(Y) } $$

::: notes
Probability of a word sequence W given an acoustic observation Y
:::

## Acoustic Speech Recognition

Learn the parametric model from training data, and use to estimate the probabilities.

## Acoustic Speech Recognition

![](assets/img3/speech-recognition-01.png)

## Visual Speech Recognition

![](assets/img3/speech-recognition-02.png)

::: notes
Probability of a word sequence W given an visual observation V
:::

## Audio-Visual Speech Recognition

Combine two modalities using:

- Late Integration
- Early Integration

## Late Integration

Late integration builds two separate models and weights their
probabilities to provide the recognised word sequence.

## Late Integration

Has been shown to offer better performance than early integration.

Not straightforward to weight output probabilities.

<cite> 
An investigation of HMM classifier combination strategies for improved audio-visual speech recognition.</br>
Lucey et al. 2001
</cite>

## Late Integration

![](assets/img3/speech-recognition-03.png)

::: notes
Late Integration
:::

## Early Integration

Concatenate the acoustic and visual models to form a single model.

Visual features often need **interpolation** to align with the acoustic features.

## Early Integration

![](assets/img3/speech-recognition-04.png)

::: notes
Early Integration
:::

# Visual Features

## Visual Features

MFCCs are the standard features used in acoustic speech recognition.

- What is the equivalent for visual speech?
- In short: there is little agreement!

## Visual Features

Typical features include:

- Shape-based features
- Appearance-based features
- Hybrid features

## Region of Interest (ROI) {data-auto-animate="true"}

::: columns

::::: column
![](assets/img3/roi-01.jpg)
:::::

::::: column
For any form of visual feature extraction, some form of localisation is required.
:::::

:::

## Region of Interest (ROI) {data-auto-animate="true"}

::: columns

::::: column
![](assets/img3/roi-02.jpg)
:::::

::::: column
Where in the image is the face?
:::::

:::

## Region of Interest (ROI) {data-auto-animate="true"}

::: columns

::::: column
![](assets/img3/roi-03.jpg)
:::::

::::: column
Where are the facial features of interest?
:::::

:::

## Region of Interest (ROI) {data-auto-animate="true"}

::: columns

::::: column
![](assets/img3/roi-04.jpg)
:::::

::::: column
MATLAB has an implementation of the Viola Jones face tracker.
:::::

:::

# Shape Features

## Shape Features for Recognition

Shape features _might_ include:

- Articulatory-based features, such as mouth height and width
- Point distribution model (and related features)
- Fourier descriptors

## Shape Features for Recognition

There is a trade-off between ease of extraction and the amount of information extracted.

- Sparse point sets are easier to locate, but capture less information
- Denser point sets are information rich, but require a more sophisticated capture process

## Representing Shapes

We need a method for describing specific shapes in images.

## Representing Shapes

::: columns
::::: column
![](assets/plots2/cameraman-canny.png)
:::::
::::: column
An edge detector will locate edges in an image.
:::::
:::

## Representing Shapes

::: columns
::::: column
![](assets/plots2/cameraman-canny.png)
:::::
::::: column
Which belong to the object of interest?

How are these allowed to vary as the object deforms?
:::::
:::

## Representing Shapes

::: columns
::::: column
![](assets/plots2/cameraman-canny.png)
:::::
::::: column

### Idea

Can we represent shapes using the image coordinates of the edge pixels?

:::::
:::

## Representing Shapes

We could, but the same shape in two locations will have different coordinates.

The coordinates describe the shape in the image coordinate frame, so they encode the shape **and the location** of the shape.

## Representing Shapes

We are not interested in **where** the shape is ??? just the shape itself.

- A lip-reading system might use the shape of the lips to recognise speech, but it should not matter where in the image the lips are.

## Representing Shapes

The primary problem is how to segment the lips from the background to extract a representation of the shape that is independent of image location.

A pre-processing stage of feature extraction identifies the region of the image that corresponds to the mouth.

This results in a binary mask, which is 1 if a pixel represents the mouth and 0 otherwise.

# Image Segmentation

The goal of image segmentation is to classify each pixel as being either foreground or background.

::: notes
mouth is foreground for us
:::

## Image Segmentation

We require three things:

1. A property that we can measure from the image pixels (e.g. colour).
2. A distance measure that defines how close two pixels are given that property.
3. A classifier that can discriminate one class from another using that distance.

## Image Segmentation

::: columns
::::: column
Which colour-space should be used?
:::::
::::: column
![RGB](assets/plots2/barry-rgb.png)
:::::
:::

## Image Segmentation

::: columns
::::: column
![Normalised RGB](assets/plots2/norm-rgb.png)
:::::
::::: column
![RGB](assets/plots2/barry-rgb.png)
:::::
:::

## Image Segmentation

::: columns
::::: column
![Normalised RGB](assets/plots2/norm-rgb.png)

:::::
::::: column

$$I = \left[\frac{r}{r+b+g} \frac{g}{r+b+g} \frac{b}{r+b+g}\right]$$

- A colour is represented by its proportion of red, green and blue, not the intensity of each.
- Reduces distortions caused by lights and shadows in an image.

:::::
:::

## Image Segmentation

::: columns
::::: column
![Normalised RGB](assets/plots2/norm-rgb-rect.png)
:::::
::::: column

What colour do we want to segment out?

:::::
:::

## Image Segmentation

::: columns
::::: column
![Normalised RGB](assets/plots2/norm-rgb-rect.png)
:::::
::::: column

Find the mean colour of a lip pixel:

$$\begin{bmatrix} \mu_{r} \\ \mu_{g} \\ \mu_{b} \end{bmatrix} = \mu_{c}$$

:::::
:::

## Image Segmentation {data-auto-animate="true"}

Find the Euclidean distance between each pixel in the image, $~I_{i, j}$, and the mean lip pixel colour $\mu_{c}$.

$$D_{i, j} = \sqrt{\sum{(I_{i, j} -  \mu_{c})^2}}$$

::: notes
The Euclidean distance between colour at row i, column j and the mean lip colour.
:::

## Image Segmentation {data-auto-animate="true"}

$$D_{i, j} = \sqrt{\sum{(I_{i, j} -  \mu_{c})^2}}$$

A better distance metric might consider the variance of the lip pixels rather
than just the mean, e.g. _Mahalanobis_ distance.

::: notes
The Euclidean distance between colour at row i, column j and the mean lip colour.
:::

## Image Segmentation

Threshold the distance to segment lips from the background.

$$T_{i, j} = \begin{cases}1 ~ if ~ D_{i, j} < \tau \\ 0 ~ otherwise \end{cases}$$

## Image Segmentation

::: columns
::::: column
![Normalised RGB](assets/plots2/norm-rgb.png)
:::::
::::: column
![Threshold Image](assets/plots2/norm-rgb-threshold.png)
:::::
:::

## Image Segmentation

- This approach assumes that there is nothing in the image that is the same colour as the lips, otherwise there is nothing to tell these regions apart.

- Often do other pre-processing (e.g. Viola-Jones face detector) first.

## Image Segmentation

- Need to set the threshold, which itself is not trivial.
- If the threshold is too low, lip pixels will be missing.
- If the threshold is too high, background will be accepted as foreground.

## Image Segmentation

The matte will still contain spurious pixels, which might need cleaning up using **morphological** filtering.

## Image Segmentation

- From the resultant binary mask, the relevant features still need to be extracted.
  - e.g. articulatory-based features...

## Articulatory-based Features

::: columns
::::: column
![Threshold Image](assets/plots2/artic-features.png)
:::::
::::: column

From the binary image we can extract features such as:

- the height and width of the mouth region
- the number of pixels within the mouth region
- the mouth centroid

:::::
:::

## Image Segmentation

Automated approaches are attractive as there is no manual effort. However:

- The colour of the lips is often similar to the surrounding skin.
- Noise is an issue.
- The facial appearance can change over time (e.g. beard growth, etc.).

## Image Segmentation

Semi-automated approaches are generally more robust.

- They might need significant effort to reliably construct the model.
- But priors can be imposed on the expected shape.

# Point Distribution Models

## Point Distribution Models {data-auto-animate="true"}

A _generative_ statistical model of the variation of the shape of an object.

## Point Distribution Models {data-auto-animate="true"}

Use **Principal Component Analysis (PCA)** to model the variation in the coordinates of a set of _landmark_ points.

The PDM can represent complex shapes with just a few parameters.

## Point Distribution Models {data-auto-animate="true"}

You can use an _Active Shape Model (ASM) _ or _Active Appearance Model (AAM)_ to automatically locate the landmarks (facial tracking).

This model **requires training**.

## Point Distribution Models {data-auto-animate="true"}

::: columns
::::: column
![](assets/img3/aj_sample_05.jpg)
:::::
::::: column

A **shape** is represented by a set of **landmarks** located along the shape boundary.

:::::
:::

## Point Distribution Models {data-auto-animate="true"}

::: columns
::::: column
![](assets/img3/aj_sample_05.jpg)
:::::
::::: column

- The landmarks must be easy to locate from one image to another.
- T-junctions, points of high curvature, corners etc. form good candidates.
- Include evenly spaced intermediate points along the boundary.

:::::
:::

## Point Distribution Models {data-auto-animate="true"}

::: columns
::::: column
![](assets/img3/aj_sample_05.jpg)
:::::
::::: column

I provide a tool to annotate landmarks here:
[https://github.com/davegreenwood/face-landmark-tool](https://github.com/davegreenwood/face-landmark-tool)

:::::
:::

## Point Distribution Models {data-auto-animate="true"}

![](assets/img3/comb-lm.jpg)

Manually hand label a selection of images from a training set.

All examples _must_ have the **same number** of landmarks and be labelled in the **same order**.

## Point Distribution Models {data-auto-animate="true"}

![](assets/img3/comb-lm.jpg)

Sufficient images must be labelled to capture the expected range of variation.

- Capture large facial expressions, wide mouths, etc.
- Typically need 20 - 30 images per person.

## Point Distribution Models {data-auto-animate="true"}

A shape is the concatenation of the $x$ and $y$ coordinates of the landmarks:

$$X = \{x_1, x_2, \dots, x_n, y_1, y_2, \dots, y_n\}^T $$

The consistency in the labelling ensures the elements of these vectors have the same meaning.

## Point Distribution Models

::: columns
::::: column
![](assets/img3/multi-lm.png)
:::::
::::: column

The coordinates describe the shape in the image coordinate frame.

The same shape at different locations results in a different shape vector.

:::::
:::

## Point Distribution Models

::: columns
::::: column
![](assets/img3/multi-lm.png)
:::::
::::: column

We need to normalise shapes for translation, scale and rotation.
This can be done using **Procrustes analysis**.

:::::
:::

## _Aside:_ Procrustes analysis

::: columns
::::: column
![captured landmarks](assets/img3/multi-lm.png)
:::::
::::: column
![aligned landmarks](assets/img3/multi-lm-aligned.png)
:::::
:::

## Point Distribution Models

Given the aligned shapes, compute a model that describes the variation in shape.

A linear model of the variation can be found using **Principal Components Analysis (PCA)**.

## Point Distribution Models

The model is in the form:

$$x = \overline x + \mathbf{P}_{s} \mathbf{b}_{s}$$

where $x$ is a shape, $\overline x$ is the _mean_ shape, the matrix $\mathbf{P}_{s}$ describes
the variation in shape, and $\mathbf{b}_{s}$ are the **parameters** that represent a shape instance.

## _Aside:_ Principal Component Analysis (PCA)

::: incremental

- Reveals the internal structure of the data in a way that best _explains the variance_ in the data.
- Used for dimensionality reduction.
- Reduces data down into its basic components, stripping away any unnecessary parts.

:::

::: notes
PCA was invented in 1901 by Karl Pearson, as an analogue of the principal axis theorem in mechanics;
:::

## _Aside:_ Principal Component Analysis (PCA)

::: incremental

- Assume we have 2-dimensional measurements.
  e.g. the height and foot size for a number of people
- We expect the measurements to be correlated to some degree.
  e.g. taller people tend to have larger feet
- Visualise the data by plotting one measure against the other.

:::

---

![](assets/plots2/pca_01.png){width=85%}

## _Aside:_ Principal Component Analysis (PCA)

The objective of PCA is to capture as much of the variation in as few dimensions as possible.

Find line of "best fit" through the data, then line of "next best fit" which is _orthogonal_ to the first...

Repeat for however many dimensions your data has

---

![](assets/plots2/pca_02.png){width=85%}

---

![](assets/plots2/pca_03.png){width=85%}

## _Aside:_ Principal Component Analysis (PCA)

Since the dimensions must be orthogonal, all we have done is rotate the axes to better align with the data.

In doing this:

- P1 captures most of the meaningful variation
- P2 seems to capture the noise in the measurements

The original data can be approximated as some distance along P1 from the centre of the data cloud.

---

![](assets/plots2/pca_04.png){width=85%}

---

![](assets/plots2/pca_05.png){width=85%}

---

![](assets/plots2/pca_06.png){width=85%}

---

![](assets/plots2/pca_07.png){width=85%}

## _Aside:_ Principal Component Analysis (PCA)

To project a data point onto a new axis:

$$\mathbf{b}_{s}  = \mathbf{P}_{s}^{T}  (x - \overline x )$$

## _Aside:_ Principal Component Analysis (PCA)

To reconstruct the data point from the features:

$$x \approx \overline x + \mathbf{P}_{s} \mathbf{b}_{s}$$

This is only an approximation since the data are truncated to lie on just the principal component(s).

## _Aside:_ Principal Component Analysis (PCA)

Note, in the previous example we have moved from a 2D problem to 1D so the representation is more compact.

Staying within the limits of the data means new examples can be generated ??? this is a **generative** model.

## _Aside:_ Principal Component Analysis (PCA) {data-auto-animate="true"}

Algorithm:

- Compute the mean of the data and subtract.
- Compute the covariance matrix.
- Compute the eigenvectors and eigenvalues of the covariance matrix and sort into descending order of eigenvalue.

## _Aside:_ Principal Component Analysis (PCA) {data-auto-animate="true"}

- Eigenvectors are the principal components.
- Eigenvalues are the variance explained by each principal component.
- We typically retain the number of eigenvectors that describe 95% of the total variation in the data.

## _Aside:_ Principal Component Analysis (PCA) {data-auto-animate="true"}

Matlab has implementations of both PCA and of Eigenvector/Eigenvalue decomposition.

## Point Distribution Models

For modelling shapes, an n-point shape is represented as a 2n element vector:

$$X = \{x_1, x_2, \dots, x_n, y_1, y_2, \dots, y_n \}^{T}$$

Can be thought of as a single point in a $\mathbb{R}^{2n}$ space.

## Point Distribution Models

PCA can be applied to the $\mathbb{R}^{2n}$ data, rotating the $2n$ axes to
best fit to the data cloud in $\mathbb{R}^{2n}$ space.

We retain only the meaningful variation - often resulting in considerable compression.

## Point Distribution Models

![](assets/plots2/pca_mouth.png)

::: notes
Here, the original data is 20 x 2D points.
We can express the mouth shapes with only 3 values.
:::

## Fitting a PDM

Given a PDM, and a new image, how do we fit the PDM to the facial pose in the new image?

- Sample the pixels around each landmark in the training set, and look for the
  region in the image that best matches the sample.

- Refine the fit by forcing the shape to lie within the model space.

- More efficient if provided an approximate starting point.

- Further reading: [Active Shape Models](http://personalpages.manchester.ac.uk/staff/timothy.f.cootes/papers/asm_overview.pdf)

::: notes

There is a lot to model-fitting and optimisation.
Too much to cover in one slide...
Gradient descent is a good start.
Creating an Active Appearance Model (AAM) would be great.

:::

# Fourier Descriptors of Shape

## Fourier Descriptors

The lip boundary provides a closed contour.

- Normalise the length to $2 \pi$ units.
- Measure the distance from the centroid to the contour at regular intervals
  to calculate a **Centroid Contour Distance Curve**.
- The curve is _periodic_ with period $2 \pi$, and it is real, continuous.

## Fourier Descriptors

![](assets/plots2/fourier_descriptors.gif)

## Fourier Descriptors

The curve can be decomposed into a **Fourier** series (refer back to the audio processing slides).

## Fourier Descriptors

- The coefficients of the series provide the visual features
- This requires an accurate and complete estimate of the lip-contour.
- The coefficients do not have direct physical meaning.

::: notes
you could get the lip contour from tracking or thresholding.
:::

# Summary

- Visual Features
- Image segmentation
- Point distribution models and PCA
- Fourier descriptors
