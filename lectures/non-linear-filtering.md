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

##

Crop a part of a larger image to uses as an example.

![Cameraman crop](assets/plots3/region_8x8.png)

##

First, window a region of size 3x3:

![region window](assets/plots3/region_select.png)

##

Sort the intensities in the region:

![ordered values](assets/plots3/region_ordered.png)

##

Sort the intensities in the region, and select the middle value:

![median value](assets/plots3/region_median.png)

##

Max filter is similar to median filter, but selects the maximum value:

![maximum value](assets/plots3/region_max.png)

##

Min filter is again similar, but selects the minimum value:

![minimum value](assets/plots3/region_min.png)

##

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

::: notes
You might think that a gaussian blur would be a good alternative to a median filter.
Let's look closely at the difference between the two.
:::

## Noise removal {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/noise-01.png)
:::::
::::: column
If we consider this 5 pixel neighbourhood, what will the median filter do?
:::::
:::

## Noise removal {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/noise-02.png)
:::::
::::: column
The median filter removes spike noise.

::: incremental

- What will the gaussian filter do?

:::
:::::
:::

## Noise removal {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/noise-03.png)
:::::
::::: column
The Gaussian filter amplifies noise.
:::::
:::

# Morphological Filters

::: notes
One of the issues we will have to deal with is noise in binary images.
We could consider min and max filters for this - but I'd like to introduce morphological filters for that task.
:::

## Morphological Filters

Operation of the filter is characterised by mathematical morphology.

::: incremental

- Embedded in set theory.
- Useful for thickening and thinning edges and de-noising binary images

:::

::: notes
We will consider only binary images.
The notation gets messy beyond this!
:::

## Motivation

![Filtered Threshold Image](assets/plots3/coins_erosion.png)

::: notes
Useful for cleaning up binary images.
:::

## Morphological Filters

For binary images:

::: incremental

- White pixels (with intensity 1) can be considered elements in a set.
- Black pixels (with intensity 0) can be considered elements outside of the set.
- Morphological filters are essentially set operations.

:::

## Set Notation {data-auto-animate="true"}

$$\text{Let } A \text{ be a set in } \mathbb{Z}^{2}$$

the set of _all integers_ in 2 dimensions...

## Set Notation {data-auto-animate="true"}

$$ a \in A \text{ if } a = (x, y) \text{ is an element of set } A $$

this is the _element_ symbol...

## Set Notation {data-auto-animate="true"}

$$ a \notin A \text{ if } a \text{ is not in } A $$

_not_ in...

## Set Notation {data-auto-animate="true"}

$$ C = \{ w|w = -d, ~ for ~ d \in D \} $$

the set of all $w$ _such that_...

::: notes
The elements of C, are w, which are formed by multiplying the elements of set D by -1

Braces are used to delimit the contents of a set.

:::

## Set Notation {data-auto-animate="true"}

$$\emptyset \text{ is the empty set} $$

## Set Operations {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/set-01.png)
:::::
::::: column
Given two sets, A and B, the following can be defined:
:::::
:::

## Set Operations {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/set-02.png)
:::::
::::: column

$$C \subseteq B,  A \nsubseteq B$$

Subset: a set where all members belong to a given set.
:::::
:::

::: notes
C is a subset of B.
A is not a subset of B.
:::

## Set Operations {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/set-03.png)
:::::
::::: column

$$A \cup B$$

Union: all elements that are either in set A or set B.
:::::
:::

## Set Operations {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/set-04.png)
:::::
::::: column

$$A \cap B$$

Intersection: all elements that are common to both A and B.
:::::
:::

## Set Operations {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/set-05.png)
:::::
::::: column

$$A^{c} \{w|w ~\notin ~ A\}$$

Complement: the elements not contained in set A

:::::
:::

## Set Operations {data-auto-animate="true"}

::: columns
::::: column
![](assets/img4/set-06.png)
:::::
::::: column

$$A \setminus B = \{w|w ~\in ~ A,~ w ~\notin ~ B \}$$

Difference: the elements of set A that are not in set B

:::::
:::
::: notes
Sometimes the minus sign is used for set difference...
:::

# Structuring Element

A _binary_ image (or mask) that allows us to define neighbourhood structures.

## Structuring Element

::: incremental

- Can be different sizes: larger structuring elements produce a more extreme effect.
- Can be different shapes: common to use a disk or cross shape.
- Has a defined origin: usually at the centre.

:::

## Structuring Element

![](assets/img4/structuring-elements.png)

::: notes
bold indicates the origin
:::

# Morphological Operators

## Dilation

$$A \oplus B = \{ x, y| B_{x, y} \cap \neq \emptyset \} $$

Defines dilation of binary image $A$ by structuring element $B$

Calculate the binary **OR** of elements in $A$ masked by $B$
