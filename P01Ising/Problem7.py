
# coding: utf-8

# In[1]:


import time
import shelve
import numpy
from matplotlib import pyplot
import samp


# In[2]:


db = shelve.open("Result")


# In[3]:


ns = [12, 16]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4


# In[4]:


res = [[None for _ in ts] for _ in ns]


# In[5]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        g1, g2, ga1, ga2 = (numpy.zeros(n) for _ in range(4))
        start = time.time()
        samp.wrapper_driver_samp_ising_kin_3d_corr(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4, g1, g2, ga1, ga2)
        end = time.time()
        print("Time: {}".format(end - start))
        res[i][j] = (g1, g2, ga1, ga2)
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob7/Part1/Kin/Final"] = res
db.sync()


# In[ ]:


db.close()

