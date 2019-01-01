
# coding: utf-8

# In[1]:


import time
import shelve
import numpy
from matplotlib import pyplot
import samp


# In[2]:


db = shelve.open("Result")


# In[6]:


ns = [32, 64]
ts = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
hs = numpy.logspace(-3.0, 0.0, 31)
it = 25000000
m = 4


# In[7]:


res = [[[None for _ in hs] for _ in ts] for _ in ns]


# In[8]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        for k, h in enumerate(hs):
            start = time.time()
            res[i][j][k] = samp.wrapper_driver_samp_ising_kin_2d(n, t, h, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
            end = time.time()
            print("Time: {}".format(end - start))
            print(res[i][j][k])
            print("h = {} finished".format(h))
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob2/Part1/Kin/Final"] = res
db.sync()


# In[9]:


ns = [32, 64]
ts = [1.0, 1.5, 2.0, 2.5, 3.0]
hs = numpy.logspace(-3.0, 0.0, 31)
it = 1000000
m = 1000


# In[10]:


res = [[[None for _ in hs] for _ in ts] for _ in ns]


# In[11]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        for k, h in enumerate(hs):
            start = time.time()
            res[i][j][k] = samp.wrapper_driver_samp_ising_kin_2d(n, t, h, it, it//3*2, m, 65536, numpy.random.randint(0, 2147483647), 4)
            end = time.time()
            print("Time: {}".format(end - start))
            print(res[i][j][k])
            print("h = {} finished".format(h))
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob2/Part2/Kin/Final"] = res
db.sync()


# In[10]:


db.close()

