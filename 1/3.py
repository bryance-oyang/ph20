#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt

fx = input("fx: ")
fy = input("fy: ")
Ax = 1
Ay = 1
phi = input("phi: ")
dt = 0.01
N = 100

t = dt * np.array(range(0, N+1))

X = Ax * np.cos(2 * np.pi * fx * t)
Y = Ay * np.sin(2 * np.pi * fy * t + phi)

plt.figure(figsize = (8, 5))

plt.plot(X, Y, "b.-")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Ratio: %.4f, $\phi$ = %.4f" % (float(fx)/fy, phi))
plt.savefig("latex/plot_3_ratio_%.0f_%.0f_phase_%.0f.pdf" % (fx, fy, phi))

