# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.gridspec as gridspec
from skimage import filters

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots4/'

coins = plt.imread(root + 'coins.png')
cameraman = plt.imread(root + 'cameraman.png')

# %%

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(coins, cmap='gray')
ax.set_title('coins image')
fig.tight_layout()
fig.savefig(root + 'coins_fig.png', **savekw)

# %%

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(coins, cmap='gray')
ax.plot([0, 300], [20, 20], 'r--')
ax.set_xlabel('pixels')
ax.set_ylabel('pixels')

# create new axes on the top of the current axes.
divider = make_axes_locatable(ax)
axtop = divider.append_axes("top", size=1.2, pad=0.3, sharex=ax)
axtop.plot(coins[20, :])
axtop.set_title('intensity values at row 20')
axtop.set_ylabel('intensity')
fig.tight_layout()
fig.savefig(root + 'coins_row.png', **savekw)

# %%

y1 = coins[20, :]
y2 = coins[20, 1:] - coins[20, :-1]
y3 = coins[20, 2:] - 2 * coins[20, 1:-1] + coins[20, :-2]

fig = plt.figure(constrained_layout=True, figsize=(12, 5))
gs = fig.add_gridspec(3, 2)
ax = fig.add_subplot(gs[:, 0])
ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[1, 1], sharex=ax1)
ax3 = fig.add_subplot(gs[2, 1], sharex=ax1)

plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)

ax.imshow(coins, cmap='gray')
ax.plot([0, 300], [20, 20], 'r--')
ax.set_xlabel('pixels')
ax.set_ylabel('pixels')
ax.set_title('coins image')
ax1.plot(y1)
ax1.yaxis.tick_right()
ax1.set_title('intensity values')
ax2.plot(y2)
ax2.set_title('first derivative')
ax2.yaxis.tick_right()
ax3.plot(y3)
ax3.set_title('second derivative')
ax3.yaxis.tick_right()
ax3.set_xlabel('pixels')

fig.savefig(root + 'coins_derivatives.png', **savekw)

# %%

fx = (cameraman[1:, :] - cameraman[:-1, :])[:, :-1]
fy = (cameraman[:, 1:] - cameraman[:, :-1])[:-1, :]

fig, ax = plt.subplots(1, 3, figsize=(12, 6), sharey=True)
ax[0].imshow(cameraman, cmap='gray')
ax[0].set_title(r'$f$')
ax[0].set_xticks([0, 127, 256])
ax[0].set_yticks([0, 127, 256])

ax[1].imshow(fx, cmap='gray')
ax[1].set_title(r'$\frac{\delta f}{\delta x}$')
ax[1].set_xticks([0, 127, 256])

ax[2].imshow(fy, cmap='gray')
ax[2].set_title(r'$\frac{\delta f}{\delta y}$')
ax[2].set_xticks([0, 127, 256])
ax[2].set_ylabel('pixels')
ax[2].yaxis.set_label_position("right")

for a in ax:
    a.grid(False)

fig.tight_layout()
fig.savefig(root + 'cameraman_derivatives.png', **savekw)

# %%

mag_img = np.sqrt(fx**2 + fy**2)

fig, ax = plt.subplots(figsize=(7, 7))
ax.imshow(mag_img, cmap='gray')
ax.set_title('gradient magnitude ' + r'$|\Delta f|$')
ax.set_xticks([0, 127, 255])
ax.set_yticks([0, 127, 255])
ax.set_ylabel('pixels')
ax.grid(False)
ax.yaxis.set_label_position("right")
fig.tight_layout()
fig.savefig(root + 'cameraman_mag.png', **savekw)

# %%

lap_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
laplacian = filters.laplace(cameraman)

fig, ax = plt.subplots(1, 2, figsize=(12, 7), sharey=True)
ax[0].imshow(cameraman, cmap='gray')
ax[0].set_title('original')
ax[1].imshow(laplacian, cmap='gray', vmin=0, vmax=1)
ax[1].set_title('Laplacian ' + r'$\nabla f$')
ax[1].yaxis.set_label_position("right")
ax[1].set_ylabel('pixels')
for a in ax:
    a.set_xticks([0, 127, 256])
    a.set_yticks([0, 127, 256])
    a.grid(False)
fig.tight_layout()
fig.savefig(root + 'cameraman_laplacian.png', **savekw)


# %%

fig, ax = plt.subplots(1, 2, figsize=(12, 7), sharey=True)
ax[0].imshow(mag_img, cmap='gray')
ax[0].set_title('gradient magnitude ' + r'$|\Delta f|$')
ax[1].imshow(laplacian, cmap='gray', vmin=0, vmax=1)
ax[1].set_title('Laplacian ' + r'$\nabla f$')
ax[1].yaxis.set_label_position("right")
ax[1].set_ylabel('pixels')
for a in ax:
    a.set_xticks([0, 127, 256])
    a.set_yticks([0, 127, 256])
    a.grid(False)
fig.tight_layout()
fig.savefig(root + 'mag_grad_laplacian.png', **savekw)

# %%

# vertical lines
vert = np.array([[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]])
vert_filt = filters.edges.convolve(cameraman, vert)

fig, ax = plt.subplots(1, 2, figsize=(12, 7), sharey=True)
ax[0].imshow(laplacian, cmap='gray', vmin=0, vmax=1)
ax[0].set_title('Laplacian ' + r'$\nabla f$')
ax[1].imshow(vert_filt, cmap='gray', vmin=0, vmax=1)
ax[1].set_title('vertical lines')
ax[1].yaxis.set_label_position("right")
ax[1].set_ylabel('pixels')
for a in ax:
    a.set_xticks([0, 127, 256])
    a.set_yticks([0, 127, 256])
    a.grid(False)
fig.tight_layout()
fig.savefig(root + 'laplacian_vert_lines.png', **savekw)

# %%

vert = np.array([[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]])
fdiag = np.array([[-1, -1, 2], [-1, 2, -1], [2, -1, -1]])
horiz = np.array([[-1, -1, -1], [2, 2, 2], [-1, -1, -1]])
bdiag = np.array([[2, -1, -1], [-1, 2, -1], [-1, -1, 2]])

kernels = [vert, fdiag, horiz, bdiag]
labels = ['vertical', 'forward diagonal', 'horizontal', 'backward diagonal']
fig, ax = plt.subplots(1, 4, figsize=(14, 5))

for i, k in enumerate(kernels):
    filt = filters.edges.convolve(cameraman, k)
    ax[i].imshow(filt, cmap='gray', vmin=0, vmax=1)
    ax[i].set_title(labels[i])
    ax[i].grid(False)
    ax[i].set_xticks([])
    ax[i].set_yticks([])
fig.tight_layout()
fig.savefig(root + 'four_directions.png', **savekw)

# %%


def plot_kernel(ax, k, t, fs=18):
    img = np.ones_like(k)
    n = 3
    lw = 2
    ax.imshow(img, vmin=0, vmax=1, extent=[0, n, n, 0], cmap='gray')
    ax.grid(True, lw=lw, color='0')
    ax.set_title(t)
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    for s in ax.spines:
        ax.spines[s].set_color('0')
        ax.spines[s].set_linewidth(lw)
    for i in range(n):
        for j in range(n):
            txt = str(int(k[i, j]))
            ax.text(j + 0.5, i + 0.5, txt,
                    ha='center', va='center', fontsize=fs)


# prewitt operators - have a smoothing effect
prewitt_a = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewitt_b = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_d = np.array([[-1, -1, 0], [-1, 0, 1], [0, 1, 1]])

prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
prewitt_e = np.array([[0, -1, -1], [1, 0, -1], [1, 1, 0]])
prewitt_f = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
prewitt_g = np.array([[1, 1, 0], [1, 0, -1], [0, -1, -1]])

prewitts = [prewitt_a, prewitt_b, prewitt_x, prewitt_d,
            prewitt_y, prewitt_e, prewitt_f, prewitt_g]
labels = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']

fig, axs = plt.subplots(2, 4, figsize=(10, 6))
ax = axs.flatten()
for i, k in enumerate(prewitts):
    plot_kernel(ax[i], k, labels[i])
fig.suptitle('Prewitt operators', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'prewitts.png', **savekw)

# %%

fig, axs = plt.subplots(2, 4, figsize=(12, 8))
ax = axs.flatten()
for i, k in enumerate(prewitts):
    filt = filters.edges.convolve(cameraman, k)
    ax[i].imshow(filt, cmap='gray', vmin=0, vmax=1)
    ax[i].set_title(labels[i])
    ax[i].grid(False)
    ax[i].set_xticks([])
    ax[i].set_yticks([])
fig.suptitle('Prewitt operators', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'cameraman_prewitts.png', **savekw)

# %%

# sobel operators - have a smoothing effect
sobel_a = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
sobel_b = np.array([[0, 1, 2], [-1, 0, 1], [-2, -1, 0]])
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_d = np.array([[-2, -1, 0], [-1, 0, 1], [0, 1, 2]])

sobel_e = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
sobel_f = np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]])
sobel_g = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
sobel_h = np.array([[2, 1, 0], [1, 0, -1], [0, -1, -2]])

sobels = [sobel_a, sobel_b, sobel_x, sobel_d,
          sobel_e, sobel_f, sobel_g, sobel_h]
labels = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']

fig, axs = plt.subplots(2, 4, figsize=(10, 6))
ax = axs.flatten()
for i, k in enumerate(sobels):
    plot_kernel(ax[i], k, labels[i])
fig.suptitle('Sobel operators', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'sobels.png', **savekw)

# %%

fig, axs = plt.subplots(2, 4, figsize=(12, 8))
ax = axs.flatten()
for i, k in enumerate(sobels):
    filt = filters.edges.convolve(cameraman, k)
    ax[i].imshow(filt, cmap='gray', vmin=0, vmax=1)
    ax[i].set_title(labels[i])
    ax[i].grid(False)
    ax[i].set_xticks([])
    ax[i].set_yticks([])
fig.suptitle('Sobel operators', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'cameraman_sobels.png', **savekw)

# %%
