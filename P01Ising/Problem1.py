
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


ns = [16, 32, 64, 128]
ts = numpy.linspace(0.5, 4.5, 41)
it = 250000000
m = 4


# In[4]:


res = [[None for _ in ts] for _ in ns]


# In[5]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob1/Part1/Kin/Final"] = res
db.sync()


# In[6]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(2.22, 2.32, 21)
it = 250000000
m = 4


# In[7]:


res = [[None for _ in ts] for _ in ns]


# In[8]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob1/Part2/Kin/Final"] = res
db.sync()


# In[ ]:


db.close()

