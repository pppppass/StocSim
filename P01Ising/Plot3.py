
# coding: utf-8

# In[1]:


import shelve
import numpy
import scipy.stats
from matplotlib import pyplot


# In[2]:


def filter_array(array, lamda):
    l = []
    for e in array:
        if lamda(e):
            l.append(e)
        else:
            l.append(numpy.infty)
    return numpy.array(l)


# In[3]:


db = shelve.open("Result")
res = db["Prob9/Part3/Kin/Final"]
res1 = res


# In[4]:


ns = [16, 32, 64, 128]
ts = [1.0, 1.5, 2.0, 2.5, 3.0]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][l][0][k] for l, _ in enumerate(its)]) for k in [2, 3, 4, 5, 6, 7]]
        mean = ma1
        std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
        pyplot.plot(its, mean, label="$ T = {:.1f} $".format(t), color="C{}".format(j))
        pyplot.scatter(its, mean, s=2.0, color="C{}".format(j))
        pyplot.fill_between(its, mean - eta * std, mean + eta * std, alpha = 0.3, color="C{}".format(j))
    pyplot.xlabel("$\\mathit{ITER}$")
    pyplot.ylabel("$m$")
    pyplot.semilogx()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure01.pgf")
pyplot.show()
pyplot.close()


# In[5]:


db = shelve.open("Result")
res = db["Prob9/Part4/Dir/Final"]
res2 = res


# In[6]:


ns = [16, 32, 64, 128]
ts = [1.0, 1.5, 2.0, 2.5, 3.0]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][l][0][k] for l, _ in enumerate(its)]) for k in [2, 3, 4, 5, 6, 7]]
        mean = ma1
        std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
        pyplot.plot(its, mean, label="$ T = {:.1f} $".format(t), color="C{}".format(j))
        pyplot.scatter(its, mean, s=2.0, color="C{}".format(j))
        pyplot.fill_between(its, mean - eta * std, mean + eta * std, alpha = 0.3, color="C{}".format(j))
    pyplot.xlabel("$\\mathit{ITER}$")
    pyplot.ylabel("$m$")
    pyplot.semilogx()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure02.pgf")
pyplot.show()
pyplot.close()


# In[7]:


ns = [16, 32, 64, 128]
ts = [1.0, 1.5, 2.0, 2.5, 3.0]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        t_runs1 = numpy.array([res1[i][j][l][1] for l, _ in enumerate(its)])
        t_runs2 = numpy.array([res2[i][j][l][1] for l, _ in enumerate(its)])
        pyplot.plot(its, t_runs1, label="$ T = {:.1f} $".format(t), color="C{}".format(j))
        pyplot.scatter(its, t_runs1, s=2.0, color="C{}".format(j))
        pyplot.plot(its, t_runs2, color="C{}".format(j), linestyle="--")
        pyplot.scatter(its, t_runs2, s=2.0, color="C{}".format(j))
    pyplot.xlabel("$\\mathit{ITER}$")
    pyplot.ylabel("Time")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure03.pgf")
pyplot.show()
pyplot.close()


# In[8]:


db = shelve.open("Result")
res = db["Prob9/Part5/Kin/Final"]
res2 = res


# In[9]:


ns = [8, 12, 16, 24]
ts = [3.5, 4.0, 4.5, 5.0, 5.5]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][l][0][k] for l, _ in enumerate(its)]) for k in [2, 3, 4, 5, 6, 7]]
        mean = ma1
        std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
        pyplot.plot(its, mean, label="$ T = {:.1f} $".format(t), color="C{}".format(j))
        pyplot.scatter(its, mean, s=2.0, color="C{}".format(j))
        pyplot.fill_between(its, mean - eta * std, mean + eta * std, alpha = 0.3, color="C{}".format(j))
    pyplot.xlabel("$\\mathit{ITER}$")
    pyplot.ylabel("$m$")
    pyplot.semilogx()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure04.pgf")
pyplot.show()
pyplot.close()


# In[10]:


ns = [8, 12, 16, 24]
ts = [3.5, 4.0, 4.5, 5.0, 5.5]
m = 4
its = numpy.logspace(4.0, 9.0, 21) / m
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        t_runs = numpy.array([res[i][j][l][1] for l, _ in enumerate(its)])
        pyplot.plot(its, t_runs, label="$ T = {:.1f} $".format(t), color="C{}".format(j))
        pyplot.scatter(its, t_runs, s=2.0, color="C{}".format(j))
    pyplot.xlabel("$\\mathit{ITER}$")
    pyplot.ylabel("Time")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure05.pgf")
pyplot.show()
pyplot.close()


# In[11]:


# db = shelve.open("Result")
# res = db["Prob9/Part2/Dir/Final"]


# In[12]:


# ns = [16, 32, 64, 128]
# ts = numpy.linspace(2.22, 2.32, 21)
# it = 250000000
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(6.0, 4.0))
# for i, n in enumerate(ns):
#     u1, u2, c1, c2 = [numpy.array([res[i][j][0][k] for j, _ in enumerate(ts)]) for k in [4, 5, 6, 7]]
#     mean = c1
#     std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
#     pyplot.plot(ts, mean, label="$ N = {} $".format(n))
#     pyplot.fill_between(ts, mean - eta * std, mean + eta * std, alpha = 0.3)
# pyplot.legend()
# pyplot.show()
# pyplot.close()

