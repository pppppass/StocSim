
# coding: utf-8

# In[1]:


import numpy
import shelve


# In[2]:


def mc_sin(num):
    n = num
    x = numpy.random.rand(n)
    y = numpy.sin(x)
    s = numpy.sum(y) / n
    return s


# In[3]:


def get_sin_exact():
    return numpy.cos(0.0) - numpy.cos(1.0)


# In[4]:


def calc_e2(num, rep):
    n, m = num, rep
    sum_e2 = 0.0
    for i in range(m):
        e = mc_sin(n) - get_sin_exact()
        sum_e2 += e**2
    return sum_e2 / m


# In[5]:


def calc_e1(num, rep):
    n, m = num, rep
    sum_e1 = 0.0
    for i in range(m):
        e = numpy.abs(mc_sin(n) - get_sin_exact())
        sum_e1 += e
    return sum_e1 / m


# In[6]:


numpy.random.seed(1)


# In[7]:


rt = [[], []]


# In[8]:


n_list = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
m = 1000


# In[9]:


for n in n_list:
    rt[0].append(calc_e2(n, m))
    rt[1].append(calc_e1(n, m))
    print("n = {} finished".format(n))


# In[10]:


with shelve.open("Result") as db:
    db["size"] = n_list
    db["error2"] = rt[0]
    db["error1"] = rt[1]

