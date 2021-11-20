---
title: |
  ![](uea-logo.jpg){width=2in}  
  Non-Linear Image Filters -- Lab Sheet
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
date: \today
---

# Aims and Objectives

This laboratory session will introduce non-linear filtering of images.
Prior to beginning this laboratory sheet, you are strongly encouraged to complete the previous laboratory sheets.
Be sure to complete all of the exercises, and try to understand the purpose
and result of each exercise rather than simply entering the Matlab commands provided.

## Exercise 1

In the lectures you saw that the median filter is extremely powerful for
removing image noise for certain types of noise model (e.g. Salt and Pepper noise).
Write a Matlab function that implements a 2D median filter for both grayscale
and colour images.
Compare your implementation with that of the Matlab filter `medfilt2`.

## Exercise 2

Using the `imnoise` function, degrade a number of test images and look at
the effect of the noise type and magnitude on the images. Determine which the
types of noise the median filter is effective against, and determine the
amount of noise that can be present before the filter begins to fail.
Can you think of a way of measuring how well the filter performs
such that you can compare the filters in a scientific way?

## Exercise 3

Construct a binary image that contains a number of white regions
against a black background (you may find the `roipoly` function useful).

## Exercise 4

The Image Processing toolbox provides tools for performing the
morphological operations of erosion, dilation, opening and closing
(in `imerode`, `imdilate`, `imopen` and `imclose` respectively).

Test the effect of these filters on your binary
image using an 11 by 11 square structuring element (use the `strel` function
for creating a structuring element).

## Exercise 5

Experiment with using different sized filters with different shaped
structuring elements, and compare the result.

## Exercise 6

Experiment with using combinations of morphological operations
for extracting the edges of the white regions in your image.
Try implementing the approaches shown in Figure[@fig:morph].

![Combining morphological operations for extracting the edges of a shape.](morph.pdf){#fig:morph width=90%}

## Exercise 7

Use the rest of the laboratory session to work with your own face dataset.
You can try using different techniques to begin working on visual
feature extraction for your coursework.
For instance, you might want to try thresholding your face
image to extract a binary image containing just the lip region (see previous lab).

From this you might try automatically measuring lip height and width.
Alternatively, you might try edge detection using morphological
operations on your binary image to locate the lip contours, and then use these
to extract $x, y$ landmarks.

Or, you might want to use a face detector to locate
a region of interest around the lips, and then encode this using 2D DCT or PCA.

Use this time to experiment with different feature extraction techniques,
and remember to ask for guidance from the associate tutors whenever you need it.
