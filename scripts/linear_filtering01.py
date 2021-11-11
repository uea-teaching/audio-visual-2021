# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


plt.style.use('fivethirtyeight')
savekw = dict(bbox_inches='tight', dpi=120)
root = '../lectures/assets/plots3/'

# %%


def plot_square(ax, n, y_label, x_label, title, data=None, cmap=None,):
    data = np.ones([n, n]) if data is None else data
    pad, lw = 10, 0.5
    ax.imshow(data, extent=[0, n, n, 0],
              interpolation='none', cmap=cmap, vmin=0, vmax=1,)
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticks(np.arange(0, n, 1))
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.grid(True, lw=lw, color='0',)
    ax.set_title(title, pad=pad)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label, rotation=0, labelpad=pad)
    ax.set_aspect('equal')
    for s in ax.spines:
        ax.spines[s].set_color('0')
        ax.spines[s].set_linewidth(lw)


def plot_conv(f=None, h=None, g=None):
    fig, ax = plt.subplots(1, 3, figsize=(10, 8), gridspec_kw={
        'width_ratios': [10, 3, 10]})
    plot_square(ax[0], 10, 'i', 'j', r'$f$', data=f)
    plot_square(ax[1], 3, None, None, r'$h$', data=h)
    plot_square(ax[2], 10, 'i', 'j', r'$g$', data=g)
    fig.tight_layout(w_pad=1.5, h_pad=1.0)
    plt.close(fig)
    return fig, ax


cols = [(1, 0, 0), (0.3, 0.9, 0.3), (0.9, 0.9, 0.3),
        (0.9, 0.3, 0.9), (0.3, 0.9, 0.9), (0.9, 0.6, 0.6), (0.9, 0.9, 0.6)]

# %%


f = np.ones([10, 10, 3])
h = np.ones([3, 3, 3])
g = np.ones([10, 10, 3])
fig, ax = plot_conv(f, h, g)
ax[0].text(0.5, 0.5, r'$0, 0$', ha='center', va='center', fontsize=12)
ax[1].text(1.5, 1.5, r'$0, 0$', ha='center', va='center', fontsize=12)
ax[2].text(0.5, 0.5, r'$0, 0$', ha='center', va='center', fontsize=12)
fig.suptitle('Kernel Coordinates', fontsize=16, y=0.77)
fig.savefig(root + 'kernel_coords.png', **savekw)


# %%

i, j = 1, 1
f = np.ones([10, 10, 3])
h = np.ones([3, 3, 3])
g = np.ones([10, 10, 3])
f[i, j, :] = cols[0]
fig, ax = plot_conv(f, h, g)
# fig.suptitle(r'f(1, 1)', fontsize=16, y=0.3)
fig.savefig(root + 'kernel_11_00.png', **savekw)
fig

# %%
i, j = 1, 1
m, n = -1, -1
f[i-m, j-n, :] = cols[1]
h[i+m, j+n, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.suptitle(fr'm,n = ({m},{n})', fontsize=16, y=0.3, x=0.515)
fig.savefig(root + 'kernel_11_01.png', **savekw)
fig

# %%
i, j = 1, 1
m, n = -1, 0
f[i-m, j-n, :] = cols[2]
h[1+m, 1+n, :] = cols[2]
fig, ax = plot_conv(f, h, g)
fig.suptitle(fr'm,n = ({m},{n})', fontsize=16, y=0.3, x=0.515)
fig.savefig(root + 'kernel_11_02.png', **savekw)

# %%
i, j = 1, 1
m, n = -1, 1
f[i-m, j-n, :] = cols[3]
h[1+m, 1+n, :] = cols[3]
fig, ax = plot_conv(f, h, g)
fig.suptitle(fr'm,n = ({m},{n})', fontsize=16, y=0.3, x=0.515)
fig.savefig(root + 'kernel_11_03.png', **savekw)

# %%
i, j = 1, 1
m, n = 0, -1
f[i-m, j-n, :] = cols[4]
h[1+m, 1+n, :] = cols[4]
fig, ax = plot_conv(f, h, g)
fig.suptitle(fr'm,n = ({m},{n})', fontsize=16, y=0.3, x=0.515)
fig.savefig(root + 'kernel_11_04.png', **savekw)

# %%
i, j = 1, 1
f[:3, :3, :] = cols[5]
f[i, j, :] = cols[0]
h[:, :, :] = cols[6]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + 'kernel_11_all.png', **savekw)
fig

# %%
i, j = 1, 1
f[i-1:i+2, j-1:j+2, :] = cols[5]
f[i, j, :] = cols[0]
h[:, :, :] = cols[6]
g[i, j, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + 'kernel_11_g11.png', **savekw)
fig

# %%

f = np.ones([10, 10, 3])

i, j = 1, 2
f[i-1:i+2, j-1:j+2, :] = cols[5]
f[i, j, :] = cols[0]
g[i, j, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + f'kernel_{i}{j}_g{i}{j}.png', **savekw)
fig

# %%

f = np.ones([10, 10, 3])

i, j = 1, 3
f[i-1:i+2, j-1:j+2, :] = cols[5]
f[i, j, :] = cols[0]
g[i, j, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + f'kernel_{i}{j}_g{i}{j}.png', **savekw)
fig
# %%

f = np.ones([10, 10, 3])
g = np.ones([10, 10, 3])
i, j = 1, 8
f[i-1:i+2, j-1:j+2, :] = cols[5]
f[i, j, :] = cols[0]
g[i, 1:j+1, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + f'kernel_{i}_all_g{i}_all.png', **savekw)
fig

# %%

f = np.ones([10, 10, 3])
g = np.ones([10, 10, 3])
i, j = 2, 1
f[i-1:i+2, j-1:j+2, :] = cols[5]
f[i, j, :] = cols[0]
g[1, 1:9, :] = cols[1]
g[i, j, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + f'kernel_{i}{j}_g{i}{j}.png', **savekw)
fig
# %%

f = np.ones([10, 10, 3])
g = np.ones([10, 10, 3])
i, j = 2, 8
f[i-1:i+2, j-1:j+2, :] = cols[5]
f[i, j, :] = cols[0]
g[1, 1:9, :] = cols[1]
g[i, 1:9, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + f'kernel_{i}{j}_g{i}{j}.png', **savekw)
fig
# %%

f = np.ones([10, 10, 3])
g = np.ones([10, 10, 3])
i, j = 8, 8
f[i-1:i+2, j-1:j+2, :] = cols[5]
f[i, j, :] = cols[0]
g[1:9, 1:9, :] = cols[1]
fig, ax = plot_conv(f, h, g)
fig.savefig(root + f'kernel_{i}{j}_g{i}{j}.png', **savekw)
fig

# %%

f = np.ones([12, 12, 3]) * 0.7
f[1:11, 1:11, :] = 1
f[:3, :3, :] = cols[5]
f[1:3, 1:3, :] = cols[6]
fig, ax = plt.subplots(1, figsize=(7, 7))
plot_square(ax, 12, '', '', '', data=f)
fig.savefig(root + 'conv_edge_00.png', **savekw)


# %%

f = np.ones([12, 12, 3]) * 0.7
f[1:11, 1:11, :] = 1
f[:3, :3, :] = cols[6]
fig, ax = plt.subplots(1, figsize=(7, 7))
plot_square(ax, 12, '', '', '', data=f)
for i in range(12):
    ax.text(i + 0.5, 0.5, '0', fontsize=16, ha='center', va='center')
for i in range(1, 11):
    ax.text(0.5, i + 0.5, '0', fontsize=16, ha='center', va='center')
    ax.text(11.5, i + 0.5, '0', fontsize=16, ha='center', va='center')
for i in range(12):
    ax.text(i + 0.5, 11.5, '0', fontsize=16, ha='center', va='center')

fig.savefig(root + 'conv_edge_zeros.png', **savekw)

# %%

f = np.ones([12, 12, 3]) * 0.7
f[1:11, 1:11, :] = 1
f[:3, :3, :] = cols[6]
f[1:11, 10, :] = cols[3]
fig, ax = plt.subplots(1, figsize=(7, 7))
plot_square(ax, 12, '', '', '', data=f)
for i in range(10):
    ax.arrow(10.5, i + 1.5, -9.75, 0, head_width=0.2,
             head_length=0.3, fc='m', ec='m', lw=2)
fig.savefig(root + 'conv_edge_wrap.png', **savekw)

# %%

f = np.ones([12, 12, 3]) * 0.7
f[1:11, 1:11, :] = 1
f[:3, :3, :] = cols[6]
f[1:11, 10, :] = cols[3]
fig, ax = plt.subplots(1, figsize=(7, 7))
plot_square(ax, 12, '', '', '', data=f)
for i in range(10):
    ax.arrow(10.5, i + 1.5, 0.75, 0, head_width=0.2,
             head_length=0.3, fc='m', ec='m', lw=2)
fig.savefig(root + 'conv_edge_repeat.png', **savekw)

# %%
