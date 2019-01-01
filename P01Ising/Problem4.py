
# coding: utf-8

# In[4]:


import time
import shelve
import numpy
from matplotlib import pyplot
import samp


# In[5]:


db = shelve.open("Result")


# In[11]:


ns = [16, 32, 64, 128]
es = numpy.logspace(-3.0, 0.0, 31)
t = 2.269185
ts = t + es
it = 250000000
m = 4


# In[12]:


res = [[None for _ in ts] for _ in ns]


# In[13]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob4/Part1/Kin/Final"] = res
db.sync()


# In[17]:


ns = [16, 32, 64, 128]
es = numpy.logspace(-3.0, 0.0, 31)
t = 2.269185
ts = t - es
it = 250000000
m = 4


# In[18]:


res = [[None for _ in ts] for _ in ns]


# In[19]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j] = samp.wrapper_driver_samp_ising_kin_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob4/Part2/Kin/Final"] = res
db.sync()


# In[23]:


ns = [16, 32, 64, 128]
es = numpy.logspace(-3.0, 0.0, 31)
t = 2.269185
ts = t + es
it = 250000000
m = 4


# In[24]:


res = [[None for _ in ts] for _ in ns]


# In[25]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        g1, g2, ga1, ga2 = (numpy.zeros(n) for _ in range(4))
        start = time.time()
        samp.wrapper_driver_samp_ising_kin_2d_corr(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4, g1, g2, ga1, ga2)
        end = time.time()
        print("Time: {}".format(end - start))
        res[i][j] = (g1, g2, ga1, ga2)
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob4/Part3/Kin/Final"] = res
db.sync()


# In[26]:


ns = [16, 32, 64, 128]
es = numpy.logspace(-3.0, 0.0, 31)
t = 2.269185
ts = t - es
it = 250000000
m = 4


# In[27]:


res = [[None for _ in ts] for _ in ns]


# In[28]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        g1, g2, ga1, ga2 = (numpy.zeros(n) for _ in range(4))
        start = time.time()
        samp.wrapper_driver_samp_ising_kin_2d_corr(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4, g1, g2, ga1, ga2)
        end = time.time()
        print("Time: {}".format(end - start))
        res[i][j] = (g1, g2, ga1, ga2)
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob4/Part4/Kin/Final"] = res
db.sync()


# In[ ]:


db.close()

