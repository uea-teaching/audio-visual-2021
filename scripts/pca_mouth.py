# %%
import json
import numpy as np
from sklearn.decomposition import PCA
from scipy.spatial import procrustes
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# %%

# Load data and centre it
with open('lmk_recG001_crop.json') as fid:
    mouths = np.array(json.load(fid), dtype=np.float64)[:, 48:, :]
    mouths -= np.mean(mouths, axis=1, keepdims=True)

# %%

mean_mouth = np.mean(mouths, axis=0, keepdims=True)
mean_mouth -= mean_mouth.mean(axis=1, keepdims=True)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.set_title('Mean mouth')
ax.scatter(mean_mouth[0, :, 0], mean_mouth[0, :, 1])
ax.scatter(mouths[0, :, 0], mouths[0, :, 1])
ax.legend(['mean', 'first'])

# %%

# Align all the mouths to the mean mouth
aligned = np.stack([procrustes(mean_mouth[0], m)[1] for m in mouths], 0)

# %%

idx = 42
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.set_title('Procrustes')
ax.scatter(aligned[idx, :, 0], aligned[idx, :, 1])
ax.legend(['mean', 'first'])


# %%

# Perform PCA
x_mean = mean_mouth.reshape(1, 40)
x_aligned = aligned.reshape(-1, 40) - x_mean

pca = PCA(n_components=3)
pca.fit(x_aligned)

# %%

# 1 std is sqrt of variance
b = np.sqrt(pca.explained_variance_.copy())


def plot_mouth(ax, x, title=None):
    outer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
    inner = [12, 13, 14, 15, 16, 17, 18, 19, 12]
    ax.set_title(title)
    ax.scatter(x[:, 0], x[:, 1])
    ax.plot(x[inner, 0], x[inner, 1], '-r', alpha=0.5)
    ax.plot(x[outer, 0], x[outer, 1], '-r', alpha=0.5)


fig, axs = plt.subplots(2, 3, figsize=(12, 7), sharex=True, sharey=True)
fig.suptitle('First 3 Components +/- 3 standard deviations')
for i in range(3):
    for j in range(2):
        _m = np.zeros(3)
        _m[i] = 3
        _m *= -1 if j == 1 else 1
        p = b * _m
        x = (x_mean + pca.inverse_transform(p)).reshape(20, 2)
        plot_mouth(
            axs[j, i], x, f'$\sigma$ * ({int(_m[0])}, {int(_m[1])}, {int(_m[2])})')

fig.savefig('../lectures/assets/plots2/pca_mouth.png')

# %%
