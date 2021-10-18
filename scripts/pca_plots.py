# %%

import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

savekw = dict(bbox_inches='tight', dpi=160)
root = '../lectures/assets/plots2/'


# %%

# Some fake data:
np.random.seed(42)
fs = np.linspace(3, 12, 100) + np.random.randn(100) * 0.2
ht = np.linspace(3.5, 6, 100) + np.random.randn(100) * 0.2

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.scatter(ht, fs)
ax.grid(True)
ax.set_ylim(2.5, 12.5)
ax.set_xlabel('Height (ft)')
ax.set_ylabel('foot size')
ax.set_ylabel('Foot Size')
ax.set_title('Height and Foot Size')
fig.savefig(root + 'pca_01.png', **savekw)

# %%

# Some fake 2D data, normalised:
fs -= fs.mean()
fs /= fs.std()
ht -= ht.mean()
ht /= ht.std()

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.scatter(ht, fs)
ax.grid(True)
ax.set_xlim([-2.9, 2.9])
ax.set_ylim([-1.9, 1.9])
ax.set_aspect('equal')
ax.set_xlabel('Height')
ax.set_ylabel('Foot Size')
ax.set_title('Height and Foot Size - Normalised')
fig.savefig(root + 'pca_02.png', **savekw)

# %% DO PCA

X = np.stack([ht, fs], axis=1)
pca = PCA(n_components=2)
pca.fit(X)

# eigenvalue  is the variance of the data (std is sqrt of variance).
# eigenvector is the direction of the data
pc1 = pca.components_[0] * np.sqrt(pca.explained_variance_[0]) * -1
pc2 = pca.components_[1] * np.sqrt(pca.explained_variance_[1]) * -1

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.scatter(ht, fs)
ax.grid(True)
ax.set_aspect('equal')
ax.set_xlim([-2.9, 2.9])
ax.set_ylim([-1.9, 1.9])
ax.set_xlabel('Height')
ax.set_ylabel('Foot Size')
ax.set_title('Height and Foot Size - Normalised')

ax.plot([0, pc1[0]], [0, pc1[1]], 'r-', lw=2)
ax.plot([0, pc2[0]], [0, pc2[1]], 'g-', lw=2)
ax.legend(['P1', 'P2'], loc='upper left')
fig.savefig(root + 'pca_03.png', **savekw)

# %% ROTATE Data

cos, sin = -pca.components_[0]

R = np.array([
    [cos, -sin],
    [sin, cos]])

rX = X @ R
rp1 = pc1 @ R
rp2 = pc2 @ R

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([-2.9, 2.9])
ax.set_ylim([-1.9, 1.9])
ax.grid(False)
ax.scatter(rX[:, 0], rX[:, 1])
ax.plot([0, rp1[0]], [0, rp1[1]], 'r-', lw=2)
ax.plot([0, rp2[0]], [0, rp2[1]], 'g-', lw=2)
ax.legend(['P1', 'P2'], loc='upper left')
ax.set_title('Rotated Data')
fig.savefig(root + 'pca_04.png', **savekw)

# %%

pX = rX * (1, 0)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
ax.set_xlim([-2.9, 2.9])
ax.set_ylim([-1.9, 1.9])
ax.scatter(rX[:, 0], rX[:, 1])
ax.plot([-3, 3], [0, 0], 'r-', lw=2)
ax.legend(['P1', ], loc='upper left')
ax.set_title('First Principal Component')
fig.savefig(root + 'pca_05.png', **savekw)

# %%

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
ax.set_xlim([-2.9, 2.9])
ax.set_ylim([-1.9, 1.9])
ax.scatter(pX[:, 0], pX[:, 1])
ax.plot([-3, 3], [0, 0], 'r-', lw=2)
ax.legend(['P1', ], loc='upper left')
ax.set_title('Projected Data')
fig.savefig(root + 'pca_06.png', **savekw)

# %%

fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)
ax.set_xlim([-3, 3])
ax.set_ylim([-2, 2])
ax.plot([-3, 3], [0, 0], 'r-', lw=2)
ax.scatter(pX[:, 0], pX[:, 1], c='k')
ax.legend(['P1', ], loc='upper left')
ax.set_title('Parameter Values')
fig.savefig(root + 'pca_07.png', **savekw)
