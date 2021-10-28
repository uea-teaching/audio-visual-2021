# %%
import matplotlib.patches as patches
import numpy as np
from skimage import data, io, filters, transform, feature
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

savekw = dict(bbox_inches='tight')

# %%

root = '../lectures/assets/plots2/'
cameraman = io.imread('../lectures/assets/plots1/cameraman.png')
barry = io.imread(root + 'barry.png')

# %%


def plot_image_no_ticks(ax, img, interpolation='antialiased'):
    print(interpolation)
    cm = plt.cm.gray if len(img.shape) == 2 else None
    ax.imshow(img, vmin=0, vmax=255, cmap=cm, interpolation=interpolation)
    ax.axes.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

# %%


def plot_canny():
    fig, ax = plt.subplots(1, 1, figsize=(5, 5), tight_layout=True)
    ax.imshow(feature.canny(cameraman, sigma=3.0),  cmap="gray")
    ax.axes.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig(root + 'cameraman-canny.png', **savekw)
    plt.close(fig)


plot_canny()

# %%


def plot_barry_rgb():
    fig, ax = plt.subplots(1, 1, figsize=(6, 5), tight_layout=True)
    plot_image_no_ticks(ax, barry)
    fig.savefig(root + 'barry-rgb.png', **savekw)
    plt.close(fig)


plot_barry_rgb()

# %%


def norm_rgb(img):
    rgb = img.sum(axis=2)
    nrgb = img / rgb[..., None]
    nrgb -= nrgb.min()
    nrgb /= nrgb.max()
    return nrgb


def plot_norm_rgb():
    fig, ax = plt.subplots(1, 1, figsize=(6, 5), tight_layout=True)
    img = norm_rgb(barry)
    plot_image_no_ticks(ax, img)
    fig.savefig(root + 'norm-rgb.png', **savekw)
    plt.close(fig)


plot_norm_rgb()

# %%

x, y, w, h = 610, 430, 30, 10


def plot_norm_rect():
    fig, ax = plt.subplots(1, 1, figsize=(6, 5), tight_layout=True)
    img = norm_rgb(barry)
    plot_image_no_ticks(ax, img)
    rect = patches.Rectangle(
        (x, y), w, h, linewidth=1, edgecolor='w', facecolor='none')
    ax.add_patch(rect)
    fig.savefig(root + 'norm-rgb-rect.png', **savekw)
    plt.close(fig)


plot_norm_rect()

# %%

t = 0.05


def thres_img():
    img = norm_rgb(barry)
    mu = img[y:y+h, x:x+w, :].reshape(-1, 3).mean(0)
    dist = np.sqrt(np.sum((img - mu) ** 2, -1))
    timg = dist < t
    return timg


def plot_norm_threshold():
    fig, ax = plt.subplots(1, 1, figsize=(6, 5), tight_layout=True)
    timg = thres_img()
    ax.imshow(timg,  cmap="gray")
    ax.axes.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig(root + 'norm-rgb-threshold.png', **savekw)
    plt.close(fig)


plot_norm_threshold()

# %%

arrow = dict(
    color='red',
    linewidth=2,
    head_length=15,
    head_width=15,
    length_includes_head=True)


def plot_w_h_threshold():
    fig, ax = plt.subplots(1, 1, figsize=(6, 5), tight_layout=True)
    timg = thres_img()
    ax.imshow(timg,  cmap="gray")
    ax.axes.set_aspect('equal')
    ax.arrow(550, 450, 120, 0, **arrow)
    ax.text(600, 500, 'w', color="r")
    ax.arrow(550, 450, 0, -60, **arrow)
    ax.text(500, 425, 'h', color="r")
    ax.set_xticks([])
    ax.set_yticks([])
    fig.savefig(root + 'artic-features.png', **savekw)
    plt.close(fig)


plot_w_h_threshold()
