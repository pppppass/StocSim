
# coding: utf-8

# In[1]:


import shelve
import numpy
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


# In[2]:


with shelve.open("Result") as db:
    n = db["size"]
    d1 = db["hei-ang"]
    d2 = db["box-norm"]
    d3 = db["gauss-norm"]


# In[4]:


pyplot.figure(figsize=(8.0, 4.5))
pyplot.subplot(1, 3, 1, projection="3d", aspect="equal")
p = numpy.load("Result1.npy")
pyplot.gca().scatter(p[0], p[1], p[2], s=10)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.gca().set_zlabel("$z$")
pyplot.title("$Z$--$T$")
pyplot.subplot(1, 3, 2, projection="3d", aspect="equal")
p = numpy.load("Result2.npy")
pyplot.gca().scatter(p[0], p[1], p[2], s=10)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.gca().set_zlabel("$z$")
pyplot.title("Uniform")
pyplot.subplot(1, 3, 3, projection="3d", aspect="equal")
p = numpy.load("Result3.npy")
pyplot.gca().scatter(p[0], p[1], p[2], s=10)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.gca().set_zlabel("$z$")
pyplot.title("Gaussian")
pyplot.tight_layout()
pyplot.savefig("Figure1.pgf")
pyplot.show()


# In[5]:


pyplot.figure(figsize=(8.0, 4.5))
pyplot.subplot(1, 3, 1, aspect="equal")
p = numpy.load("Result1.npy")
pyplot.gca().scatter(p[0], p[1], s=10)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.title("$Z$--$T$")
pyplot.subplot(1, 3, 2, aspect="equal")
p = numpy.load("Result2.npy")
pyplot.gca().scatter(p[0], p[1], s=10)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.title("Uniform")
pyplot.subplot(1, 3, 3, aspect="equal")
p = numpy.load("Result3.npy")
pyplot.gca().scatter(p[0], p[1], s=10)
pyplot.xlabel("$x$")
pyplot.ylabel("$y$")
pyplot.title("Gaussian")
pyplot.tight_layout()
pyplot.savefig("Figure2.pgf")
pyplot.show()


# In[6]:


pyplot.figure(figsize=(8.0, 4.5))
pyplot.subplot(1, 3, 1, aspect="equal")
p = numpy.load("Result1.npy")
pyplot.gca().scatter(p[1], p[2], s=10)
pyplot.xlabel("$y$")
pyplot.ylabel("$z$")
pyplot.title("$Z$--$T$")
pyplot.subplot(1, 3, 2, aspect="equal")
p = numpy.load("Result2.npy")
pyplot.gca().scatter(p[1], p[2], s=10)
pyplot.xlabel("$y$")
pyplot.ylabel("$z$")
pyplot.title("Uniform")
pyplot.subplot(1, 3, 3, aspect="equal")
p = numpy.load("Result3.npy")
pyplot.gca().scatter(p[1], p[2], s=10)
pyplot.xlabel("$y$")
pyplot.ylabel("$z$")
pyplot.title("Gaussian")
pyplot.tight_layout()
pyplot.savefig("Figure3.pgf")
pyplot.show()


# In[7]:


with open("Table1.tbl", "w") as f:
    f.write("Time & {:.3f} & {:.3f} & {:.3f} \\\\\n".format(d1[0], d2[0], d3[0]))
    f.write("\\hline\n")
    f.write("\#Sample & {:} & {:} & {:} \\\\\n".format(d1[1], d2[1], d3[1]))
    f.write("\\hline\n")
    f.write("Speed & {:5e} & {:5e} & {:5e} \\\\\n".format(d1[1] / d1[0], d2[1] / d2[0], d3[1] / d3[0]))
    f.write("\\hline\n")

