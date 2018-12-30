
# coding: utf-8

# In[1]:


import time
import numpy
from matplotlib import pyplot
import samp


# In[2]:


def calc_log_line(start, end, intc, order):
    return [start, end], [intc, intc * (end / start)**order]


# In[3]:


def filter_array(array, lower):
    l = []
    for e in array:
        if e > lower:
            l.append(e)
        else:
            l.append(numpy.infty)
    return l


# In[4]:


def samp_ml(x, y, size, level, num_step, rep):
    n, l, k, m = size, level, num_step, rep
    mean, var = 0.0, 0.0
    h = 1.0 / n
    c = m / numpy.sqrt(h)
    m1, m2 = samp.wrapper_driver_em_1(x, y, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
    mean += m1
    var += (m2 - m1**2) / m
    for i in range(l):
        h /= k
        m_i = int(c * (h**(3.0/4.0) * (-numpy.log2(h))**(1.0/4.0)))
        m1, m2 = samp.wrapper_driver_em_ml_1(x, y, h, k, m_i, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        mean += m1
        var += (m2 - m1**2) / m_i
    stddev = numpy.sqrt(var)
    return mean, stddev


# In[5]:


ns = numpy.array([
    16, 23, 32, 45, 64, 91, 128, 181,
    256, 362, 512, 724, 1024, 1448, 2048, 2896,
    4096, 5793, 8192, 11585, 16384, 23170, 32768, 46341,
    65536, 92682, 131072,
])
m = 1048576
ls = [0, 1, 2, 3, 4, 5, 6, 7]
k = 2


# In[6]:


means, stddevs, ts = ([numpy.zeros(len(ns)) for _ in ls] for _ in range(3))


# In[7]:


for j, l in enumerate(ls):
    for i, n in enumerate(ns):
        h = 1.0 / n
        start = time.time()
        mean, stddev = samp_ml(0.0, 0.0, n, l, k, m)
        end = time.time()
        means[j][i] = mean
        stddevs[j][i] = stddev
        ts[j][i] = end - start
        print("n = {} finished".format(n))
    print("l = {} finished".format(l))


# In[8]:


pyplot.figure(figsize=(6.0, 4.0))
for i, l in enumerate(ls):
    pyplot.plot(ns, filter_array(numpy.abs(means[i]), 1.0e-4), label="$ L = {} $".format(l), color="C{}".format(i))
    pyplot.plot(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(means[i]), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure16.pgf")
pyplot.show()
pyplot.close()


# In[9]:


pyplot.figure(figsize=(6.0, 4.0))
for i, l in enumerate(ls):
    pyplot.plot(ns, ts[i], label="$ L = {} $".format(l), color="C{}".format(i))
    pyplot.scatter(ns, ts[i], color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Time")
pyplot.legend()
pyplot.savefig("Figure17.pgf")
pyplot.show()
pyplot.close()


# In[43]:


ns = numpy.array([
    16, 23, 32, 45, 64, 91, 128, 181,
    256, 362, 512, 724, 1024, 1448, 2048, 2896,
    4096, 5793, 8192, 11585, 16384, 23170, 32768#, 46341,
#     65536,
])
m_mults = [64, 128, 256, 512]
n_filter = lambda n: n in [16, 64, 256, 1024, 4096, 16384, 32768]
l, k = 3, 4


# In[44]:


means, stddevs, ts = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(3))


# In[45]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        start = time.time()
        mean, stddev = samp_ml(0.0, 0.0, n, l, k, m)
        end = time.time()
        means[j][i] = mean
        stddevs[j][i] = stddev
        ts[j][i] = end - start
        print("n = {}, m = {} finished".format(n, m))


# In[47]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(means[i]), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(means[i]), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure10.pgf")
pyplot.show()
pyplot.close()


# In[48]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, ts[i], label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.scatter(ns, ts[i], color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Time")
pyplot.legend()
pyplot.savefig("Figure11.pgf")
pyplot.show()
pyplot.close()


# In[49]:


means, stddevs, ts = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(3))


# In[50]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        start = time.time()
        mean, stddev = samp_ml(0.5, 0.0, n, l, k, m)
        end = time.time()
        means[j][i] = mean
        stddevs[j][i] = stddev
        ts[j][i] = end - start
        print("n = {}, m = {} finished".format(n, m))


# In[52]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(means[i] - 0.125), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(means[i] - 0.125), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure12.pgf")
pyplot.show()
pyplot.close()


# In[53]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, ts[i], label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.scatter(ns, ts[i], color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Time")
pyplot.legend()
pyplot.savefig("Figure13.pgf")
pyplot.show()
pyplot.close()


# In[54]:


means, stddevs, ts = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(3))


# In[55]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        start = time.time()
        mean, stddev = samp_ml(0.5, 0.5, n, l, k, m)
        end = time.time()
        means[j][i] = mean
        stddevs[j][i] = stddev
        ts[j][i] = end - start
        print("n = {}, m = {} finished".format(n, m))


# In[56]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(means[i] - 0.25), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(means[i] - 0.25), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(stddevs[i], 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure14.pgf")
pyplot.show()
pyplot.close()


# In[57]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, ts[i], label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.scatter(ns, ts[i], color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Time")
pyplot.legend()
pyplot.savefig("Figure15.pgf")
pyplot.show()
pyplot.close()

