# %%

import numpy as np
import matplotlib.pyplot as plt
import skimage.morphology as morphology

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

# %%

n = 9


def plot_question(ax):
    ax.imshow(np.ones([n, n]) * 0.7, cmap='gray', vmin=0, vmax=1)
    ax.set_title('output')
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticks(np.arange(0, n, 1))
    ax.grid(False)
    ax.text(4, 4, '?', ha='center', va='center', fontsize=98)


def plot_binary(ax, img, n=9, title='$A$', fs=16):
    ax.imshow(img, vmin=0, vmax=1, cmap='gray')

    # Set the major ticks at the centers and minor tick at the edges
    locs = np.arange(0, n, 1)
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_ticks(locs + 0.5, minor=True)
        axis.set(ticks=locs, ticklabels=locs)

    # Turn on the grid for the minor ticks
    ax.grid(True, which='minor')
    ax.grid(False, which='major')

    for i in range(n):
        for j in range(n):
            v = int(img[i, j])
            c = 'w' if v == 0 else 'k'
            ax.text(j, i, v, ha='center', va='center', fontsize=fs, color=c)
    ax.set_title(title)


def plot_structuring_element(ax, img, n=3, title='$B$', fs=16):
    plot_binary(ax, img, n=n, title=title, fs=fs)
    ax.set_xticks([])
    ax.set_yticks([])


A = np.zeros([n, n], dtype=bool)
A[4, 4] = 1

B = np.array([[1, 0, 0], [1, 0, 0], [1, 1, 1]], dtype=bool)

fig, ax = plt.subplots(1, 3, figsize=(10, 8), gridspec_kw={
    'width_ratios': [10, 3.5, 10]})
plot_binary(ax[0], A)
plot_structuring_element(ax[1], B)
plot_question(ax[2])
fig.tight_layout()
fig.savefig(root + 'dilate_question.png', **savekw)


# %%

C = morphology.dilation(A, B)

fig, ax = plt.subplots(1, 3, figsize=(10, 8), gridspec_kw={
    'width_ratios': [10, 3.5, 10]})
plot_binary(ax[0], A)
plot_structuring_element(ax[1], B)
plot_binary(ax[2], C, title='output')
fig.tight_layout()
fig.savefig(root + 'dilate_answer.png', **savekw)

# %%
