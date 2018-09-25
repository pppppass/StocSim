
# coding: utf-8

# In[1]:


import numpy
import shelve
import matplotlib
matplotlib.use("pgf")
from matplotlib import pyplot


# In[ ]:


with shelve.open("Result") as db:
    x = db["n"]
    y = db["e^2"]
    pyplot.figure(figsize=(6.0, 4.5))
    pyplot.plot(x, y, label=r"<LABEL1~~~~>")
    pyplot.plot([1.0e1, 1.0e6], [1.0e-2, 1.0e-7], linewidth=0.5, color="black", label="Slope $-1$")
    pyplot.legend()
    pyplot.semilogx()
    pyplot.semilogy()
    pyplot.xlabel("$N$")
    pyplot.ylabel("Value")
    pyplot.savefig("Figure1.pgf")
    pyplot.show()


# In[ ]:


with shelve.open("Result") as db:
    x = db["n"]
    y = db["|e|"]
    pyplot.figure(figsize=(6.0, 4.5))
    pyplot.plot(x, y, label="<LABEL2~~~~~~>")
    pyplot.plot([1.0e1, 1.0e6], [1.0e-1, numpy.power(10.0, -3.5)], linewidth=0.5, color="black", label="Slope $ -1 / 2 $")
    pyplot.legend()
    pyplot.semilogx()
    pyplot.semilogy()
    pyplot.xlabel("$N$")
    pyplot.ylabel("Value")
    pyplot.savefig("Figure2.pgf")
    pyplot.show()

