
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


ns = [8, 12, 16, 24]
es = numpy.logspace(-3.0, 0.0, 31)
t = 4.511528
ts = t + es
it = 250000000
m = 4


# In[4]:


res = [[None for _ in ts] for _ in ns]


# In[5]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_3d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob8/Part1/Kin/Final/CorrectTC"] = res
db.sync()


# In[9]:


ns = [8, 12, 16, 24]
es = numpy.logspace(-3.0, 0.0, 31)
t = 4.511528
ts = t - es
it = 250000000
m = 4


# In[10]:


res = [[None for _ in ts] for _ in ns]


# In[11]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_3d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob8/Part2/Kin/Final/CorrectTC"] = res
db.sync()


# In[12]:


ns = [8, 12, 16, 24]
es = numpy.logspace(-3.0, 0.0, 31)
t = 4.511528
ts = t + es
it = 250000000
m = 4


# In[13]:


res = [[None for _ in ts] for _ in ns]


# In[14]:


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
db["Prob8/Part3/Kin/Final/CorrectTC"] = res
db.sync()


# In[15]:


ns = [8, 12, 16, 24]
es = numpy.logspace(-3.0, 0.0, 31)
t = 4.511528
ts = t - es
it = 250000000
m = 4


# In[16]:


res = [[None for _ in ts] for _ in ns]


# In[17]:


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
db["Prob8/Part4/Kin/Final/CorrectTC"] = res
db.sync()


# In[ ]:


db.close()

