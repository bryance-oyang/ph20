#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt

fx = 40
fy = 45
Ax = 1
Ay = 1
phi = 0
dt = 0.001
N = 1000

t = dt * np.array(range(0, N+1))

X = Ax * np.cos(2 * np.pi * fx * t)
Y = Ay * np.sin(2 * np.pi * fy * t + phi)
Z = X + Y

plt.figure(figsize = (8, 5))

plt.plot(t, Z, "b.-")

plt.xlabel("t")
plt.ylabel("Z")
plt.title("$fx = %.4f, f_y = %.4f$" % (fx, fy))
plt.savefig("latex/plot_4.pdf")

