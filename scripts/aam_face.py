# %%

import numpy as np
import matplotlib.pyplot as plt
import skimage
import skimage.transform as tf
import dlib
import os

MODEL = os.path.expanduser(
    "~/.dg/dlib/shape_predictor_68_face_landmarks_GTX.dat")
DETECTOR = dlib.get_frontal_face_detector()
PREDICTOR = dlib.shape_predictor(MODEL)

# %%

# data:

tri = np.load('dlib68_tris.npz')['tris']
pos = np.load('dlib68_tris.npz')['landmarks']


root = "../lectures/assets/img4/"
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
    print(img.shape, img.dtype)
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


def plot_shape(ax, pos, tri):
    ax.triplot(pos[:, 0], pos[:, 1], tri)
    ax.set_xlim(0, 512)
    ax.set_ylim(512, 0)
    ax.set_aspect('equal')


# %%

lmks = np.array([landmarks(img) for img in images])

# %%

fig, ax = plt.subplots(figsize=(10, 10))
plot_shape(ax, pos, tri)


# %%


mean_shape = lmks.mean(axis=0)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(images[0])
ax.plot(lmks[0, :, 0], lmks[0, :, 1], 'o')
ax.plot(mean_shape[:, 0], mean_shape[:, 1], 'o')

# %%

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
for i, k in enumerate(tri):
    t = pos[k] * (1, -1)
    c = np.mean(t, axis=0)
    t = np.concatenate([t, t[:1]])
    ax.plot(t[:, 0], t[:, 1], '-o')
    ax.text(c[0], c[1], str(i), fontdict={'size': 10})


# %%

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
for i in tidx:
    t = pos[tri[i]] * (1, -1)
    c = np.mean(t, axis=0)
    t = np.concatenate([t, t[:1]])
    ax.plot(t[:, 0], t[:, 1], '-o')
    ax.text(c[0], c[1], str(i), fontdict={'size': 12})
    ax.set_aspect('equal')


fig, ax = plt.subplots(1, 1, figsize=(10, 10))
for i in tidx:
    t = lmks[0][tri[i]] * (1, -1)
    c = np.mean(t, axis=0)
    t = np.concatenate([t, t[:1]])
    ax.plot(t[:, 0], t[:, 1], '-o')
    ax.text(c[0], c[1], str(i), fontdict={'size': 12})
    ax.set_aspect('equal')


# %%

# plot images with landmarks
img = images[0]
h, w = img.shape[:2]
fig, ax = plt.subplots(1, 2, figsize=(12, 10))
ax[0].imshow(img)
plot_shape(ax[0], lmks[0], tri[tidx])
ax[0].set_ylim(h-1, 0)
ax[0].set_xlim(0, w-1)
plot_shape(ax[1], pos, tri[tidx])

# %%


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


plt.imshow(warped_face(images[0], lmks[0]))

# %%
