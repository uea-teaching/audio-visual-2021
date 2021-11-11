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


# %%

n, m = 85, 188
mini = astronaut[n:n+30, m:m+30]

fig, ax = plt.subplots(1, figsize=(5, 5))
ax.imshow(mini, cmap='gray',
          vmin=0, vmax=1, interpolation='none')
ax.grid(False)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
fig.savefig(root + 'astroeye.png', **savekw)

# %%

fig, ax = plt.subplots(1, figsize=(5, 5))
ax.imshow(np.ones([9, 9]) * 0.5, cmap='gray', vmin=0, vmax=1)
ax.grid(False)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.text(4, 4, '?', ha='center', va='center', fontsize=98)
fig.savefig(root + 'question.png', **savekw)

# %%
