
# coding: utf-8

# In[1]:


import time
import numpy
import samp
from matplotlib import pyplot


# In[3]:


def calc_log_line(start, end, intc, order):
    return [start, end], [intc, intc * (end / start)**order]


# In[4]:


def filter_array(array, lower):
    l = []
    for e in array:
        if e > lower:
            l.append(e)
        else:
            l.append(numpy.infty)
    return l


# In[5]:


ns = numpy.array([
    16, 23, 32, 45, 64, 91, 128, 181,
    256, 362, 512, 724, 1024, 1448, 2048, 2896,
    4096, 5793, 8192, 11585, 16384, 23170, 32768, 46341,
    65536, 92682, 131072, 185364, 262144#, 370728, 524288, 741455,
#     1048576,
])
m_mults = [1, 2, 4, 8]
n_filter = lambda n: n in [16, 64, 256, 1024, 4096, 16384, 65536, 262144]#, 10485765]


# In[6]:


m1s, m2s, ts = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(3))


# In[7]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        start = time.time()
        m1, m2 = samp.wrapper_driver_em_1(0.0, 0.0, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        m1s[j][i] = m1
        m2s[j][i] = m2
        ts[j][i] = end - start
        print("n = {}, m = {} finished".format(n, m))


# In[8]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(m1s[i]), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(m1s[i]), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure01.pgf")
pyplot.show()
pyplot.close()


# In[12]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, ts[i], label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.scatter(ns, ts[i], s=2.0, color="C{}".format(i))
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Time")
pyplot.legend()
pyplot.savefig("Figure07.pgf")
pyplot.show()
pyplot.close()


# In[13]:


with open("Table1.tbl", "w") as f:
    for i, n in enumerate(ns):
        if not n_filter(n):
            continue
        f.write("{} & {} & {:.5e} & {:.5e} & {:.5f} \\\\\n\\hline\n".format(
            n, m_mults[-1] * n,
            m1s[-1][i],
            numpy.sqrt((m2s[-1][i] - m1s[-1][i]**2) / (m_mults[-1] * n)),
            ts[-1][i]
        ))


# In[14]:


m1s, m2s, ts = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(3))


# In[15]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        start = time.time()
        m1, m2 = samp.wrapper_driver_em_1(0.5, 0.0, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        m1s[j][i] = m1
        m2s[j][i] = m2
        ts[j][i] = end - start
        print("n = {}, m = {} finished".format(n, m))


# In[16]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(m1s[i] - 0.125), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(m1s[i] - 0.125), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure02.pgf")
pyplot.show()
pyplot.close()


# In[18]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, ts[i], label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.scatter(ns, ts[i], s=2.0, color="C{}".format(i))
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Time")
pyplot.legend()
pyplot.savefig("Figure08.pgf")
pyplot.show()
pyplot.close()


# In[19]:


with open("Table2.tbl", "w") as f:
    for i, n in enumerate(ns):
        if not n_filter(n):
            continue
        f.write("{} & {} & {:.5e} & {:.5e} & {:.5f} \\\\\n\\hline\n".format(
            n, m_mults[-1] * n,
            m1s[-1][i] - 0.125,
            numpy.sqrt((m2s[-1][i] - m1s[-1][i]**2) / (m_mults[-1] * n)),
            ts[-1][i],
        ))


# In[20]:


m1s, m2s, ts = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(3))


# In[21]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        start = time.time()
        m1, m2 = samp.wrapper_driver_em_1(0.5, 0.5, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        end = time.time()
        m1s[j][i] = m1
        m2s[j][i] = m2
        ts[j][i] = end - start
        print("n = {}, m = {} finished".format(n, m))


# In[22]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(m1s[i] - 0.25), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(m1s[i] - 0.25), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure03.pgf")
pyplot.show()
pyplot.close()


# In[24]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, ts[i], label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.scatter(ns, ts[i], s=2.0, color="C{}".format(i))
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Time")
pyplot.legend()
pyplot.savefig("Figure09.pgf")
pyplot.show()
pyplot.close()


# In[26]:


with open("Table3.tbl", "w") as f:
    for i, n in enumerate(ns):
        if not n_filter(n):
            continue
        f.write("{} & {} & {:.5e} & {:.5e} & {:.5f} \\\\\n\\hline\n".format(
            n, m_mults[-1] * n,
            m1s[-1][i] - 0.25,
            numpy.sqrt((m2s[-1][i] - m1s[-1][i]**2) / (m_mults[-1] * n)),
            ts[-1][i]
        ))


# In[40]:


ns = numpy.array([
    16, 23, 32, 45, 64, 91, 128, 181,
    256, 362, 512, 724, 1024, 1448, 2048, 2896,
    4096, 5793, 8192, 11585, 16384, 23170, 32768#, 46341,
#     65536,
])
m_mults = [64, 128, 256, 512]
n_filter = lambda n: n in [16, 64, 256, 1024, 4096, 16384, 32768]#65536]


# In[41]:


m1s, m2s = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(2))


# In[42]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        m1, m2 = samp.wrapper_driver_em_2(0.5, 0.0, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        m1s[j][i] = m1
        m2s[j][i] = m2
        print("n = {}, m = {} finished".format(n, m))


# In[43]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(m1s[i] - 0.5), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(m1s[i] - 0.5), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure04.pgf")
pyplot.show()
pyplot.close()


# In[44]:


with open("Table4.tbl", "w") as f:
    for i, n in enumerate(ns):
        if not n_filter(n):
            continue
        f.write("{} & {} & {:.5e} & {:.5e} \\\\\n\\hline\n".format(
            n, m_mults[-1] * n,
            m1s[-1][i] - 0.5,
            numpy.sqrt((m2s[-1][i] - m1s[-1][i]**2) / (m_mults[-1] * n))
        ))


# In[45]:


m1s, m2s = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(2))


# In[46]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        m1, m2 = samp.wrapper_driver_em_2(0.0, 0.5, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        m1s[j][i] = m1
        m2s[j][i] = m2
        print("n = {}, m = {} finished".format(n, m))


# In[47]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(m1s[i] + 0.5), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(m1s[i] + 0.5), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure05.pgf")
pyplot.show()
pyplot.close()


# In[48]:


with open("Table5.tbl", "w") as f:
    for i, n in enumerate(ns):
        if not n_filter(n):
            continue
        f.write("{} & {} & {:.5e} & {:.5e} \\\\\n\\hline\n".format(
            n, m_mults[-1] * n,
            m1s[-1][i] + 0.5,
            numpy.sqrt((m2s[-1][i] - m1s[-1][i]**2) / (m_mults[-1] * n))
        ))


# In[49]:


m1s, m2s = ([numpy.zeros(len(ns)) for _ in m_mults] for _ in range(2))


# In[50]:


for j, m_mult in enumerate(m_mults):
    for i, n in enumerate(ns):
        m = m_mult * n
        h = 1.0 / n
        m1, m2 = samp.wrapper_driver_em_2(0.5, 0.5, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        m1s[j][i] = m1
        m2s[j][i] = m2
        print("n = {}, m = {} finished".format(n, m))


# In[51]:


pyplot.figure(figsize=(6.0, 4.0))
for i, m_mult in enumerate(m_mults):
    pyplot.plot(ns, filter_array(numpy.abs(m1s[i] - 0.25), 1.0e-4), label="$ M = {} N $".format(m_mult), color="C{}".format(i))
    pyplot.plot(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), linestyle="--")
    pyplot.scatter(ns, filter_array(numpy.abs(m1s[i] - 0.25), 1.0e-4), color="C{}".format(i), s=2.0)
    pyplot.scatter(ns, filter_array(numpy.sqrt((m2s[i] - m1s[i]**2) / (m_mult * ns)), 1.0e-4), color="C{}".format(i), s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$N$")
pyplot.ylabel("Value")
pyplot.legend()
pyplot.savefig("Figure06.pgf")
pyplot.show()
pyplot.close()


# In[53]:


with open("Table6.tbl", "w") as f:
    for i, n in enumerate(ns):
        if not n_filter(n):
            continue
        f.write("{} & {} & {:.5e} & {:.5e} \\\\\n\\hline\n".format(
            n, m_mults[-1] * n,
            m1s[-1][i] - 0.25,
            numpy.sqrt((m2s[-1][i] - m1s[-1][i]**2) / (m_mults[-1] * n))
        ))

