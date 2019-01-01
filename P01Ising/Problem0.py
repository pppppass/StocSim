
# coding: utf-8

# In[1]:


import time
import shelve
import numpy
from matplotlib import pyplot
import samp


# In[2]:


n = 32
ts = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
it = 100000000
m = 8


# In[3]:


q = numpy.zeros((len(ts), m, n, n), dtype=numpy.int32)


# In[4]:


for i, t in enumerate(ts):
    samp.wrapper_driver_samp_ising_single_2d(n, t, 0.0, it, m, 65536, numpy.random.randint(0, 2147483647), 4, q[i])
    print("t = {} finished".format(t))


# In[7]:


pyplot.figure(figsize=(8.0, 11.0))
for i, t in enumerate(ts):
    for j in range(m):
        pyplot.subplot(m, len(ts), j*len(ts) + i + 1)
        if j == 0:
            pyplot.title("$ T = {} $".format(t))
        pyplot.imshow(q[i, j])
        pyplot.axis("off")
pyplot.tight_layout()
pyplot.savefig("Figure06.pgf")
pyplot.show()
pyplot.close()

