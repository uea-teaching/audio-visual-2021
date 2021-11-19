# %%

import numpy as np
import matplotlib.pyplot as plt
import skimage.morphology as morphology

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

shapes = plt.imread(
    '../lectures/assets/img4/binary_shapes.png')[:, :, 0].astype(bool)

# %%

shapes_dilated_5 = morphology.dilation(shapes, morphology.square(5))
shapes_dilated_15 = morphology.dilation(shapes, morphology.square(15))
shapes_eroded_5 = morphology.erosion(shapes, morphology.square(5))
shapes_eroded_15 = morphology.erosion(shapes, morphology.square(15))
shapes_open_5 = morphology.opening(shapes, morphology.square(5))
shapes_open_15 = morphology.opening(shapes, morphology.square(15))
shapes_close_5 = morphology.closing(shapes, morphology.square(5))
shapes_close_15 = morphology.closing(shapes, morphology.square(15))

# %%


def bin_axis(ax, img, title):
    h, w = img.shape[:2]
    ax.imshow(img, cmap="gray",
              extent=[0, w, h, 0],
              vmin=0, vmax=1, interpolation='none')
    ax.set_title(title)
    ax.set_xticks([0, 127, 256])
    ax.set_yticks([0, 127, 256])
    ax.grid(False)


def plot_bin_pair(img1, img2, title):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    bin_axis(ax[0], img1, 'original')
    bin_axis(ax[1], img2, title)
    ax[1].set_ylabel('pixels')
    ax[1].yaxis.set_label_position("right")
    fig.tight_layout()
    return fig

# %%


fig = plot_bin_pair(shapes, shapes_dilated_5, 'dilation 5x5')
fig.savefig(root + 'dilation_5.png', **savekw)

# %%

fig = plot_bin_pair(shapes, shapes_dilated_15, 'dilation 15x15')
fig.savefig(root + 'dilation_15.png', **savekw)

# %%

fig = plot_bin_pair(shapes, shapes_eroded_5, 'erosion 5x5')
fig.savefig(root + 'erosion_5.png', **savekw)

# %%

fig = plot_bin_pair(shapes, shapes_eroded_15, 'erosion 15x15')
fig.savefig(root + 'erosion_15.png', **savekw)

# %%

fig = plot_bin_pair(shapes, shapes_open_5, 'opening 5x5')
fig.savefig(root + 'opening_5.png', **savekw)

# %%

fig = plot_bin_pair(shapes, shapes_open_15, 'opening 15x15')
fig.savefig(root + 'opening_15.png', **savekw)

# %%

fig = plot_bin_pair(shapes, shapes_close_5, 'closing 5x5')
fig.savefig(root + 'closing_5.png', **savekw)

# %%

fig = plot_bin_pair(shapes, shapes_close_15, 'closing 15x15')
fig.savefig(root + 'closing_15.png', **savekw)
