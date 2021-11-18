# %%

import numpy as np
import matplotlib.pyplot as plt
import skimage.morphology as morphology

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

cameraman = plt.imread(
    '../lectures/assets/plots1/cameraman.png').astype(np.float32)
coins = plt.imread('../lectures/assets/plots3/coins.png').astype(np.float32)

# %%


def imshow_gray(ax, img):
    vmax = 1.
    h, w = img.shape[:2]
    ax.imshow(img, cmap="gray",
              extent=[0, w, h, 0],
              vmin=0, vmax=vmax, interpolation='none')
    ax.set_yticks([])
    ax.set_xticks([])
    ax.grid(False)


t = 0.3
b_coins = coins > t
m_coins = morphology.binary_erosion(b_coins, morphology.square(3))

fig, ax = plt.subplots(1, 3, figsize=(10, 6), sharey=True)
imshow_gray(ax[0], coins)
ax[0].set_title('Original')
imshow_gray(ax[1], b_coins)
ax[1].set_title('Threshold')
imshow_gray(ax[2], m_coins)
ax[2].set_title('Erosion')
fig.tight_layout()

fig.savefig(root + 'coins_erosion.png', **savekw)

# %%
