
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


# In[37]:


def filter_interval(mean, std, eta, eps):
    low, high = mean - eta * std, mean + eta * std
    f = high < eps
    low[f], high[f] = numpy.inf, numpy.inf
    g = (low < eps) & (~f)
    low[g] = eps
    return low, high


# In[38]:


db = shelve.open("Result")
res = db["Prob1/Part1/Kin/Final"]


# In[4]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(0.5, 4.5, 41)
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
pyplot.savefig("Figure07.pgf")
pyplot.show()
pyplot.close()


# In[5]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(0.5, 4.5, 41)
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
    if i == 3:
        pyplot.ylim(-0.1, 3.1)
pyplot.tight_layout()
pyplot.savefig("Figure08.pgf")
pyplot.show()
pyplot.close()


# In[6]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(0.5, 4.5, 41)
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
pyplot.savefig("Figure25.pgf")
pyplot.show()
pyplot.close()


# In[7]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(0.5, 4.5, 41)
it = 250000000
m = 4
eta = 3.0
tc = 2.269
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = c1
    std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
    f = (ts - tc) > 0.0
    pyplot.plot((ts - tc)[f], mean[f], label="$c$", color="C0")
    pyplot.fill_between((ts - tc)[f], (mean - eta * std)[f], (mean + eta * std)[f], alpha = 0.3, color="C0")
    pyplot.scatter((ts - tc)[f], mean[f], s=2.0, color="C0")
    pyplot.plot((ts - tc)[f], 2.5 * (ts - tc)[f]**(0.0), linewidth=0.5, color="black", label="Slope $0$")
    pyplot.xlabel("$ T - T_{\\mathrm{c}} $")
    pyplot.ylabel("$c$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure27.pgf")
pyplot.show()
pyplot.close()


# In[39]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(0.5, 4.5, 41)
it = 250000000
m = 4
eta = 3.0
tc = 2.269
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = c1
    std = numpy.sqrt((c2 - c1**2 + 1.0e-15) / m)
    f = (tc - ts) > 0.0
    pyplot.plot((tc - ts)[f], mean[f], label="$c$", color="C0")
    pyplot.fill_between((tc - ts)[f], *filter_interval(mean[f], std[f], eta, 1.0e-2), alpha = 0.3, color="C0")
    pyplot.scatter((tc - ts)[f], mean[f], s=2.0, color="C0")
    pyplot.plot((tc - ts)[f], 1.8 * (tc - ts)[f]**(0.0), linewidth=0.5, color="black", label="Slope $0$")
    pyplot.xlabel("$ T_{\\mathrm{c}} - T $")
    pyplot.ylabel("$c$")
    pyplot.ylim(5.0e-2, None)
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure28.pgf")
pyplot.show()
pyplot.close()


# In[9]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(0.5, 4.5, 41)
it = 250000000
m = 4
eta = 3.0
tc = 2.269
pyplot.figure(figsize=(8.0, 6.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 2, i+1)
    pyplot.title("$ N = {} $".format(n))
    ma1, ma2, u1, u2, c1, c2 = [numpy.array([res[i][j][k] for j, _ in enumerate(ts)]) for k in [2, 3, 4, 5, 6, 7]]
    mean = ma1
    std = numpy.sqrt((ma2 - ma1**2 + 1.0e-15) / m)
    f = (tc - ts) > 0.0
    pyplot.plot((tc - ts)[f], mean[f], label="$m$", color="C0")
    pyplot.fill_between((tc - ts)[f], (mean - eta * std)[f], (mean + eta * std)[f], alpha = 0.3, color="C0")
    pyplot.scatter((tc - ts)[f], mean[f], s=2.0, color="C0")
    pyplot.plot((tc - ts)[f], (tc - ts)[f]**(0.125), linewidth=0.5, color="black", label="Slope $ 1 / 8 $")
    pyplot.xlabel("$ T_{\\mathrm{c}} - T $")
    pyplot.ylabel("$m$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure29.pgf")
pyplot.show()
pyplot.close()


# In[10]:


db = shelve.open("Result")
res = db["Prob1/Part2/Kin/Final"]


# In[11]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(2.22, 2.32, 21)
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
pyplot.savefig("Figure09.pgf")
pyplot.show()
pyplot.close()


# In[12]:


ns = [16, 32, 64, 128]
ts = numpy.linspace(2.22, 2.32, 21)
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
pyplot.savefig("Figure10.pgf")
pyplot.show()
pyplot.close()


# In[13]:


db = shelve.open("Result")
res = db["Prob2/Part1/Kin/Final"]


# In[14]:


ns = [32, 64]
ts = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
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
pyplot.savefig("Figure15.pgf")
pyplot.show()
pyplot.close()


# In[15]:


# ns = [32, 64]
# ts = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
# hs = numpy.logspace(-3.0, 0.0, 31)
# it = 25000000
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(6.0, 8.0))
# for i, n in enumerate(ns):
#     pyplot.subplot(2, 1, i+1)
#     pyplot.title("$ N = {} $".format(n))
#     for j, t in enumerate(ts):
#         m1, m2, ma1, ma2 = [numpy.array([res[i][j][l][k] for l, _ in enumerate(hs)]) for k in [0, 1, 2, 3]]
#         mean = m1
#         std = numpy.sqrt((m2 - m1**2 + 1.0e-15) / m)
#         pyplot.plot(hs, mean, label="$ N = {}, T = {} $".format(n, t), color="C{}".format(j))
#         pyplot.fill_between(hs, mean - eta * std, mean + eta * std, alpha = 0.3, color="C{}".format(j))
#         pyplot.scatter(hs, mean, s=2.0, color="C{}".format(j))
#     pyplot.xlabel("$h$")
#     pyplot.ylabel("$m$")
#     pyplot.semilogx()
#     pyplot.ylim(-0.6, 1.1)
# pyplot.legend()
# pyplot.tight_layout()
# pyplot.savefig("Figure16.pgf")
# pyplot.show()
# pyplot.close()


# In[16]:


db = shelve.open("Result")
res = db["Prob2/Part2/Kin/Final"]


# In[17]:


ns = [32, 64]
ts = [1.0, 1.5, 2.0, 2.5, 3.0]
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
pyplot.savefig("Figure16.pgf")
pyplot.show()
pyplot.close()


# In[18]:


def calc_char_len_dir(gamma, start, end):
    g, i, j = gamma, start, end
    n = g.shape[0]
    lr = scipy.stats.linregress(numpy.arange(i, j), numpy.log(numpy.abs((g[i:j] + numpy.roll(g[::-1], 1)[i:j]) / 2.0)))
    xi = -1.0 / lr.slope
    return xi


# In[20]:


db = shelve.open("Result")
res = db["Prob3/Part1/Kin/Final"]


# In[21]:


ns = [32, 64]
ts = numpy.linspace(0.5, 4.5, 41)
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
pyplot.savefig("Figure19.pgf")
pyplot.show()
pyplot.close()


# In[22]:


ns = [32, 64]
ts = numpy.linspace(0.5, 4.5, 41)
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
pyplot.savefig("Figure20.pgf")
pyplot.tight_layout()
pyplot.show()
pyplot.close()


# In[23]:


ns = [32, 64]
ts = numpy.linspace(0.5, 4.5, 41)
it = 250000000
m = 4
eta = 3.0
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    xis = numpy.array([
        calc_char_len_dir(res[i][j][0], 0, 6)
    for j, t in enumerate(ts)])
    pyplot.plot(ts, filter_array(xis, lambda x: x < 10.0), label="$\\xi$")
    pyplot.scatter(ts, filter_array(xis, lambda x: x < 10.0), s=2.0)
    xis = numpy.array([
        calc_char_len_dir(res[i][j][2], 0, 3)
    for j, t in enumerate(ts)])
    pyplot.plot(ts, filter_array(xis, lambda x: x < 10.0), label="$\\xi_{\\mathrm{o}}$")
    pyplot.scatter(ts, filter_array(xis, lambda x: x < 10.0), s=2.0)
    pyplot.xlabel("$T$")
    pyplot.ylabel("$\\xi$")
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure21.pgf")
pyplot.show()
pyplot.close()


# In[24]:


ns = [32, 64]
ts = numpy.linspace(0.5, 4.5, 41)
it = 250000000
m = 4
eta = 3.0
tc = 2.269
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    xis = numpy.array([
        calc_char_len_dir(res[i][j][0], 0, 6)
    for j, t in enumerate(ts)])
    f = (ts - tc) > 0.0
    pyplot.plot((ts - tc)[f], filter_array(xis, lambda x: x < 10.0)[f], label="$\\xi$")
    pyplot.scatter((ts - tc)[f], filter_array(xis, lambda x: x < 10.0)[f], s=2.0)
    pyplot.plot((ts - tc)[f], 0.4 * (ts - tc)[f]**(-1.0), linewidth=0.5, color="black", label="Slope $-1$")
    pyplot.plot((ts - tc)[f], 1.0 * (ts - tc)[f]**(-0.6), linewidth=0.5, color="black", linestyle="--", label="Slope $-0.6$")
    pyplot.xlabel("$ T - T_{\\mathrm{c}} $")
    pyplot.ylabel("$\\xi$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure30.pgf")
pyplot.show()
pyplot.close()


# In[25]:


ns = [32, 64]
ts = numpy.linspace(0.5, 4.5, 41)
it = 250000000
m = 4
eta = 3.0
tc = 2.269
pyplot.figure(figsize=(6.0, 8.0))
for i, n in enumerate(ns):
    pyplot.subplot(2, 1, i+1)
    pyplot.title("$ N = {} $".format(n))
    xis = numpy.array([
        calc_char_len_dir(res[i][j][2], 0, 3)
    for j, t in enumerate(ts)])
    f = (tc - ts) > 0.0
    pyplot.plot((tc - ts)[f], filter_array(xis, lambda x: x < 10.0)[f], label="$\\xi_{\\mathrm{o}}$")
    pyplot.scatter((tc - ts)[f], filter_array(xis, lambda x: x < 10.0)[f], s=2.0)
    pyplot.plot((tc - ts)[f], 0.4 * (tc - ts)[f]**(-1.0), linewidth=0.5, color="black", label="Slope $-1$")
    pyplot.plot((tc - ts)[f], 0.4 * (tc - ts)[f]**(-0.6), linewidth=0.5, linestyle="--", color="black", label="Slope $-0.6$")
    pyplot.xlabel("$ T_{\\mathrm{c}} - T $")
    pyplot.ylabel("$\\xi_{\\mathrm{o}}$")
    pyplot.semilogx()
    pyplot.semilogy()
pyplot.legend()
pyplot.tight_layout()
pyplot.savefig("Figure31.pgf")
pyplot.show()
pyplot.close()


# In[26]:


# db = shelve.open("Result")
# res = db["Prob4/Part1/Kin/Final"]


# In[27]:


# ns = [16, 32, 64, 128]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 2.269185
# ts = t + es
# it = 250000000
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
# pyplot.plot(es, 0.1 * es**(-0.125))
# # pyplot.semilogx()
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[28]:


# ns = [16, 32, 64, 128]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 2.269185
# ts = t + es
# it = 1000000#00
# m = 12
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


# In[29]:


# db = shelve.open("Result")
# res = db["Prob4/Part2/Kin/Final"]


# In[30]:


# ns = [16, 32, 64, 128]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 2.269185
# ts = t - es
# it = 1000000#00
# m = 12
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


# In[31]:


# ns = [16, 32, 64, 128]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 2.269185
# ts = t - es
# it = 1000000#00
# m = 12
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


# In[32]:


# db = shelve.open("Result")
# res = db["Prob4/Part3/Kin/Final"]


# In[33]:


# ns = [16, 32, 64, 128]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 2.269185
# ts = t + es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     xis = numpy.array([calc_char_len_dir(res[i][j][2], 0, 2) for j, _ in enumerate(ts)])
#     pyplot.plot(es, filter_array(xis, lambda x: x < 10.0), label="$ N = {} $".format(n))
# # pyplot.plot(es, es**(-1.0))
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[34]:


# db = shelve.open("Result")
# res = db["Prob4/Part4/Kin/Final"]


# In[35]:


# ns = [16, 32, 64, 128]
# es = numpy.logspace(-3.0, 0.0, 31)
# t = 2.269185
# ts = t - es
# it = 2500000#00
# m = 4
# eta = 3.0
# pyplot.figure(figsize=(12.0, 8.0))
# for i, n in enumerate(ns):
#     xis = numpy.array([calc_char_len_dir(res[i][j][2], 0, 4) for j, _ in enumerate(ts)])
#     pyplot.plot(es, filter_array(xis, lambda x: x < 10.0), label="$ N = {} $".format(n))
# # pyplot.plot(es, es**(-1.0))
# pyplot.semilogx()
# pyplot.semilogy()
# pyplot.legend()
# pyplot.show()
# pyplot.close()


# In[36]:


list(db.keys())

