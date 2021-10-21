# %%

import numpy as np
from sklearn.decomposition import PCA
from skimage import data, io, filters, transform, feature
from scipy.fftpack import dct, dctn, idctn
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.style.use('fivethirtyeight')

savekw = dict(bbox_inches='tight', dpi=160)
rectkw = dict(linewidth=2, edgecolor='r', facecolor='none')
root = '../lectures/assets/plots2/'

cameraman = io.imread('../lectures/assets/plots1/cameraman.png')

# %%

# plot 8 point basis vectors

N = 8
fig, ax = plt.subplots(N, 1, figsize=(8, N+2), sharex=True)

for k in range(N):
    x = np.linspace(0, N-1, 1000)
    xx = np.linspace(0, N-1, N)
    y = np.cos(np.pi * k * (x + 0.5) / N)
    yy = np.cos(np.pi * k * (xx + 0.5) / N)
    ax[k].plot(x, y)
    ax[k].plot(xx, yy, 'or')
    ax[k].set_ylim(-1.2, 1.2)
    ax[k].set_yticks([-1, 0, 1])
    ax[k].set_ylabel(f'{k:1d}', rotation=0, labelpad=20)

ax[0].set_ylabel(f'{0}', rotation=0, labelpad=30)
ax[0].set_ylim(0, 2)
ax[0].set_yticks([0, 1, 2])
ax[0].set_title('8 point basis vectors')
ax[-1].set_xlabel('sample index')
fig.text(-0.05, 0.5, 'result index', va='center',
         rotation='vertical', fontsize=18)
fig.tight_layout(pad=0.1)

fig.savefig(root + 'basis_vectors_1d.png', **savekw)

# %%

x, y, w, h = 120, 55, 8, 8
rect = patches.Rectangle((x, y), w, h, **rectkw)
block = cameraman[y:h+y, x:w+x]

fig, ax = plt.subplots(1, 2, figsize=(9, 6))
ax[0].grid(False)
ax[1].grid(False)
ax[0].imshow(cameraman, cmap='gray', vmin=0, vmax=255)
ax[0].add_patch(rect)
ax[0].set_title('original image')
ax[1].set_title('8 x 8 block')
ax[1].imshow(block, cmap='gray', vmin=0, vmax=255)
fig.tight_layout(pad=0.1)
fig.savefig(root + 'cameraman_block.png', **savekw)

# %%

fig, ax = plt.subplots(8, 2, figsize=(10, 6.5), sharex=True, sharey=True)
x = np.arange(8)
for k in range(8):
    _dct = dct(block[k, :])
    ax[k, 0].plot(block[k, :])
    ax[k, 0].set_ylim(-150, 255)
    ax[k, 0].set_yticks([])
    ax[k, 0].set_ylabel(f'{k}', rotation=0, labelpad=10)
    ax[k, 0].yaxis.tick_right()
    ax[k, 1].bar(x, height=_dct, width=0.8)
ax[0, 0].set_title('Pixel Intensities')
ax[0, 1].set_title('DCT Coefficients')
ax[7, 0].set_xlabel('sample index')
ax[7, 1].set_xlabel('result index')
fig.text(-0.04, 0.5, 'row index', va='center',
         rotation='vertical', fontsize=18)
fig.suptitle('DCT of 8 x 8 block', fontsize=22, y=1.03)
fig.tight_layout(pad=0.2)
fig.savefig(root + 'dct_8x8_block.png', **savekw)

# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 2), sharey=True)
ax[0].plot(block[3, :])
ax[0].set_title('Pixel Intensities')
ax[0].set_xlabel('sample index')
ax[0].set_ylabel('row 3')
ax[0].set_ylim(-150, 255)
ax[0].set_yticks([0, 255])

ax[1].bar(np.arange(8), dct(block[3, :]), width=0.8)
ax[1].set_title('DCT Coefficients')
ax[1].set_xlabel('result index')

fig.tight_layout(pad=0.2)
fig.savefig(root + 'block_row3.png', **savekw)

# %%

# 2D DCT

_dctn = dctn(block, norm='ortho')

fig, ax = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
ax[0].pcolormesh(block, cmap='gray', vmin=0, vmax=255,
                 edgecolors='w', linewidth=1)
ax[0].set_aspect('equal')
ax[0].set_ylim(8, 0)
ax[0].set_title('8 x 8 block')
ax[1].pcolormesh(_dctn, cmap='plasma', edgecolors='w', linewidth=1)
ax[1].set_aspect('equal')
ax[1].set_ylim(8, 0)
ax[1].set_title('DCT Coefficients')
fig.tight_layout(pad=0.2)
fig.savefig(root + 'dct_2d_block.png', **savekw)


# %%

# plot values

fig, ax = plt.subplots(1, figsize=(7, 7))
ax.pcolormesh(np.ones([8, 8]), cmap='gray', vmin=0, vmax=1,
              edgecolors='k', linewidth=1)
ax.set_axis_off()
ax.set_ylim(8, 0)
ax.set_aspect('equal')

for i in range(8):
    for j in range(8):
        s = f"{_dctn[i, j]:0.0f}"
        ax.text(j + 0.05, i + 0.5, f'{s:^5}', va='center', fontsize=22)
fig.tight_layout(pad=0.2)
fig.savefig(root + 'dct_2d_values.png', **savekw)

# %%

poly = patches.Polygon([[0, 8], [0, 0], [8, 0]],
                       edgecolor='none', facecolor=(0, 0.7, 0, 0.5))

fig, ax = plt.subplots(1, figsize=(7, 7))
ax.pcolormesh(np.ones([8, 8]), cmap='gray', vmin=0, vmax=1,
              edgecolors='k', linewidth=1)
ax.set_axis_off()
ax.set_ylim(8, 0)
ax.set_aspect('equal')

for i in range(8):
    for j in range(8):
        s = f"{_dctn[i, j]:0.0f}"
        ax.text(j + 0.05, i + 0.5, f'{s:^5}', va='center', fontsize=22)

ax.add_patch(poly)
fig.tight_layout(pad=0.2)
fig.savefig(root + 'dct_2d_values_high.png', **savekw)


# %%

poly = patches.Polygon([[0, 8], [8, 8], [8, 0]],
                       edgecolor='none', facecolor=(0.7, 0, 0, 0.4))

fig, ax = plt.subplots(1, figsize=(7, 7))
ax.pcolormesh(np.ones([8, 8]), cmap='gray', vmin=0, vmax=1,
              edgecolors='k', linewidth=1)
ax.set_axis_off()
ax.set_ylim(8, 0)
ax.set_aspect('equal')

for i in range(8):
    for j in range(8):
        s = f"{_dctn[i, j]:0.0f}"
        ax.text(j + 0.05, i + 0.5, f'{s:^5}', va='center', fontsize=22)

ax.add_patch(poly)

fig.tight_layout(pad=0.2)
fig.savefig(root + 'dct_2d_values_low.png', **savekw)
