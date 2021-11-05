# %%

import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.transform as tf
import dlib
import os

import matplotlib.patches as patches
import matplotlib.gridspec as gridspec

plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=160)

MODEL = os.path.expanduser(
    "~/.dg/dlib/shape_predictor_68_face_landmarks_GTX.dat")
DETECTOR = dlib.get_frontal_face_detector()
PREDICTOR = dlib.shape_predictor(MODEL)

# %%

# data:

tri = np.load('dlib68_tris.npz')['tris']
pos = np.load('dlib68_tris.npz')['landmarks']


root = "../lectures/assets/img4/"
save_root = "../lectures/assets/plots2/"

images = [(plt.imread(f) * 255).astype(np.uint8) for f in
          [root + "ken_00.png", root + "ken_01.png",
           root + "ken_02.png", root + "ken_03.png"]]

tidx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 20, 22, 23,
        24, 29, 30, 34, 35, 36, 57, 58, 59, 60, 61, 64, 65,
        66, 67, 68, 69, 70, 73, 74, 75, 86, 87, 88, 89, 90,
        91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 103, 104, 105, 106]

# %%


def landmarks(img):
    """return the landmarks"""
    try:
        rect = DETECTOR(img, 0)[0]
        shape = PREDICTOR(img, rect)
        lmks = [(shape.part(i).x, shape.part(i).y) for i in range(68)]
    except:
        print("No face detected")
        return None
    return lmks


def pad_image(img):
    # print(img.shape, img.dtype)
    h, w = img.shape[:2]
    out = np.zeros([max(h, 512), max(w, 512), 3], dtype=img.dtype)
    out[:h, :w, :] = img
    return out


def inverse_transform(a, b):
    """find M when M@A=B, return A, B, M"""
    row = np.array((1, 1, 1))[..., None]
    A = np.hstack([a, row]).T
    B = np.hstack([b, row]).T
    M = np.linalg.inv(B @ np.linalg.inv(A))
    return M


def get_poly(b):
    return np.array([b[:, 1], b[:, 0]]).T


def plot_shape(ax, pos, tri, lw=2, color='k'):
    ax.triplot(pos[:, 0], pos[:, 1], tri, lw=lw, color=color)
    ax.set_xlim(0, 512)
    ax.set_ylim(512, 0)
    ax.set_aspect('equal')


def warped_face(img, lmk):

    out_image = np.zeros([512, 512, 3])
    out_mask = np.zeros([512, 512])
    in_image = pad_image(img)

    for i in tidx:
        a, b = lmk[tri[i]],  pos[tri[i]]
        poly = get_poly(b)
        M = inverse_transform(a, b)
        warped = tf.warp(in_image, M, clip=False, mode="constant", cval=0)
        wmask = skimage.draw.polygon2mask(warped.shape[:2], poly)
        omask = skimage.draw.polygon2mask(out_image.shape[:2], poly)

        s1, s2 = omask.sum(), wmask.sum()
        if s1 != s2:
            print("mask mismatch", i, s1, s2)
            continue

        out_image[omask] = warped[wmask]
        out_mask[omask] = 1

    return np.concatenate([out_image, out_mask[..., None]], axis=-1)


# %%

# processing
lmks = np.array([landmarks(img) for img in images])
warps = [warped_face(img, lmk) for img, lmk in zip(images, lmks)]


# %%

fig, ax = plt.subplots(1, 2, figsize=(10, 6))
ax[0].imshow(images[0])
ax[0].plot(lmks[0, :, 0], lmks[0, :, 1], 'o')
ax[0].grid(False)
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_title("Landmarks")

for i, k in enumerate(tri):
    t = pos[k]
    c = np.mean(t, axis=0)
    t = np.concatenate([t, t[:1]])
    ax[1].plot(t[:, 0], t[:, 1], '-o')

ax[1].grid(False)
ax[1].set_xticks([])
ax[1].set_yticks([])
ax[1].set_ylim(600, -50)
ax[1].set_aspect('equal')
ax[1].set_title("Triangulated Shape")
plt.tight_layout()

fig.savefig(save_root + "triangulate_lmks.png", **savekw)


# %%

fig, ax = plt.subplots(1, figsize=(10, 10))
for i in tidx:
    t = pos[tri[i]]
    c = np.mean(t, axis=0)
    t = np.concatenate([t, t[:1]])
    ax.plot(t[:, 0], t[:, 1], '-o')
    ax.text(c[0], c[1], str(i), fontdict={'size': 12})
    ax.set_xlabel("pixels")
    ax.set_ylabel("pixels")
    ax.set_ylim(550, 200)
    ax.set_aspect('equal')
    ax.set_title("Triangulated Mouth Shape")

plt.tight_layout()
fig.savefig(save_root + "mouth_triangulation.png", **savekw)


# %%

idx = 0


def shape_norm(idx):
    fig = plt.figure(figsize=(10, 8))
    gs = gridspec.GridSpec(ncols=2, nrows=1, figure=fig,
                           width_ratios=[1, 400/350.])

    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])

    ax1.imshow(images[idx])
    ax1.triplot(lmks[idx][:, 0], lmks[idx][:, 1], tri[tidx], lw=1, color='r')
    ax1.set_xlabel("pixels")
    ax1.set_ylabel("pixels")

    ax2.imshow(warps[idx])
    ax2.set_xlim([0, 512])
    ax2.set_ylim([550, 200])
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title("Normalised Appearance")
    fig.tight_layout()
    fig.suptitle("Shape Normalisation - Image {}".format(idx),
                 fontsize=24, y=0.9)
    plt.close(fig)
    return fig


for i in range(4):
    fig = shape_norm(i)
    fig.savefig(save_root + "shape_norm_{}.png".format(i), **savekw)
