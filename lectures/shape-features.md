---
title: Lip Reading with Shape Features
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

## Acoustic Speech Recognition

$$ P(W | Y) = \frac{P(Y | W) P(W)}{P(Y) } $$

::: notes
Probability of a word sequence W given an acoustic observation Y
:::

## Acoustic Speech Recognition

Learn the parametric model from training data, and use to estimate the probabilities.

## Acoustic Speech Recognition

![](assets/img2/speech-recognition-01.png)

## Visual Speech Recognition

![](assets/img2/speech-recognition-02.png)

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
An investigation of HMM classifier combination strategies for improved audio-visual speech recognition. Lucey et al. 2001
</cite>

## Late Integration

![](assets/img2/speech-recognition-03.png)

::: notes
Late Integration
:::

## Early Integration

Concatenate the acoustic and visual models to form a single model.

Visual features often need interpolation to align with the acoustic features.

## Early Integration

![](assets/img2/speech-recognition-04.png)

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
![](assets/img2/roi-01.jpg)
:::::

::::: column
For any form of visual feature extraction, some form of localisation is required.
:::::

:::

## Region of Interest (ROI) {data-auto-animate="true"}

::: columns

::::: column
![](assets/img2/roi-02.jpg)
:::::

::::: column
Where in the image is the face?
:::::

:::

## Region of Interest (ROI) {data-auto-animate="true"}

::: columns

::::: column
![](assets/img2/roi-03.jpg)
:::::

::::: column
Where are the facial features of interest?
:::::

:::

## Region of Interest (ROI) {data-auto-animate="true"}

::: columns

::::: column
![](assets/img2/roi-04.jpg)
:::::

::::: column
MATLAB has an implementation of the Viola Jones face tracker.
:::::

:::
