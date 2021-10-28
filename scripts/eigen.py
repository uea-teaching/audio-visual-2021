# %%

import numpy as np
from numpy.lib.arraypad import pad
from numpy.random import beta
from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=160)
root = '../lectures/assets/plots2/'

# %%

faces = datasets.fetch_olivetti_faces()
faces.data.shape

# %%

fig, axs = plt.subplots(3, 6, figsize=(10.5, 6), sharey=True, sharex=True)
for i, ax in enumerate(axs.flat):
    k = i * 23
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')
    ax.imshow(faces.images[k], cmap='gray', interpolation='none')
    print(k)
fig.suptitle('Olivetti faces', fontsize=22, y=1.0)
fig.tight_layout(pad=0.1)
fig.savefig(root + 'eigen_faces_data.png', **savekw)

# %%

X = faces.data
pca = PCA(n_components=150, whiten=True)
pca.fit(X)

# %%

fig, ax = plt.subplots(1, 1, figsize=(5, 5))
ax.grid(False)
ax.set_aspect('equal')
ax.set_title('Mean Face')
ax.imshow(pca.mean_.reshape((64, 64)), cmap='gray')
fig.tight_layout(pad=0.1)
fig.savefig(root + 'eigen_faces_mean.png', **savekw)

# %%

fig, axs = plt.subplots(3, 6, figsize=(10.5, 6), sharey=True, sharex=True)
for i, ax in enumerate(axs.flat):
    ax.grid(False)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    im = pca.components_[i].reshape((64, 64))
    ax.imshow(im, cmap='gray', interpolation='none')
fig.suptitle('First 18 Principal Components', fontsize=22, y=1.0)
fig.tight_layout(pad=0.1)
fig.savefig(root + 'eigen_faces_components.png', **savekw)


# %%


def reconstruct(idx, n=0):
    betas_t = pca.transform(faces.data[idx:idx+1])
    betas = np.zeros_like(betas_t)
    betas[:, :n] = betas_t[:, :n]
    return pca.inverse_transform(betas).reshape((64, 64))


def recon_frame(idx, n=0):
    fig, ax = plt.subplots(1, 2, figsize=(9, 6), sharey=True, sharex=True)
    ax[0].set_title('Target Face')
    ax[0].grid(False)
    ax[0].set_xticks([])
    ax[0].set_xlim(0, 64)
    ax[0].set_ylim(64, 0)
    ax[0].set_aspect('equal')
    ax[0].imshow(faces.images[idx], cmap='gray', interpolation='none')
    ax[1].set_title(f'{n:03d} components')
    ax[1].grid(False)
    ax[1].set_xticks([])
    ax[1].set_aspect('equal')
    ax[1].set_xlim(0, 64)
    ax[1].set_ylim(64, 0)
    ax[1].imshow(reconstruct(idx, n), cmap='gray', interpolation='none')
    fig.tight_layout(pad=0.1)
    plt.close(fig)
    return fig, ax


idx = 368
for n in range(151):
    if n > 5 and n % 5 != 0:
        continue
    fig, ax = recon_frame(idx, n)
    fig.savefig(f'/Users/shared/tmp/recon_{n:03d}.png', **savekw)

fig

# %%

"""
Make a video:
ffmpeg \
    -framerate 5 \
    -r 5 \
    -pattern_type glob \
    -i '*.png' \
    -vf scale=600:-1 \
    out.gif
"""
