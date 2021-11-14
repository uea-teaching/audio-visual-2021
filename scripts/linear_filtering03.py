# %%

import numpy as np
from numpy.lib.type_check import imag
from skimage import filters
from skimage.feature import match_template
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

cameraman = plt.imread('../lectures/assets/plots1/cameraman.png')
astronaut = plt.imread('../lectures/assets/plots1/astronaut.png')

# %%


def plot_image(ax, image, title):
    n, m = image.shape[:2]
    ax.imshow(image, cmap='gray', vmin=0, vmax=1)
    ax.set_title(title)
    ax.grid(False)


def outline(ax, lw=2):
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    for s in ax.spines:
        ax.spines[s].set_color('0')
        ax.spines[s].set_linewidth(lw)


def sigma2fwhm(sigma):
    return sigma * np.sqrt(8 * np.log(2))


def fwhm2sigma(fwhm):
    return fwhm / np.sqrt(8 * np.log(2))


def gkern(l=5, sig=1.):
    """
    creates gaussian kernel with side length `l` and a sigma of `sig`
    """
    ax = np.linspace(-(l - 1) / 2., (l - 1) / 2., l)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sig))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)


# %%

sigma = 2
x = np.linspace(-6, 6, 100)
y = np.linspace(-6, 6, 100)
x2d, y2d = np.meshgrid(x, y)
kernel_2d = np.exp(-(x2d ** 2 + y2d ** 2) / (2 * sigma ** 2))
kernel_2d = kernel_2d / (2 * np.pi * sigma ** 2)  # unit integral

h = gkern(7, sigma)

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x2d, y2d, kernel_2d, cmap='viridis')
ax1.set_title(fr'2D Gaussian $\sigma={sigma}$')
ax1.set_xticks([-5, 0, 5])
ax1.set_yticks([-5, 0, 5])
ax1.set_zticks([0, 0.02, 0.04])
ax2 = fig.add_subplot(122)
ax2.imshow(h, cmap='viridis', extent=[0, 7, 0, 7])
ax2.set_title(fr'$7 \times 7$ kernel matrix')
ax2.axis('off')
fig.savefig(root + '2d_gaussian.png', **savekw)

# %%

mean_filtered = filters.edges.convolve(cameraman, np.ones((7, 7)) / (7 ** 2))
gaussian_filtered = filters.edges.convolve(cameraman, gkern(7, sigma))

fig, ax = plt.subplots(1, 3, figsize=(10, 6))
plot_image(ax[0], cameraman, 'original')
plot_image(ax[1], mean_filtered, 'mean 7x7')
plot_image(ax[2], gaussian_filtered, 'gaussian 7x7')
for a in ax:
    outline(a)
fig.tight_layout()
fig.savefig(root + 'cameraman_filtered.png', **savekw)


# %%

diff7x7 = cameraman - gaussian_filtered

fig, ax = plt.subplots(1, 3, figsize=(10, 6))
plot_image(ax[0], cameraman, 'original')
plot_image(ax[1], gaussian_filtered, 'gaussian 7x7')
plot_image(ax[2], diff7x7, 'difference image')

for a in ax:
    outline(a)
fig.tight_layout()
fig.savefig(root + 'unsharp_diff.png', **savekw)

# %%

fig, ax = plt.subplots(1, 3, figsize=(10, 6))
plot_image(ax[0], cameraman, 'original')
plot_image(ax[1], cameraman + 2 * diff7x7, r'I(x, y) + 2D(x, y)')
plot_image(ax[2], cameraman + 5 * diff7x7, r'I(x, y) + 5D(x, y)')

for a in ax:
    outline(a)
fig.tight_layout()
fig.savefig(root + 'unsharp_mask7x7.png', **savekw)

# %%

gaussian_11 = filters.edges.convolve(cameraman, gkern(13, sigma))
diff11x11 = cameraman - gaussian_11

fig, ax = plt.subplots(1, 3, figsize=(10, 6))
plot_image(ax[0], cameraman, 'original')
plot_image(ax[1], gaussian_11, 'gaussian 11x11')
plot_image(ax[2], diff11x11, 'difference image')

for a in ax:
    outline(a)
fig.tight_layout()
fig.savefig(root + 'unsharp_diff_11x11.png', **savekw)

# %%

fig, ax = plt.subplots(1, 3, figsize=(10, 6))
plot_image(ax[0], cameraman, 'original')
plot_image(ax[1], cameraman + 2 * diff11x11, r'I(x, y) + 2D(x, y)')
plot_image(ax[2], cameraman + 5 * diff11x11, r'I(x, y) + 5D(x, y)')

for a in ax:
    outline(a)
fig.tight_layout()
fig.savefig(root + 'unsharp_mask11x11.png', **savekw)

# %%


def plot_image_min_max(ax, image, title):
    n, m = image.shape[:2]
    ax.imshow(image, cmap='gray')
    ax.set_title(title)
    ax.grid(False)


rect = patches.Rectangle(
    (95, 40), 40, 40, linewidth=2, edgecolor='r', facecolor='none')

image = cameraman / 255
image_mean = image.mean()
image -= image_mean
kernel = np.rot90(image[40:80, 95:135], 2)
output = filters.edges.convolve(image, kernel)
y, x = np.where(output == output.max())


fig, ax = plt.subplots(1, 2, figsize=(10, 6))
plot_image_min_max(ax[0], image, 'original')
plot_image_min_max(ax[1], kernel, 'kernel')
ax[0].add_patch(rect)
ax[0].set_xticks([0, 100, 200])
ax[0].set_yticks([0, 100, 200])
ax[1].set_xticks([0, 20, 40])
ax[1].set_yticks([0, 20, 40])
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")
ax[0].set_xlabel('pixels')
ax[1].set_xlabel('pixels')

fig.tight_layout()
fig.savefig(root + 'template_region.png', **savekw)

# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
plot_image_min_max(ax[0], image, 'original')
plot_image_min_max(ax[1], output, 'filtered')
ax[0].set_xticks([0, 100, 200])
ax[0].set_yticks([0, 100, 200])
ax[1].set_xticks([0, 100, 200])
ax[1].set_yticks([0, 100, 200])
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")
ax[0].set_xlabel('pixels')
ax[1].set_xlabel('pixels')

fig.tight_layout()
fig.savefig(root + 'template_response.png', **savekw)

# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
plot_image_min_max(ax[0], output, 'filtered')
plot_image_min_max(ax[1], image, 'original')
ax[0].set_xticks([0, 100, 200])
ax[0].set_yticks([0, 100, 200])
ax[1].set_xticks([0, 100, 200])
ax[1].set_yticks([0, 100, 200])
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")
ax[0].set_xlabel('pixels')
ax[1].set_xlabel('pixels')
ax[0].plot(x, y, 'rx', ms=15)
ax[1].plot(x, y, 'rx', ms=15)

fig.tight_layout()
fig.savefig(root + 'template_max.png', **savekw)

# %%
