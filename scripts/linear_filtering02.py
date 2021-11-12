# %%

import numpy as np
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

cameraman = plt.imread('../lectures/assets/plots1/cameraman.png')
astronaut = rgb2gray(plt.imread('../lectures/assets/plots1/astronaut.png'))
n, m = 85, 188
mini = astronaut[n:n+30, m:m+30]


cols = [(1, 0, 0), (0.3, 0.9, 0.3), (0.9, 0.9, 0.3),
        (0.9, 0.3, 0.9), (0.3, 0.9, 0.9), (0.9, 0.6, 0.6), (0.9, 0.9, 0.6)]


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


def plot_question(ax):
    ax.imshow(np.ones([9, 9]) * 0.7, cmap='gray', vmin=0, vmax=1)
    ax.set_title('$g$')
    ax.grid(False)
    ax.text(4, 4, '?', ha='center', va='center', fontsize=98)


def plot_kernel(ax, n, txt, fs=18):
    img = np.ones([n, n, 3]) * cols[6]
    lw = 2
    ax.imshow(img, vmin=0, vmax=1, extent=[0, n, n, 0],)
    ax.grid(True, lw=lw, color='0',)
    ax.set_title('$h$')
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticks(np.arange(0, n, 1))
    for i in range(n):
        for j in range(n):
            ax.text(j + 0.5, i + 0.5, txt[i*n+j],
                    ha='center', va='center', fontsize=fs)


def plot_filter(f=None, g=None):
    fig, ax = plt.subplots(1, 3, figsize=(10, 8), gridspec_kw={
        'width_ratios': [10, 3.5, 10]})
    plot_image(ax[0], f, '$f$')
    if g is not None:
        plot_image(ax[2], g, '$g$')
    else:
        plot_question(ax[2])
    for a in ax:
        outline(a)
    plt.close(fig)
    fig.tight_layout()
    return fig, ax

# %%


fig, ax = plot_filter(mini, None)
hs = ['0', '0', '0', '0', '1', '0', '0', '0', '0', ]
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel1_q.png', **savekw)
fig

# %%

fig, ax = plot_filter(mini, mini)
hs = ['0', '0', '0', '0', '1', '0', '0', '0', '0', ]
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel1_a.png', **savekw)
fig

# %%

fig, ax = plot_filter(mini, None)
hs = ['0', '0', '0', '1', '0', '0', '0', '0', '0', ]
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel2_q.png', **savekw)
fig

# %%

hs = ['0', '0', '0', '1', '0', '0', '0', '0', '0', ]
h = np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]])
g = filters.edges.convolve(mini, h, mode='constant')

fig, ax = plot_filter(mini, g)
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel2_a.png', **savekw)
fig

# %%

hs = ['1/9'] * 9
fig, ax = plot_filter(mini, None)
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel3_q.png', **savekw)
fig

# %%

hs = ['1/9'] * 9
h = np.ones([3, 3])/9
g = filters.edges.convolve(mini, h)
fig, ax = plot_filter(mini, g)
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel3_a.png', **savekw)
fig

# %%

hs = ['0', '-1', '0', '-1', '5', '-1', '0', '-1', '0']
fig, ax = plot_filter(mini, None)
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel4_q.png', **savekw)
fig

# %%

hs = ['0', '-1', '0', '-1', '5', '-1', '0', '-1', '0']
h = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
g = filters.edges.convolve(mini, h)
fig, ax = plot_filter(mini, g)
plot_kernel(ax[1], 3, hs, fs=16)
fig.savefig(root + 'kernel4_a.png', **savekw)
fig

# %%
