
# coding: utf-8

# In[1]:


import numpy
import scipy.stats
import matplotlib
matplotlib.use("pgf")
from matplotlib import pyplot


# In[2]:


def calc_binomial(num, prob, pos):
    n, p, x = num, prob, pos
    rv = scipy.stats.binom(n, p)
    y = rv.pmf(x)
    return y


# In[3]:


def calc_poisson(lamda, pos):
    l, x = lamda, pos
    rv = scipy.stats.poisson(l)
    y = rv.pmf(x)
    return y


# In[4]:


def calc_gauss_disc(mu, sigma, pos, delta):
    m, s, x, d = mu, sigma, pos, delta
    rv = scipy.stats.norm(m, s)
    y = rv.cdf(pos + delta) - rv.cdf(pos - delta)
    return y


# In[5]:


x = numpy.arange(0, 20)
l = 5.0
n_list = [10, 20, 40, 80, 160, 320]


# In[6]:


pyplot.figure(figsize=(8.0, 4.5))
for i in range(len(n_list)):
    n = n_list[i]
    pyplot.subplot(2, 3, i+1)
    y1 = calc_binomial(n, l / n, x)
    y2 = calc_poisson(l, x)
    pyplot.plot(x, y1, color="C0", label="$ \mathcal{B} ( n, p ) $")
    pyplot.plot(x, y2, color="C1", label="$ \mathcal{P} (\lambda) $")
    if i == 5:
        pyplot.legend()
    pyplot.title("$ n = {} $".format(n))
pyplot.tight_layout()
pyplot.savefig("Figure1.pgf")
pyplot.show()


# In[7]:


l_list = [2.0, 5.0, 10.0, 20.0, 40.0, 80.0]
l_int_list = [2, 5, 10, 20, 40, 80]


# In[8]:


pyplot.figure(figsize=(8.0, 4.5))
for i in range(len(l_list)):
    l = l_list[i]
    x = numpy.arange(int(l - 2.0 * numpy.sqrt(2.0 * l) + 0.5), int(l + 4.0 * numpy.sqrt(2.0 * l)) + 0.5)
    pyplot.subplot(2, 3, i+1)
    y1 = calc_poisson(l, x)
    y2 = calc_gauss_disc(l, numpy.sqrt(l), x, 0.5)
    pyplot.plot(x, y1, color="C1", label="$ \mathcal{P} (\lambda) $")
    pyplot.plot(x, y2, color="C2", label="$ \mathcal{N} ( \lambda, \lambda ) $")
    if i == 5:
        pyplot.legend()
    pyplot.title("$ \lambda = {} $".format(l_int_list[i]))
pyplot.tight_layout()
pyplot.savefig("Figure2.pgf")
pyplot.show()

