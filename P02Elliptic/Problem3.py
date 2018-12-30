
# coding: utf-8

# In[1]:


import time
import numpy
from matplotlib import pyplot
import samp


# In[17]:


def calc_log_line(start, end, intc, order):
    return [start, end], [intc, intc * (end / start)**order]


# In[18]:


ns = numpy.array([
    16, 23, 32, 45, 64, 91, 128, 181,
    256, 362, 512, 724, 1024, 1448, 2048, 2896,
    4096
])
pts = [(0.0, 0.0), (0.5, 0.0), (0.5, 0.5)]
m = 65536


# In[27]:


means, vars_ = ([numpy.zeros(len(ns)) for _ in pts] for _ in range(2))


# In[28]:


for j, pt in enumerate(pts):
    for i, n in enumerate(ns):
        h = 1.0 / n
        m1, m2 = samp.wrapper_driver_em_ml_1(*pt, h, 2, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        means[j][i] = m1
        vars_[j][i] = m2 - m1**2
        print("n = {} finished".format(n))


# In[36]:


pyplot.figure(figsize=(6.0, 4.0))
for i, pt in enumerate(pts):
    pyplot.plot(ns, vars_[i], label="$ (x, y) = ({:.1f}, {:.1f}) $".format(*pt))
    pyplot.scatter(ns, vars_[i], s=2.0)
pyplot.plot(*calc_log_line(16.0, 4096.0, 0.03, -0.5), linewidth=0.5, c="black", label="Slope $-1 / 2$")
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$n$")
pyplot.ylabel("Variance")
pyplot.legend()
pyplot.savefig("Figure20.pgf")
pyplot.show()
pyplot.close()


# In[37]:


means, vars_ = ([numpy.zeros(len(ns)) for _ in pts] for _ in range(2))


# In[38]:


for j, pt in enumerate(pts):
    for i, n in enumerate(ns):
        h = 1.0 / n
        m1, m2 = samp.wrapper_driver_em_1(*pt, h, 0, m, 2147483647, 4096, numpy.random.randint(0, 2147483647), 4)
        means[j][i] = m1
        vars_[j][i] = m2 - m1**2
        print("n = {} finished".format(n))


# In[40]:


pyplot.figure(figsize=(6.0, 4.0))
for i, pt in enumerate(pts):
    pyplot.plot(ns, vars_[i], label="$ (x, y) = ({:.1f}, {:.1f}) $".format(*pt))
    pyplot.scatter(ns, vars_[i], s=2.0)
pyplot.semilogx()
pyplot.semilogy()
pyplot.xlabel("$n$")
pyplot.ylabel("Variance")
pyplot.legend()
pyplot.savefig("Figure21.pgf")
pyplot.show()
pyplot.close()

