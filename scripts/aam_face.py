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

tri = np.load('dlib68_tris.npz')['tris']
pos = np.load('dlib68_tris.npz')['landmarks']


def plot_shape(ax, pos, tri):
    ax.triplot(pos[:, 0], pos[:, 1], tri)
    ax.set_xlim(0, 512)
    ax.set_ylim(512, 0)
    ax.set_aspect('equal')


fig, ax = plt.subplots(figsize=(10, 10))
plot_shape(ax, pos, tri)


# %%

root = "../lectures/assets/img4/"
images = [(plt.imread(f) * 255).astype(np.uint8) for f in
          [root + "ken_00.png", root + "ken_01.png",
           root + "ken_02.png", root + "ken_03.png"]]

tidx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 20, 22, 23,
        24, 29, 30, 34, 36, 57, 58, 59, 60, 61, 64, 65,
        66, 67, 68, 69, 70, 74, 75, 86, 87, 88, 89, 90,
        91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 103, 104, 105, 106]

# %%

landmarks = []

for k, img in enumerate(images):
    try:
        rect = DETECTOR(img, 0)[0]
        shape = PREDICTOR(img, rect)
        lmks = [(shape.part(i).x, shape.part(i).y) for i in range(68)]
    except:
        print("No face detected", k)
        continue
    landmarks.append(lmks)

landmarks = np.array(landmarks)

# %%

mean_shape = landmarks.mean(axis=0)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(images[0])
ax.plot(landmarks[0, :, 0], landmarks[0, :, 1], 'o')
ax.plot(mean_shape[:, 0], mean_shape[:, 1], 'o')

# %%

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
for i, k in enumerate(tri):
    t = pos[k] * (1, -1)
    c = np.mean(t, axis=0)
    t = np.concatenate([t, t[:1]])
    ax.plot(t[:, 0], t[:, 1], '-o')
    ax.text(c[0], c[1], str(i), fontdict={'size': 10})
fig.savefig('dlib68_tris.png', dpi=300)

# %%

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
for i in tidx:
    t = pos[tri[i]] * (1, -1)
    c = np.mean(t, axis=0)
    t = np.concatenate([t, t[:1]])
    ax.plot(t[:, 0], t[:, 1], '-o')
    ax.text(c[0], c[1], str(i), fontdict={'size': 12})
    ax.set_aspect('equal')
fig.savefig('dlib68_tris_idx.png', dpi=300)

# %%

# plot images with landmarks
img = images[0]
h, w = img.shape[:2]
fig, ax = plt.subplots(1, 2, figsize=(12, 10))
ax[0].imshow(img)
plot_shape(ax[0], landmarks[0], tri[tidx])
ax[0].set_ylim(h-1, 0)
ax[0].set_xlim(0, w-1)
plot_shape(ax[1], pos, tri[tidx])

# %%


def inverse_transform(a, b):
    row = np.array((0, 0, 1))[..., None]
    print(a.shape, b.shape, row.shape)
    A = np.concatenate([a, row], 1)
    B = np.concatenate([b, row], 1)
    return np.linalg.inv(A@B)


D = inverse_transform(landmarks[0, tri[0], :],  pos[tri[0]])
tform = tf.AffineTransform(matrix=D)

# %%
