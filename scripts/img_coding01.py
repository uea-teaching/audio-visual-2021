# %%

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.fftpack import dctn

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots4/'

cameraman = (plt.imread(root + 'cameraman.png') * 255).astype(np.uint8)
x, y, w, h = 126, 61, 8, 8

I = cameraman[y:y+h, x:x+w]

D = dctn((I*255).astype(np.float32), norm='ortho')

Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
              [12, 12, 14, 19, 26, 58, 60, 55],
              [14, 13, 16, 24, 40, 57, 69, 56],
              [14, 17, 22, 29, 51, 87, 80, 62],
              [18, 22, 37, 56, 68, 109, 103, 77],
              [24, 35, 55, 64, 81, 104, 113, 92],
              [49, 64, 78, 87, 103, 121, 120, 101],
              [72, 92, 95, 98, 112, 100, 103, 99]])

DQ = np.round(D / Q)

Z = [0, 1, 8, 16, 9, 2, 3, 10, 17, 24, 32, 25, 18,
     11, 4, 5, 12, 19, 26, 33, 40, 48, 41, 34, 27,
     20, 13, 6, 7, 14, 21, 28, 35, 42, 49, 56, 57,
     50, 43, 36, 29, 22, 15, 23, 30, 37, 44, 51, 58,
     59, 52, 45, 38, 31, 39, 46, 53, 60, 61, 54, 47,
     55, 62, 63]

# %%


def plot_grey(ax, img):
    ax.imshow(img, vmin=0, vmax=255, cmap='gray')

    # Set the major ticks at the centers and minor tick at the edges
    locs = np.arange(0, 8, 1)
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_ticks(locs + 0.5, minor=True)
        axis.set(ticks=locs, ticklabels=[])

    # Turn on the grid for the minor ticks
    ax.grid(True, which='minor')
    ax.grid(False, which='major')

    for s in ax.spines:
        ax.spines[s].set_color('0')
        ax.spines[s].set_linewidth(2)


def plot_vals(ax, img, fs=16):
    white = np.ones_like(img)
    ax.imshow(white, vmin=0, vmax=1, cmap='gray')

    # Set the major ticks at the centers and minor tick at the edges
    locs = np.arange(0, 8, 1)
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_ticks(locs + 0.5, minor=True)
        axis.set(ticks=locs, ticklabels=[])

    for s in ax.spines:
        ax.spines[s].set_color('0')
        ax.spines[s].set_linewidth(2)

    # Turn on the grid for the minor ticks
    ax.grid(True, which='minor', linestyle='-', linewidth=2, color='0')
    ax.grid(False, which='major')

    for i in range(8):
        for j in range(8):
            v = int(img[i, j])
            ax.text(j, i, v, ha='center', va='center', fontsize=fs)

# %%


fig, ax = plt.subplots(1, 2, figsize=(10, 6))
plot_grey(ax[0], I)
plot_vals(ax[1], I)
ax[0].set_title('8x8 Block')
ax[1].set_title('Intensities')
fig.tight_layout()
fig.savefig(root + 'jpg_block_values.svg', **savekw)

# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
plot_grey(ax[0], I)
plot_vals(ax[1], D)
ax[0].set_title('8x8 Block')
ax[1].set_title('DCT Coefficients')
fig.tight_layout()
fig.savefig(root + 'jpg_block_dct.svg', **savekw)

# %%

fig, ax = plt.subplots(1, figsize=(6, 6))
plot_vals(ax, Q)
ax.set_title('Quantisation Matrix ' + r'$Q$')
fig.tight_layout()
fig.savefig(root + 'jpg_quant_matrix.svg', **savekw)

# %%

fig, ax = plt.subplots(1, 3, figsize=(15, 6))
plot_vals(ax[0], D)
ax[0].set_title('DCT Coefficients')
plot_vals(ax[1], Q)
ax[1].set_title(r'$Q$')
plot_vals(ax[2], DQ)
ax[2].set_title('Quantised DCT')
fig.tight_layout()
fig.savefig(root + 'jpg_block_dct.svg', **savekw)

# %%

fig, ax = plt.subplots(1, figsize=(6, 6))
plot_vals(ax, DQ)
ax.set_title('Quantised DCT')
fig.tight_layout()
fig.savefig(root + 'jpg_block_quantised.svg', **savekw)

# %%

fig, ax = plt.subplots(1, figsize=(6, 6))
plot_vals(ax, DQ)

prev = (0, 0)
for z in Z[1:]:
    i, j = z % 8, z // 8
    ax.plot([prev[0], i], [prev[1], j], 'r-', lw=2)
    prev = (i, j)
ax.set_title('Quantised DCT')

fig.tight_layout()
fig.savefig(root + 'jpg_zigzag.svg', **savekw)

# %%

print([int(i) for i in DQ.flat[Z]])

# %%
