# %%
import json
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# %%
# Load data and centre it
with open('lmk_recG001_crop.json') as fid:
    mouths = np.array(json.load(fid), dtype=np.float64)[:, 48:, :]
    mouths -= np.mean(mouths, axis=1, keepdims=True)

# %%


def norm_outer(mouths):
    """Return just the outer perimeter normalised to 2pi"""
    idx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
    outer = mouths[:, idx[:-1], :]
    a, b = outer[:, idx[:-1], :], outer[:, idx[1:], :]
    outer_len = (((a - b) ** 2).sum(axis=-1) ** 0.5).sum(axis=1)
    return outer * 2 * np.pi / outer_len[:, None, None]


outer_norm = norm_outer(mouths)
# centroids are at (0, 0)
centroid_dists = np.linalg.norm(outer_norm, axis=-1)

# %%

# pick a few frames to plot
choice = [10, 100, 200, 300, 400]
mouth = outer_norm[choice, :, :]
dist = centroid_dists[choice, :]

# %%

frm = 4
lmk = 5


def fourier_mouth(mouth, dist, frm, lmk):

    loop = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]

    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    ax[0].plot(mouth[frm, loop, 0], mouth[frm, loop, 1], '-o')
    ax[0].plot([0, mouth[frm, lmk, 0]], [0, mouth[frm, lmk, 1]])

    dd = dist.flatten()[:frm*12+lmk+1]
    for x, y in enumerate(dd):
        ax[1].plot([x, x], [0, y], 'k', lw=1.5, alpha=0.5)
        ax[1].plot(x, y, 'rx')

    ax[0].set_aspect('equal')
    ax[0].set_title(f'Lip Contour - Frame: {frm+1:02d}')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('y')
    ax[0].set_xlim(-1.5, 1.5)
    ax[0].set_ylim(-1.5, 1.5)
    ax[0].set_xticks([-1.0, 0, 1.0])
    ax[0].set_yticks([-1.0, 0, 1.0])

    ax[1].set_xlabel('Frame')
    ax[1].set_ylabel('Distance')
    ax[1].set_title('Distance From Centroid')
    ax[1].set_xticks([-1, 12, 24, 36, 48, 60, 72])
    ax[1].set_xlim(-1, 72)
    ax[1].set_xticklabels(['', '1', '2', '3', '4', '5', ''])
    ax[1].set_ylim([0, 3])
    ax[1].set_yticks([0.5, 1.5, 2.5])
    plt.close(fig)

    return fig


fig = fourier_mouth(mouth, dist, frm, lmk)
fig


# %%

fname = '/Users/Shared/tmp/fd_{n:02d}.png'

for frm in range(5):
    for lmk in range(12):
        fig = fourier_mouth(mouth, dist, frm, lmk)
        fig.savefig(fname.format(n=frm*12+lmk), bbox_inches='tight')
        plt.close(fig)

# %%

"""
Make a video:
ffmpeg -f image2 
    -framerate 15 \
    -i fd_%02d.png \
    out.gif
"""
