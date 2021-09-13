---
title: Visual Speech
subtitle: Audiovisual Processing CMP-6026A
author: Dr. David Greenwood
institution: University of East Anglia
date: \today
section-titles: false
---

# Dr David Greenwood

david.greenwood@uea.ac.uk

SCI - 2.16a

# Content

- Speech Production
- Visual Speech
- Visemes
- Coarticulation

# Speech Production

## Speech Production {data-auto-animate="true"}

Speech can be regarded as a filtering process.

::: incremental

- Air is expelled from the lungs.
  - the excitation signal
- This air is forced through the vocal tract.
  - the filter
- The air exits via the nose and mouth.
  - the filtered signal

:::

## Speech Production {data-auto-animate="true"}

The filter response is determined by the vocal tract shape,
which is dependent on the position of the speech articulators.

::: incremental

- The filter is non-stationary since the response changes over time.
- Speech is time-varying in nature.

:::

---

An MRI of the vocal tract.

<video controls src="assets/mov/mri.mp4" width="40%"></video>

<cite> source: https://sail.usc.edu/span/gallery.html</cite>

# Visual Speech

## Visual Speech {data-auto-animate="true"}

::: columns
::::: column

<video controls width="400px"
data-src="assets/mov/Bog-AV-noise-m18dB-SNR-mask.mp4">
</video>

:::::
::::: column

<video controls width="400px"
data-src="assets/mov/Dog-AV-noise-m18dB-SNR-mask.mp4">
</video>

:::::
:::

Can you discriminate between "dog" and "bog", in noisy audio?

## Visual Speech {data-auto-animate="true"}

::: columns
::::: column

<video controls width="400px"
data-src="assets/mov/Bog-AV-noise-m18dB-SNR.mp4">
</video>

:::::
::::: column

<video controls width="400px"
data-src="assets/mov/Dog-AV-noise-m18dB-SNR.mp4">
</video>

:::::
:::

Can you discriminate between "dog" and "bog", when the articulators are visible?

## Visual Speech {data-auto-animate="true"}

Audiovisual speech is _complementary_ in nature.

::: incremental

- Sounds that **sound** similar often look different

  eg. /b/, /d/, /m/, /n/, /f/, /s/

- The formation of sounds that **look** the same sound different

  eg. /f/, /v/, /s/, /t/, /b/, /p/

:::

## Visual Speech {data-auto-animate="true"}

Visual information provides an effective improvement of $\approx 11 dB$ in signal-to-noise ratio.

## Visual Speech {data-auto-animate="true"}

Vision can improve understanding of hard-to-understand utterances.

## Visual Speech {data-auto-animate="true"}

::: columns
::::: column
![Benjamin Franklin](assets/benfranklin.jpg)
:::::
::::: column
Benjamin Franklin invented bi-focal spectacles to help better understand French!
:::::
:::

---

> "... since my being in France, the glasses that serve me best at table
> to see what I eat, not being the best to see the faces of
> those on the other side of the table who speak to me;
>
> ... and when one's ears are not well accustomed to the sounds of a
> language, a sight of the movements in the features of him that
> speaks helps to explain...
>
> so that I understand French better by the help of my spectacles."
>
> -- <cite>Benjamin Franklin, in 1785</cite>

## McGurk Effect {data-auto-animate="true"}

Visual speech can **alter** our perception of a sound.

## McGurk Effect {data-auto-animate="true"}

::: columns
::::: column

<video controls loop width="340px"
    data-src="assets/mov/bagada.mp4">
</video>

:::::
::::: {.column .incremental}

- you hear "baa" ...
- you see "gaa" ...
- you perceive "daa" ...

:::::
:::

## McGurk Effect {data-auto-animate="true"}

Auditory "baa" with visual "gaa" is (usually) perceived as "daa".

::: incremental

- What is perceived is neither seen nor heard!
- happens even when the viewer is aware of the effect
- The effect persists across age, gender and language.

:::

## McGurk Effect {data-auto-animate="true"}

<video controls loop
    data-src="assets/mov/McGurkEffect.mp4">
</video>

"baa" or "faa"?

## McGurk Effect {data-auto-animate="true"}

<video controls loop
    data-src="assets/mov/bill-pail-mayo.mp4">
</video>

"Bill", "pail", "mayo"?

## McGurk Effect {data-auto-animate="true"}

Also on YouTube:

- https://youtu.be/KiuO_Z2_AD4
- https://youtu.be/xlXaNJR-1Oo
- https://youtu.be/G-lN8vWm3m0

# Visemes

## Visemes {data-auto-animate="true"}

- The basic building block of auditory speech is the **phoneme**.
- The closest visual equivalent is the **viseme** (visual phoneme).

## Visemes {data-auto-animate="true"}

- The mapping from phonemes to visemes is **many-to-one**.
- Many phonemes map to the same viseme.

## Visemes {data-auto-animate="true"}

- Visemes are usually derived using _subjective_ experiments.
- Viewers are asked to identify the consonant in isolated nonsense words.

## Visemes {data-auto-animate="true"}

![F.Parke and K.Waters, Computer Facial Animation, A K Peters, 1996. 
](assets/img/visemes.png)

#

<h1 class="r-fit-text"> Coarticulation</h1>

## Coarticulation {data-auto-animate="true"}

Phonemes are abstract representations of sound.

## Coarticulation {data-auto-animate="true"}

- We could think of speech as being a string of phonemes.
- Each has an idealised articulator configuration
- Speech is produced by smoothly varying from one vocal tract configuration to the next.

## Coarticulation {data-auto-animate="true"}

::: r-fit-text

WRONG!!

:::

## Coarticulation {data-auto-animate="true"}

The articulator positions **do not** depend only on the current sound.

::: incremental

- Neighbouring sounds influence each other.

:::

## Coarticulation {data-auto-animate="true"}

The articulators never reach their _ideal_ target.

They only move close enough to _approximate_ the required sound.

::: incremental

- What you see is a by-product of this.

:::

## Coarticulation {data-auto-animate="true"}

This is known as **coarticulation**.

## Coarticulation {data-auto-animate="true"}

There are two forms of coarticulation:

- anticipatory coarticulation
- perseverative coarticulation

::: notes
perseverative is also known as carry-over coarticulation
:::

## Coarticulation {data-auto-animate="true"}

The same phoneme in different contexts both sounds and **looks** different.

## /k/

::: columns
::::: column

<video controls width="400px"
    data-src="assets/mov/k-k-k-ken-small-cropped.mp4">
</video>

:::::
::::: {.column width=16%}

![](assets/img/k-phone-0.jpg)
![](assets/img/k-phone-1.jpg)
![](assets/img/k-phone-2.jpg)
![](assets/img/k-phone-3.jpg)
![](assets/img/k-phone-4.jpg)

:::::
:::

## /t/

::: columns
::::: column

<video controls width="400px"
    data-src="assets/mov/t-t-t-ken-small-cropped.mp4">
</video>

:::::
::::: {.column width=16%}

![](assets/img/t-phone-0.jpg)
![](assets/img/t-phone-1.jpg)
![](assets/img/t-phone-2.jpg)
![](assets/img/t-phone-3.jpg)
![](assets/img/t-phone-4.jpg)

:::::
:::
