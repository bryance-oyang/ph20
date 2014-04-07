#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt

fx = input("fx: ");
fy = input("fy: ");
Ax = 1;
Ay = 1;
phi = input("phi: ");
dt = 0.01;
N = 100;

t = dt * np.array(range(0, N+1));

X = Ax * np.sin(2 * np.pi * fx * t);
Y = Ay * np.sin(2 * np.pi * fy * t + phi);

plt.figure(figsize = (8, 5));

plt.plot(X, Y, "b.-");

plt.xlabel("X");
plt.ylabel("Y");
plt.savefig("latex/plot_3_numpy.pdf");
