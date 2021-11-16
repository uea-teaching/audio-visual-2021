# %%

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

cameraman = plt.imread('../lectures/assets/plots1/cameraman.png')
astronaut = plt.imread('../lectures/assets/plots1/astronaut.png')

# %%


def imshow_gray(ax, img):
    vmax = 255 if img.dtype == np.uint8 else 1
    h, w = img.shape[:2]
    ax.imshow(img, cmap="gray",
              extent=[0, w, h, 0],
              vmin=0, vmax=vmax, interpolation='none')


x, y, w, h = 126, 61, 8, 8
region = (cameraman[y:y+h, x:x+w] * 255).astype(np.uint8)

rect = patches.Rectangle(
    (x, y), w, h, linewidth=2, edgecolor='r', facecolor='none')

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
imshow_gray(ax[0], cameraman)
ax[0].add_patch(rect)
ax[0].grid(False)
ax[0].set_title('Original')
ax[0].set_xticks([0, 128, 256])
ax[0].set_yticks([0, 128, 256])
imshow_gray(ax[1], region)
ax[1].set_title('Region')
ax[1].set_ylabel('pixels')
ax[1].yaxis.set_label_position("right")
fig.tight_layout()
fig.savefig(root + 'region_8x8.png', **savekw)

# %%


def outline(ax, w, h, lw=2):
    ax.set_yticks(np.arange(0, h, 1))
    ax.set_xticks(np.arange(0, w, 1))
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.grid(True, color='k',  linewidth=2)
    for s in ax.spines:
        ax.spines[s].set_color('0')
        ax.spines[s].set_linewidth(lw)


def text_values(ax, w, h, img=None):
    for i in range(h):
        for j in range(w):
            v = '  ' if img is None else img[i, j]
            ax.text(j + 0.5, i + 0.5, v, ha='center', va='center', fontsize=16)


def show_values(ax, img, bg=None, cmap=None):
    h, w = img.shape[:2]
    vmax = 255 if img.dtype == np.uint8 else 1
    if bg is None:
        bg = np.ones_like(img) * vmax
    ax.imshow(bg, cmap=cmap,
              extent=[0, w, h, 0],
              vmin=0, vmax=vmax, interpolation='none')
    text_values(ax, w, h, img)
    outline(ax, w, h)


h = np.array(sorted([i for i in region[:3, :3].flatten()])).reshape(-1, 1)


# %%

bg1 = (np.ones([8, 8, 3]) * 255).astype(np.uint8)
bg2 = (np.ones([9, 1, 3]) * 255).astype(np.uint8)
bg3 = (np.ones([8, 8, 3]) * 255).astype(np.uint8)

bg1[:3, :3, :] = (230, 180, 180)


fig, ax = plt.subplots(1, 2, figsize=(11, 6))
show_values(ax[0], region, bg1)
ax[0].set_title('Input Image', y=1.02)

ax[1].imshow(bg3, cmap='gray', extent=[0, 8, 8, 0],
             vmin=0, vmax=255, interpolation='none')
outline(ax[1], 8, 8)
ax[1].set_title('Output Image', y=1.02)
fig.suptitle('Window Region', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'region_select.png', **savekw)

# %%

bg1 = (np.ones([8, 8, 3]) * 255).astype(np.uint8)
bg2 = (np.ones([9, 1, 3]) * 255).astype(np.uint8)
bg3 = (np.ones([8, 8, 3]) * 255).astype(np.uint8)

bg1[:3, :3, :] = (230, 180, 180)
bg2[:, :, :] = (230, 180, 180)


fig, ax = plt.subplots(1, 3, figsize=(11, 6), gridspec_kw={
    'width_ratios': [10, 1.2, 10]})
show_values(ax[0], region, bg1)
ax[0].set_title('Input Image', y=1.02)

show_values(ax[1], h, bg2)
# ax[1].set_title('Ordered', y=1.04)
outline(ax[1], 1, 9)

ax[2].imshow(bg3, cmap='gray', extent=[0, 8, 8, 0],
             vmin=0, vmax=255, interpolation='none')
outline(ax[2], 8, 8)
ax[2].set_title('Output Image', y=1.02)
fig.suptitle('Ordered Values', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'region_ordered.png', **savekw)


# %%

idx = 4
bg = (np.ones([8, 8, 3]) * 255).astype(np.uint8)
bg2 = (np.ones([9, 1, 3]) * 255).astype(np.uint8)
bg3 = (np.ones([8, 8, 3]) * 255).astype(np.uint8)

bg[:3, :3, :] = (230, 180, 180)
bg2[idx, 0, :] = (180, 230, 180)
bg3[1, 1, :] = (180, 230, 180)


fig, ax = plt.subplots(1, 3, figsize=(11, 6), gridspec_kw={
    'width_ratios': [10, 1.2, 10]})
show_values(ax[0], region, bg)
ax[0].set_title('Input Image', y=1.02)
show_values(ax[1], h, bg2)
# ax[1].set_title('Ordered', y=1.02)
ax[2].imshow(bg3, cmap='gray', extent=[0, 8, 8, 0],
             vmin=0, vmax=255, interpolation='none')
outline(ax[2], 8, 8)
ax[2].text(1.5, 1.5, str(h[idx, 0]), ha='center', va='center', fontsize=16)
ax[2].set_title('Output Image', y=1.02)
fig.suptitle('Median Filter', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'region_median.png', **savekw)

# %%

idx = 0
bg = (np.ones([8, 8, 3]) * 255).astype(np.uint8)
bg2 = (np.ones([9, 1, 3]) * 255).astype(np.uint8)
bg3 = (np.ones([8, 8, 3]) * 255).astype(np.uint8)

bg[:3, :3, :] = (230, 180, 180)
bg2[idx, 0, :] = (180, 230, 180)
bg3[1, 1, :] = (180, 230, 180)


fig, ax = plt.subplots(1, 3, figsize=(11, 6), gridspec_kw={
    'width_ratios': [10, 1.2, 10]})
show_values(ax[0], region, bg)
ax[0].set_title('Input Image', y=1.02)
show_values(ax[1], h, bg2)
# ax[1].set_title('Ordered', y=1.02)
ax[2].imshow(bg3, cmap='gray', extent=[0, 8, 8, 0],
             vmin=0, vmax=255, interpolation='none')
outline(ax[2], 8, 8)
ax[2].text(1.5, 1.5, str(h[idx, 0]), ha='center', va='center', fontsize=16)
ax[2].set_title('Output Image', y=1.02)
fig.suptitle('Min Filter', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'region_min.png', **savekw)

# %%

idx = 8
bg = (np.ones([8, 8, 3]) * 255).astype(np.uint8)
bg2 = (np.ones([9, 1, 3]) * 255).astype(np.uint8)
bg3 = (np.ones([8, 8, 3]) * 255).astype(np.uint8)

bg[:3, :3, :] = (230, 180, 180)
bg2[idx, 0, :] = (180, 230, 180)
bg3[1, 1, :] = (180, 230, 180)


fig, ax = plt.subplots(1, 3, figsize=(11, 6), gridspec_kw={
    'width_ratios': [10, 1.2, 10]})
show_values(ax[0], region, bg)
ax[0].set_title('Input Image', y=1.02)
show_values(ax[1], h, bg2)
# ax[1].set_title('Ordered', y=1.02)
ax[2].imshow(bg3, cmap='gray', extent=[0, 8, 8, 0],
             vmin=0, vmax=255, interpolation='none')
outline(ax[2], 8, 8)
ax[2].text(1.5, 1.5, str(h[idx, 0]), ha='center', va='center', fontsize=16)
ax[2].set_title('Output Image', y=1.02)
fig.suptitle('Max Filter', fontsize=20)
fig.tight_layout()
fig.savefig(root + 'region_max.png', **savekw)
