
# coding: utf-8

# In[2]:


import time
import shelve
import numpy
from matplotlib import pyplot
import samp


# In[3]:


db = shelve.open("Result")


# In[4]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4


# In[5]:


res = [[None for _ in ts] for _ in ns]


# In[6]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_3d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob5/Part1/Kin/Final"] = res
db.sync()


# In[11]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(4.41, 4.61, 21)
it = 250000000
m = 4


# In[12]:


res = [[None for _ in ts] for _ in ns]


# In[13]:


for i, n in enumerate(ns):
    if n == 8:
        ts = numpy.linspace(4.21, 4.41, 21)
    elif n == 12:
        ts = numpy.linspace(4.31, 4.51, 21)
    else:
        ts = numpy.linspace(4.41, 4.61, 21)
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_3d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob5/Part2/Kin/Final"] = res
db.sync()


# In[4]:


ns = [8, 12]
ts = numpy.linspace(4.41, 4.61, 21)
it = 250000000
m = 4


# In[5]:


res = [[None for _ in ts] for _ in ns]


# In[6]:


for i, n in enumerate(ns):
    if n == 8:
        ts = numpy.linspace(4.21, 4.41, 21)
    elif n == 12:
        ts = numpy.linspace(4.31, 4.51, 21)
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_3d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob5/Part2/Kin/Final/Add"] = res
db.sync()


# In[ ]:


db.close()

