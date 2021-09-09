# %%
import numpy as np
from skimage import data, io, filters, transform
import matplotlib.pyplot as plt

plt.style.use('classic')
plt.rcParams['savefig.facecolor'] = '0.85'
plt.rcParams['savefig.dpi'] = 100
plt.rcParams['font.size'] = 14

# %%
root = 'lectures/assets/plots1/'
cameraman = io.imread(root + 'cameraman.png')
astronaut = io.imread(root + 'astronaut.png')

# %%


def plot_image_no_ticks(ax, img, interpolation='antialiased'):
    print(interpolation)
    cm = plt.cm.gray if len(img.shape) == 2 else None
    ax.imshow(img, vmin=0, vmax=255, cmap=cm, interpolation=interpolation)
    ax.axes.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])


def plot_image(ax, img, interpolation='antialiased'):
    h, w = img.shape[0] - 1, img.shape[1] - 1
    plot_image_no_ticks(ax, img, interpolation)
    ax.axes.set_aspect('equal')
    ax.set_xticks([0, w//2, w])
    ax.set_yticks([0, h//2, h])
    ax.set_xlim([0, w])
    ax.set_ylim([h, 0])


def plot_tone_curve(ax, x, y):
    lim = [0, 255]
    ax.plot(x, x, '--k', label='original')
    ax.plot(x, y, label='mapped')
    ax.set_xticks(lim)
    ax.set_yticks(lim)
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.axes.set_aspect('equal')
    ax.set_xlabel('input intensity')
    ax.set_ylabel('output intensity')
    ax.legend(fontsize=12, loc=2)


def plot_in_out(ax, inval, func):
    vx = inval
    vy = func(np.array([vx, ]))[0]
    ax.plot([vx, vx], [0, vy], '--r')
    ax.plot([0, vx], [vy, vy], '--r')
    ax.text(vx + 5, 10, f'{vx}', color='r', fontsize=12)
    ax.text(10, vy + 5, f'{vy}', color='r', fontsize=12)


def gamma(img, val):
    return 255 * (img / 255) ** (1.0 / val)


tones = {
    't1': lambda x: x.astype(np.uint8),
    't2': lambda x: (x * 0.7).astype(np.uint8),
    't3': lambda x: (x * 0.5 + 90).astype(np.uint8),
    't4': lambda x: np.clip(x * 1.6 - 90, 0, 255).astype(np.uint8),
}

titles = {
    't1': r'$f(I) = I$',
    't2': r'$f(I) = I * 0.7$',
    't3': r'$f(I) = I * 0.5 + 90$',
    't4': r'$f(I) = I * 1.6 - 90$',
}

gvals = {
    'g2': 0.7,
    'g3': 1.5,
    'g4': 2.2,
}

gtitles = {
    'g1': r'$\gamma = 1$',
    'g2': r'$\gamma = 0.7$',
    'g3': r'$\gamma = 1.5$',
    'g4': r'$\gamma = 2.2$',
}

# %%


def plot_value(img):
    i = img[150, 200]
    fig, ax = plt.subplots(1, 1, figsize=(5, 5), tight_layout=True)
    ax.plot([0, 200], [150, 150], '-r')
    ax.plot([200, 200], [0, 150], '-r')
    ax.scatter([200, ], [150, ], color='r', marker='x', s=90, linewidth=2)
    ax.set_title(rf"$I(x=200, y=150)={i}$", fontsize=18)
    plot_image(ax, img)
    fig.savefig(root + 'cam-coord.png', bbox_inches='tight')
    plt.close(fig)


plot_value(cameraman)

# %%


def plot_rgb(img):
    fig, ax = plt.subplots(1, 4, figsize=(12, 5), tight_layout=True)
    plot_image_no_ticks(ax[0], img)
    ax[0].set_title('RGB')

    for i, title in enumerate(['Red', 'Green', 'Blue']):
        plot_image_no_ticks(ax[i + 1], img[..., i])
        ax[i + 1].set_title(title)

    fig.savefig(root + 'astronaut-rgb.png', bbox_inches='tight')
    plt.close(fig)


plot_rgb(astronaut)

# %%


def plot_resolutions(img, interpolation='none'):
    sizes = ((256, 256), (128, 128), (64, 64), (16, 16))
    fig, ax = plt.subplots(1, 4, figsize=(12, 5), tight_layout=True)
    for i, size in enumerate(sizes):
        scaled = transform.resize(
            cameraman, size, anti_aliasing=False, preserve_range=True)
        plot_image_no_ticks(ax[i], scaled, interpolation=interpolation)
        ax[i].set_title(f'{size[0]} X {size[1]}')

    fig.savefig(root + f'sampling-{interpolation}.png', bbox_inches='tight')
    plt.close(fig)


plot_resolutions(cameraman)
plot_resolutions(cameraman, interpolation='bicubic')


# %%


def plot_levels(img):
    levels = (256, 64, 16, 4)
    fig, ax = plt.subplots(1, 4, figsize=(
        12, 5), tight_layout=True, sharey=True)
    for i, level in enumerate(levels):
        d = 256 // level
        lev = (img // d) * d
        plot_image_no_ticks(ax[i], lev)
        ax[i].set_title(f'levels: {level}')

    fig.savefig(root + 'levels.png', bbox_inches='tight')
    plt.close(fig)


plot_levels(cameraman)
# %%


def plot_tone_mapping(key):
    """big plots!!"""
    x = np.linspace(0, 255, 256)
    img = cameraman
    func, title = tones[key], titles[key]

    fig, ax = plt.subplots(1, 3, figsize=(11, 5), tight_layout=True)
    plot_tone_curve(ax[0], x, func(x))
    ax[0].set_title(title, fontsize=18)
    plot_image_no_ticks(ax[1], img)
    ax[1].set_title('input image')
    plot_image_no_ticks(ax[2], func(img))
    ax[2].set_title('output image')
    fig.savefig(root + f'tone-{key}-00.png', bbox_inches='tight')
    plt.close(fig)
    fig, ax = plt.subplots(1, 1, figsize=(5, 5), tight_layout=True)
    plot_tone_curve(ax, x, func(x))
    ax.set_title(title, fontsize=18)
    fig.savefig(root + f'tone-{key}-01.png', bbox_inches='tight')
    plt.close(fig)
    fig, ax = plt.subplots(1, 1, figsize=(5, 5), tight_layout=True)
    plot_tone_curve(ax, x, func(x))
    plot_in_out(ax, 127, func)
    ax.set_title(title, fontsize=18)
    fig.savefig(root + f'tone-{key}-02.png', bbox_inches='tight')
    plt.close(fig)


for key in tones:
    plot_tone_mapping(key)

# %%


def plot_gamma_curves():
    x = np.linspace(0, 255, 256)
    fig, ax = plt.subplots(1, figsize=(5, 5), tight_layout=True)

    for key in gvals:
        y = np.clip(gamma(x, gvals[key]), 0, 255)
        title = gtitles[key]
        ax.plot(x, y, label=title)

    y = np.clip(gamma(x, 1.0), 0, 255)
    title = gtitles['g1']
    ax.plot(x, y, 'k', label=title)

    ax.set_xticks([0, 128, 255])
    ax.set_yticks([0, 128, 255])
    ax.set_xlim([0, 255])
    ax.set_ylim([0, 255])
    ax.set_ylabel('output intensity')
    ax.set_xlabel('input intensity')
    ax.legend(fontsize=12, loc=2)
    ax.set_title('gamma curves')
    fig.savefig(root + 'gamma-curves.png', bbox_inches='tight')
    plt.close(fig)


plot_gamma_curves()

# %%


def plot_gamma_img(img):
    orig = img.copy()
    fig, ax = plt.subplots(1, 4, figsize=(11, 5), tight_layout=True)
    plot_image_no_ticks(ax[0], orig)
    ax[0].set_title('original', fontsize=18)

    for i, key in enumerate(gvals):
        img = gamma(orig, gvals[key])
        title = gtitles[key]
        plot_image_no_ticks(ax[i + 1], img)
        ax[i + 1].set_title(title, fontsize=18)

    fig.savefig(root + 'gamma.png', bbox_inches='tight')
    plt.close(fig)


plot_gamma_img(cameraman)

# %%


def plot_hist_image(img):
    fig, ax = plt.subplots(1, 2, figsize=(9, 5), tight_layout=True)
    plot_image_no_ticks(ax[1], img)
    ax[1].set_title('image', fontsize=18)
    ax[0].hist(
        img.flat,
        edgecolor='grey', facecolor='grey',
        bins=256, range=(0, 255))
    ax[0].set_yticks([0, 400, 800, 1200])
    ax[0].set_ylim([0, 1200])
    ax[0].set_xlim([0, 255])
    ax[0].set_xlabel('intensity')
    ax[0].set_ylabel('frequency')
    asp = np.diff(ax[0].get_xlim())[0] / np.diff(ax[0].get_ylim())[0]
    ax[0].set_aspect(asp)
    ax[0].set_title('histogram')
    fig.savefig(root + 'hist-01.png', bbox_inches='tight')
    plt.close(fig)


def plot_hist(img):
    fig, ax = plt.subplots(1, figsize=(5, 5), tight_layout=True)
    ax.hist(
        img.flat,
        edgecolor='grey', facecolor='grey',
        bins=256, range=(0, 255))
    ax.set_yticks([0, 400, 800, 1200])
    ax.set_ylim([0, 1200])
    ax.set_xlim([0, 255])
    ax.set_xlabel('intensity')
    ax.set_ylabel('frequency')
    ax.set_title('histogram')
    fig.savefig(root + 'hist-02.png', bbox_inches='tight')
    plt.close(fig)


plot_hist(cameraman)
plot_hist_image(cameraman)

# %%


def plot_threshold_image(img, t):
    timg = (img > t) * 255
    fig, ax = plt.subplots(1, 2, figsize=(9, 5), tight_layout=True)
    plot_image_no_ticks(ax[1], timg)
    ax[1].set_title('image > t', fontsize=18)
    ax[0].hist(
        img.flat,
        edgecolor='grey', facecolor='grey',
        bins=256, range=(0, 255))
    ax[0].set_yticks([0, 400, 800, 1200])
    ax[0].set_ylim([0, 1200])
    ax[0].set_xlim([0, 255])
    ax[0].set_xlabel('intensity')
    ax[0].set_ylabel('frequency')
    asp = np.diff(ax[0].get_xlim())[0] / np.diff(ax[0].get_ylim())[0]
    ax[0].set_aspect(asp)
    ax[0].plot([t, t], ax[0].get_ylim(), 'r--', label=f'$t={t}$')
    ax[0].legend(fontsize=12, loc=1)
    ax[0].set_title('histogram')
    fig.savefig(root + 'threshold-01.png', bbox_inches='tight')
    plt.close(fig)


plot_threshold_image(cameraman, 75)
