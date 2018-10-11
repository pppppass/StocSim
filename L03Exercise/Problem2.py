
# coding: utf-8

# In[1]:


import time
import shelve
import numpy


# In[2]:


def gen_sphere_hei_ang(size):
    n = size
    z = numpy.random.uniform(-1.0, 1.0, n)
    r = numpy.sqrt(1 - z**2)
    t = numpy.random.uniform(0.0, 2.0 * numpy.pi, n)
    x = r * numpy.cos(t)
    y = r * numpy.sin(t)
    return x, y, z


# In[3]:


def gen_sphere_box_norm(size, buf):
    n, k = size, buf
    x = numpy.random.uniform(-1.0, 1.0, n)
    y = numpy.random.uniform(-1.0, 1.0, n)
    z = numpy.random.uniform(-1.0, 1.0, n)
    r = x**2 + y**2 + z**2
    b = r <= 1.0
    x, y, z = x[b], y[b], z[b]
    r = numpy.sqrt(r[b])
    x, y, z = x/r, y/r, z/r
    return x, y, z


# In[4]:


def gen_sphere_gauss_norm(n):
    x = numpy.random.randn(n)
    y = numpy.random.randn(n)
    z = numpy.random.randn(n)
    r = x**2 + y**2 + z**2
    r = numpy.sqrt(r)
    x, y, z = x / r, y / r, z / r
    return x, y, z


# In[5]:


rt = [[], [], []]


# In[6]:


n = 100000000
m = 1000


# In[7]:


numpy.random.seed(1)
start = time.time()
x, y, z = gen_sphere_hei_ang(n)
end = time.time()
rt[0].append(end - start)
rt[0].append(x.size)
print("Height-angle finished")
numpy.save("Result1.npy", numpy.stack([x[:m], y[:m], z[:m]]))
start = time.time()
x, y, z = gen_sphere_box_norm(n, m*4)
end = time.time()
rt[1].append(end - start)
rt[1].append(x.size)
print("Box-rejection-normalization finished")
numpy.save("Result2.npy", numpy.stack([x[:m], y[:m], z[:m]]))
start = time.time()
x, y, z = gen_sphere_gauss_norm(n)
end = time.time()
rt[2].append(end - start)
rt[2].append(x.size)
print("Gaussian-normalization finished")
numpy.save("Result3.npy", numpy.stack([x[:m], y[:m], z[:m]]))


# In[8]:


with shelve.open("Result") as db:
    db["size"] = n
    db["hei-ang"] = rt[0]
    db["box-norm"] = rt[1]
    db["gauss-norm"] = rt[2]

