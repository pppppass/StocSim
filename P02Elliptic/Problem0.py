
# coding: utf-8

# In[1]:


import numpy
import matplotlib.patches
from matplotlib import pyplot


# In[2]:


x, y = (numpy.linspace(-1.0, 1.0, 200) for _ in range(2))
x, y = x[:, None], y[None, :]


# In[3]:


pyplot.figure(figsize=(5.0, 4.0))
im = pyplot.imshow(((x**2 + y**2) / 2.0).transpose()[::-1, :], vmin=0.0, vmax=0.5, extent=[-1.0, 1.0, -1.0, 1.0])
patch = matplotlib.patches.Circle((0.0, 0.0), radius=1.0, transform=pyplot.gca().transData)
im.set_clip_path(patch)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.colorbar()
pyplot.savefig("Figure18.pgf")
pyplot.show()
pyplot.close()


# In[4]:


pyplot.figure(figsize=(5.0, 4.0))
im = pyplot.imshow((x * y + x - y).transpose()[::-1, :], vmin=(-1.0/2.0 - numpy.sqrt(2.0)), vmax=1.0, extent=[-1.0, 1.0, -1.0, 1.0])
patch = matplotlib.patches.Circle((0.0, 0.0), radius=1.0, transform=pyplot.gca().transData)
im.set_clip_path(patch)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.colorbar()
pyplot.savefig("Figure19.pgf")
pyplot.show()

