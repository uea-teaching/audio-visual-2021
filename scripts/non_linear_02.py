# %%
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import gaussian, median

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

cameraman = plt.imread(
    '../lectures/assets/plots1/cameraman.png').astype(np.float32)


def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    max = 1
    if len(image.shape) == 2:
        black = 0
        white = max
    else:
        colorspace = image.shape[2]
        if colorspace == 3:  # RGB
            black = np.array([0, 0, 0], dtype='uint8')
            white = np.array([max, max, max], dtype='uint8')
        else:  # RGBA
            black = np.array([0, 0, 0, max], dtype='uint8')
            white = np.array([max, max, max, max], dtype='uint8')
    probs = np.random.random(image.shape[:2])
    image[probs < (prob / 2)] = black
    image[probs > 1 - (prob / 2)] = white
    return image


def imshow_gray(ax, img):
    vmax = 255 if img.dtype == np.uint8 else 1
    h, w = img.shape[:2]
    ax.imshow(img, cmap="gray",
              extent=[0, w, h, 0],
              vmin=0, vmax=vmax, interpolation='none')


# %%

cam_sp = sp_noise(cameraman.copy(), 0.1)
fig, ax = plt.subplots(1, 2, figsize=(10, 6))
imshow_gray(ax[0], cameraman)
ax[0].grid(False)
ax[0].set_title('Original')
ax[0].set_xticks([0, 128, 256])
ax[0].set_yticks([0, 128, 256])

imshow_gray(ax[1], cam_sp)
ax[1].grid(False)
ax[1].set_title('Salt and Pepper Noise')
ax[1].set_xticks([0, 128, 256])
ax[1].set_yticks([0, 128, 256])
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")

fig.tight_layout()
fig.savefig(root + 'salt_pepper.png', **savekw)

# %%

med_filtered = median(cam_sp)
gaus_filtered = gaussian(cam_sp, sigma=1, truncate=2)

# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
imshow_gray(ax[0], cam_sp)
ax[0].grid(False)
ax[0].set_title('Salt and Pepper Noise')
ax[0].set_xticks([0, 128, 256])
ax[0].set_yticks([0, 128, 256])

imshow_gray(ax[1], med_filtered)
ax[1].grid(False)
ax[1].set_title('Median 3x3 Filtered')
ax[1].set_xticks([0, 128, 256])
ax[1].set_yticks([0, 128, 256])
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")

fig.tight_layout()
fig.savefig(root + 'sp_median_filtered.png', **savekw)

# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
imshow_gray(ax[0], cameraman)
ax[0].grid(False)
ax[0].set_title('Original')
ax[0].set_xticks([0, 128, 256])
ax[0].set_yticks([0, 128, 256])

imshow_gray(ax[1], med_filtered)
ax[1].grid(False)
ax[1].set_title('Median 3x3 Filtered')
ax[1].set_xticks([0, 128, 256])
ax[1].set_yticks([0, 128, 256])
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")

fig.tight_layout()
fig.savefig(root + 'orig_median_filtered.png', **savekw)

# %%

fig, ax = plt.subplots(1, figsize=(7, 6))
imshow_gray(ax, cameraman - med_filtered)
ax.grid(False)
ax.set_title('Difference Image')
ax.set_xticks([0, 128, 256])
ax.set_yticks([0, 128, 256])

fig.tight_layout()
fig.savefig(root + 'orig_median_difference.png', **savekw)

# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
imshow_gray(ax[0], gaus_filtered)
ax[0].grid(False)
ax[0].set_title('Gaussian Filtered')
ax[0].set_xticks([0, 128, 256])
ax[0].set_yticks([0, 128, 256])

imshow_gray(ax[1], med_filtered)
ax[1].grid(False)
ax[1].set_title('Median 3x3 Filtered')
ax[1].set_xticks([0, 128, 256])
ax[1].set_yticks([0, 128, 256])
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")

fig.tight_layout()
fig.savefig(root + 'gauss_median_filtered.png', **savekw)
