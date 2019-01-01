
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
res = db["Prob5/Part1/Kin/Final"]


# In[4]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = u1
    std = numpy.sqrt((u2 - u1**2 + 1.0e-15) / m)
    pyplot.plot(ts, mean, color="C0")
    pyplot.fill_between(ts, mean - eta * std, mean + eta * std, alpha = 0.3, color="C0")
    pyplot.scatter(ts, mean, s=2.0, color="C0")
    pyplot.xlabel("$T$")
    pyplot.ylabel("$u$")
pyplot.tight_layout()
pyplot.savefig("Figure11.pgf")
pyplot.show()
pyplot.close()


# In[5]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = c1
    std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
    pyplot.plot(ts, mean, color="C0")
    pyplot.fill_between(ts, mean - eta * std, mean + eta * std, alpha = 0.3, color="C0")
    pyplot.scatter(ts, mean, s=2.0, color="C0")
    pyplot.xlabel("$T$")
    pyplot.ylabel("$c$")
pyplot.tight_layout()
pyplot.savefig("Figure12.pgf")
pyplot.show()
pyplot.close()


# In[6]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = ma1
    std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
    pyplot.plot(ts, mean, color="C0")
    pyplot.fill_between(ts, mean - eta * std, mean + eta * std, alpha = 0.3, color="C0")
    pyplot.scatter(ts, mean, s=2.0, color="C0")
    pyplot.xlabel("$T$")
    pyplot.ylabel("$m$")
pyplot.tight_layout()
pyplot.savefig("Figure26.pgf")
pyplot.show()
pyplot.close()


# In[7]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
tcs = [4.31, 4.41, 4.45, 4.47]
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    tc = tcs[i]
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = c1
    std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
    f = (ts - tc) > 0.0
    pyplot.plot((ts - tc)[f], mean[f], label="$c$", color="C0")
    pyplot.fill_between((ts - tc)[f], (mean - eta * std)[f], (mean + eta * std)[f], alpha = 0.3, color="C0")
    pyplot.scatter((ts - tc)[f], mean[f], s=2.0, color="C0")
    pyplot.plot((ts - tc)[f], 1.0e-1 * (ts - tc)[f]**(-0.11008), linewidth=0.5, color="black", label="Slope $-0.11008$")
    pyplot.plot((ts - tc)[f], 3.0e-1 * (ts - tc)[f]**(-0.8), linewidth=0.5, color="black", linestyle="--", label="Slope $-0.8$")
    pyplot.xlabel("$ T - T_{\\mathrm{c}} $")
    pyplot.ylabel("$c$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure32.pgf")
pyplot.show()
pyplot.close()


# In[8]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
tcs = [4.31, 4.41, 4.45, 4.47]
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    tc = tcs[i]
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = c1
    std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
    f = (tc - ts) > 0.0
    pyplot.plot((tc - ts)[f], mean[f], label="$c$", color="C0")
    pyplot.fill_between((tc - ts)[f], (mean - eta * std)[f], (mean + eta * std)[f], alpha = 0.3, color="C0")
    pyplot.scatter((tc - ts)[f], mean[f], s=2.0, color="C0")
    pyplot.plot((tc - ts)[f], 0.8 * (tc - ts)[f]**(-0.11008), linewidth=0.5, color="black", label="Slope $-0.11008$")
    pyplot.plot((tc - ts)[f], 1.5 * (tc - ts)[f]**(-0.2), linewidth=0.5, color="black", linestyle="--", label="Slope $-0.2$")
    pyplot.xlabel("$ T_{\\mathrm{c}} - T $")
    pyplot.ylabel("$c$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure33.pgf")
pyplot.show()
pyplot.close()


# In[9]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
tcs = [4.31, 4.41, 4.45, 4.47]
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    tc = tcs[i]
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = ma1
    std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
    f = (tc - ts) > 0.0
    pyplot.plot((tc - ts)[f], mean[f], label="$m$", color="C0")
    pyplot.fill_between((tc - ts)[f], (mean - eta * std)[f], (mean + eta * std)[f], alpha = 0.3, color="C0")
    pyplot.scatter((tc - ts)[f], mean[f], s=2.0, color="C0")
    pyplot.plot((tc - ts)[f], 1.5 * (tc - ts)[f]**(0.326419), linewidth=0.5, color="black", label="Slope $0.326419$")
    pyplot.plot((tc - ts)[f], 0.8 * (tc - ts)[f]**(0.2), linewidth=0.5, color="black", linestyle="--", label="Slope $0.2$")
    pyplot.xlabel("$ T_{\\mathrm{c}} - T $")
    pyplot.ylabel("$m$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure34.pgf")
pyplot.show()
pyplot.close()


# In[10]:


db = shelve.open("Result")
res_orig = db["Prob5/Part2/Kin/Final"]
res_add = db["Prob5/Part2/Kin/Final/Add"]
res = [*res_add, *res_orig[2:]]


# In[11]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(4.41, 4.61, 21)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    if n == 8:
        ts = numpy.linspace(4.21, 4.41, 21)
    elif n == 12:
        ts = numpy.linspace(4.31, 4.51, 21)
    else:
        ts = numpy.linspace(4.41, 4.61, 21)
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = u1
    std = numpy.sqrt((u2 - u1**2 + 1.0e-15) / m)
    pyplot.plot(ts, mean, color="C0")
    pyplot.fill_between(ts, mean - eta * std, mean + eta * std, alpha = 0.3, color="C0")
    pyplot.scatter(ts, mean, s=2.0, color="C0")
    pyplot.xlabel("$T$")
    pyplot.ylabel("$u$")
pyplot.tight_layout()
pyplot.savefig("Figure13.pgf")
pyplot.show()
pyplot.close()


# In[12]:


ns = [8, 12, 16, 24]
ts = numpy.linspace(4.41, 4.61, 21)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    if n == 8:
        ts = numpy.linspace(4.21, 4.41, 21)
    elif n == 12:
        ts = numpy.linspace(4.31, 4.51, 21)
    else:
        ts = numpy.linspace(4.41, 4.61, 21)
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = c1
    std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
    pyplot.plot(ts, mean, color="C0")
    pyplot.fill_between(ts, mean - eta * std, mean + eta * std, alpha = 0.3, color="C0")
    pyplot.scatter(ts, mean, s=2.0, color="C0")
    pyplot.xlabel("$T$")
    pyplot.ylabel("$c$")
pyplot.tight_layout()
pyplot.savefig("Figure14.pgf")
pyplot.show()
pyplot.close()


# In[13]:


db = shelve.open("Result")
res = db["Prob6/Part1/Kin/Final"]


# In[14]:


ns = [12, 16]
ts = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
hs = numpy.logspace(-3.0, 0.0, 31)
it = 25000000
m = 4
eta = 3.0
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        m1, m2, ma1, ma2 = [numpy.array([res[i][j][l][k] for l, _ in enumerate(hs)]) for k in [0, 1, 2, 3]]
        mean = ma1
        std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
        pyplot.plot(hs, mean, label="$ N = {}, T = {} $".format(n, t), color="C{}".format(j))
        pyplot.fill_between(hs, mean - eta * std, mean + eta * std, alpha = 0.3, color="C{}".format(j))
        pyplot.scatter(hs, mean, s=2.0, color="C{}".format(j))
    pyplot.xlabel("$h$")
    pyplot.ylabel("$m$")
    pyplot.semilogx()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure17.pgf")
pyplot.show()
pyplot.close()


# In[15]:


db = shelve.open("Result")
res = db["Prob6/Part2/Kin/Final"]


# In[16]:


ns = [12, 16]
ts = [3.5, 4.0, 4.5, 5.0, 5.5]
hs = numpy.logspace(-3.0, 0.0, 31)
it = 1000000
m = 1000
eta = 3.0
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        m1, m2, ma1, ma2 = [numpy.array([res[i][j][l][k] for l, _ in enumerate(hs)]) for k in [0, 1, 2, 3]]
        mean = m1
        std = numpy.sqrt((m2 - m1**2 + 1.0e-15) / m)
        pyplot.plot(hs, mean, label="$ N = {}, T = {} $".format(n, t), color="C{}".format(j+1))
        pyplot.fill_between(hs, mean - eta * std, mean + eta * std, alpha = 0.3, color="C{}".format(j+1))
        pyplot.scatter(hs, mean, s=2.0, color="C{}".format(j+1))
    pyplot.xlabel("$h$")
    pyplot.ylabel("$m_{\\mathrm{s}}$")
    pyplot.semilogx()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure18.pgf")
pyplot.show()
pyplot.close()


# In[17]:


def calc_char_len_dir(gamma, start, end):
    g, i, j = gamma, start, end
    n = g.shape[0]
    lr = scipy.stats.linregress(numpy.arange(i, j), numpy.log(numpy.abs((g[i:j] + numpy.roll(g[::-1], 1)[i:j]) / 2.0)))
    xi = -1.0 / lr.slope
    return xi


# In[18]:


def filter_interval(mean, std, eta, eps):
    low, high = mean - eta * std, mean + eta * std
    f = high < eps
    low[f], high[f] = numpy.inf, numpy.inf
    g = (low < eps) & (~f)
    low[g] = eps
    return low, high


# In[19]:


db = shelve.open("Result")
res = db["Prob7/Part1/Kin/Final"]


# In[20]:


ns = [12, 16]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        if j % 5 != 0:
            continue
        g1, g2, ga1, ga2 = [res[i][j][k] for k in [0, 1, 2, 3]]
        mean = g1
        std = numpy.sqrt((g2 - g1**2 + 1.0e-15) / m)
        pyplot.plot(numpy.arange(n), filter_array(mean, lambda x: x > 1.0e-9), label="$ T = {} $".format(t), color="C{}".format(j//5))
        pyplot.scatter(numpy.arange(n), filter_array(mean, lambda x: x > 1.0e-9), s=2.0, color="C{}".format(j//5))
        pyplot.fill_between(numpy.arange(n), *filter_interval(mean, std, eta, 1.0e-9), alpha=0.3, color="C{}".format(j//5))
    pyplot.semilogy()
    pyplot.ylim(7.0e-7, None)
    pyplot.xlabel("$r$")
    pyplot.ylabel("$\\Gamma$")
pyplot.legend(loc="center right")
pyplot.tight_layout()
pyplot.savefig("Figure22.pgf")
pyplot.show()
pyplot.close()


# In[21]:


ns = [12, 16]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    for j, t in enumerate(ts):
        if j % 5 != 0:
            continue
        g1, g2, ga1, ga2 = [res[i][j][k] for k in [0, 1, 2, 3]]
        mean = ga1
        std = numpy.sqrt((ga2 - ga1**2 + 1.0e-15) / m)
        pyplot.plot(numpy.arange(n), filter_array(mean, lambda x: x > 1.0e-9), label="$ T = {} $".format(t), color="C{}".format(j//5))
        pyplot.scatter(numpy.arange(n), filter_array(mean, lambda x: x > 1.0e-9), s=2.0, color="C{}".format(j//5))
        pyplot.fill_between(numpy.arange(n), *filter_interval(mean, std, eta, 1.0e-9), alpha=0.3, color="C{}".format(j//5))
    pyplot.semilogy()
    pyplot.ylim(7.0e-7, None)
    pyplot.xlabel("$r$")
    pyplot.ylabel("$\\Gamma_{\\mathrm{o}}$")
pyplot.legend(loc="center right")
pyplot.savefig("Figure23.pgf")
pyplot.tight_layout()
pyplot.show()
pyplot.close()


# In[22]:


ns = [12, 16]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    xis = numpy.array([
        calc_char_len_dir(res[i][j][0], 0, 5)
    for j, t in enumerate(ts)])
    pyplot.plot(ts, filter_array(xis, lambda x: x < 3.0), label="$\\xi$")
    pyplot.scatter(ts, filter_array(xis, lambda x: x < 3.0), s=2.0)
    xis = numpy.array([
        calc_char_len_dir(res[i][j][2], 0, 3)
    for j, t in enumerate(ts)])
    pyplot.plot(ts, filter_array(xis, lambda x: x < 3.0), label="$\\xi_{\\mathrm{o}}$")
    pyplot.scatter(ts, filter_array(xis, lambda x: x < 3.0), s=2.0)
    pyplot.xlabel("$T$")
    pyplot.ylabel("$\\xi$")
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure24.pgf")
pyplot.show()
pyplot.close()


# In[23]:


ns = [12, 16]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
tcs = [4.405, 4.445]
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    tc = tcs[i]
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    xis = numpy.array([
        calc_char_len_dir(res[i][j][0], 0, 6)
    for j, t in enumerate(ts)])
    f = (ts - tc) > 0.0
    pyplot.plot((ts - tc)[f], filter_array(xis, lambda x: x < 10.0)[f], label="$\\xi$")
    pyplot.scatter((ts - tc)[f], filter_array(xis, lambda x: x < 10.0)[f], s=2.0)
    pyplot.plot((ts - tc)[f], 0.4 * (ts - tc)[f]**(-0.629971), linewidth=0.5, color="black", label="Slope $-0.629971$")
    pyplot.plot((ts - tc)[f], 1.0 * (ts - tc)[f]**(-0.4), linewidth=0.5, color="black", linestyle="--", label="Slope $-0.4$")
    pyplot.xlabel("$ T - T_{\\mathrm{c}} $")
    pyplot.ylabel("$\\xi$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure35.pgf")
pyplot.show()
pyplot.close()


# In[24]:


ns = [12, 16]
ts = numpy.linspace(2.5, 6.5, 41)
it = 250000000
m = 4
eta = 3.0
tcs = [4.405, 4.445]
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    tc = tcs[i]
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    xis = numpy.array([
        calc_char_len_dir(res[i][j][2], 0, 3)
    for j, t in enumerate(ts)])
    f = (tc - ts) > 0.0
    pyplot.plot((tc - ts)[f], filter_array(xis, lambda x: x < 10.0)[f], label="$\\xi_{\\mathrm{o}}$")
    pyplot.scatter((tc - ts)[f], filter_array(xis, lambda x: x < 10.0)[f], s=2.0)
    pyplot.plot((tc - ts)[f], 0.4 * (tc - ts)[f]**(-0.629971), linewidth=0.5, color="black", label="Slope $-0.629971$")
    pyplot.plot((tc - ts)[f], 0.6 * (tc - ts)[f]**(-0.2), linewidth=0.5, linestyle="--", color="black", label="Slope $-0.2$")
    pyplot.xlabel("$ T_{\\mathrm{c}} - T $")
    pyplot.ylabel("$\\xi_{\\mathrm{o}}$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure36.pgf")
pyplot.show()
pyplot.close()


# In[25]:


# db = shelve.open("Result")
# res = db["Prob8/Part1/Kin/Final"]


# In[26]:


# ns = [8, 12, 16, 24]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 4.451136
# ts = t + es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     ma1, ma2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(es)]) for k in [2, 3, 6, 7]]
#     mean = ma1
#     std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
#     pyplot.plot(es, mean, label="$ N = {} $".format(n))
#     pyplot.fill_between(es, mean - eta * std, mean + eta * std, alpha = 0.3)
# #     print(scipy.stats.linregress(numpy.log(es[2:6]), numpy.log(ma1)[2:6]))
# #     print(auto_reg(numpy.log(es), numpy.log(ma1), 8))
# pyplot.plot(es, 0.1 * es**(-0.326419))
# # pyplot.semilogx()
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[27]:


# ns = [8, 12, 16, 24]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 4.451136
# ts = t + es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     ma1, ma2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(es)]) for k in [2, 3, 6, 7]]
#     mean = c1
#     std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
#     pyplot.plot(es, mean, label="$ N = {} $".format(n))
#     pyplot.fill_between(es, mean - eta * std, mean + eta * std, alpha = 0.3)
# pyplot.plot(es, es**(-0.11008))
# #     print(scipy.stats.linregress(numpy.log(es[2:6]), numpy.log(ma1)[2:6]))
# #     print(auto_reg(numpy.log(es), numpy.log(ma1), 8))
# # pyplot.semilogx()
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[28]:


# db = shelve.open("Result")
# res = db["Prob8/Part2/Kin/Final"]


# In[29]:


# ns = [8, 12, 16, 24]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 4.451136
# ts = t - es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     ma1, ma2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(es)]) for k in [2, 3, 6, 7]]
#     mean = ma1
#     std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
#     pyplot.plot(es, mean, label="$ N = {} $".format(n))
#     pyplot.fill_between(es, mean - eta * std, mean + eta * std, alpha = 0.3)
# #     print(scipy.stats.linregress(numpy.log(es[2:6]), numpy.log(ma1)[2:6]))
# #     print(auto_reg(numpy.log(es), numpy.log(ma1), 8))
# pyplot.plot(es, 0.1 * es**(0.125))
# pyplot.semilogx()
# # pyplot.semilogx()
# # pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[30]:


# ns = [8, 12, 16, 24]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 4.451136
# ts = t - es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     ma1, ma2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(es)]) for k in [2, 3, 6, 7]]
#     mean = c1
#     std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
#     pyplot.plot(es, mean, label="$ N = {} $".format(n))
#     pyplot.fill_between(es, mean - eta * std, mean + eta * std, alpha = 0.3)
# #     print(scipy.stats.linregress(numpy.log(es[2:6]), numpy.log(ma1)[2:6]))
# #     print(auto_reg(numpy.log(es), numpy.log(ma1), 8))
# # pyplot.semilogx()
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[31]:


# db = shelve.open("Result")
# res = db["Prob8/Part3/Kin/Final"]


# In[32]:


# ns = [8, 12, 16, 24]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 4.451136
# ts = t + es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     xis = numpy.array([calc_char_len_dir(res[i][j][2], 0, 2) for j, _ in enumerate(ts)])
#     pyplot.plot(es, filter_array(xis, lambda x: x < 10.0), label="$ N = {} $".format(n))
# pyplot.plot(es[-10:], 0.3 * (es**(-0.6299))[-10:])
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[33]:


# db = shelve.open("Result")
# res = db["Prob8/Part4/Kin/Final"]


# In[34]:


# ns = [8, 12, 16, 24]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 4.451136
# ts = t - es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     xis = numpy.array([calc_char_len_dir(res[i][j][2], 0, 4) for j, _ in enumerate(ts)])
#     pyplot.plot(es, filter_array(xis, lambda x: x < 10.0), label="$ N = {} $".format(n))
#     pyplot.plot(es[-10:], 0.4 * (es**(-0.6299))[-10:])
# # pyplot.plot(es, es**(-1.0))
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[35]:


list(db.keys())

