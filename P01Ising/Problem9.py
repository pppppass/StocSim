
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
ts = numpy.linspace(2.22, 2.32, 21)
it = 250000000
m = 4


# In[4]:


res = [[[None for _ in range(2)] for _ in ts] for _ in ns]


# In[5]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j][0] = samp.wrapper_driver_samp_ising_kin_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        res[i][j][1] = end - start
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob9/Part1/Kin/Final"] = res
db.sync()


# In[6]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(2.22, 2.32, 21)
it = 250000000
m = 4


# In[7]:


res = [[[None for _ in range(2)] for _ in ts] for _ in ns]


# In[8]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        start = time.time()
        res[i][j][0] = samp.wrapper_driver_samp_ising_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        res[i][j][1] = end - start
        print("Time: {}".format(end - start))
        print(res[i][j])
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob9/Part2/Dir/Final"] = res
db.sync()


# In[9]:


ns = [16, 32, 64, 128]
ts = [1.0, 1.5, 2.0, 2.5, 3.0]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m


# In[10]:


res = [[[[None for _ in range(2)] for _ in its] for _ in ts] for _ in ns]


# In[12]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        for k, it_float in enumerate(its):
            it = int(it_float + 1.0e-5)
            start = time.time()
            res[i][j][k][0] = samp.wrapper_driver_samp_ising_kin_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
            end = time.time()
            res[i][j][k][1] = end - start
            print("Time: {}".format(end - start))
            print(res[i][j][k])
            print("it = {} finished".format(it))
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob9/Part3/Kin/Final"] = res
db.sync()


# In[13]:


ns = [16, 32, 64, 128]
ts = [1.0, 1.5, 2.0, 2.5, 3.0]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m


# In[14]:


res = [[[[None for _ in range(2)] for _ in its] for _ in ts] for _ in ns]


# In[15]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        for k, it_float in enumerate(its):
            it = int(it_float + 1.0e-5)
            start = time.time()
            res[i][j][k][0] = samp.wrapper_driver_samp_ising_2d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
            end = time.time()
            res[i][j][k][1] = end - start
            print("Time: {}".format(end - start))
            print(res[i][j][k])
            print("it = {} finished".format(it))
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob9/Part4/Dir/Final"] = res
db.sync()


# In[16]:


ns = [8, 12, 16, 24]
ts = [3.5, 4.0, 4.5, 5.0, 5.5]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m


# In[17]:


res = [[[[None for _ in range(2)] for _ in its] for _ in ts] for _ in ns]


# In[18]:


for i, n in enumerate(ns):
    for j, t in enumerate(ts):
        for k, it_float in enumerate(its):
            it = int(it_float + 1.0e-5)
            start = time.time()
            res[i][j][k][0] = samp.wrapper_driver_samp_ising_kin_3d(n, t, 0.0, it, it//3, m, 65536, numpy.random.randint(0, 2147483647), 4)
            end = time.time()
            res[i][j][k][1] = end - start
            print("Time: {}".format(end - start))
            print(res[i][j][k])
            print("it = {} finished".format(it))
        print("t = {} finished".format(t))
    print("n = {} finished".format(n))
db["Prob9/Part5/Kin/Final"] = res
db.sync()


# In[ ]:


db.close()

