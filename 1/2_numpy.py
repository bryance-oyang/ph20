#!/usr/bin/python

import numpy as np

fx = input("fx: ");
fy = input("fy: ");
Ax = input("Ax: ");
Ay = input("Ay: ");
phi = input("phi: ");
dt = input("Delta t: ");
N = input("N: ");

t = dt * np.array(range(0, N+1));

X = Ax * np.sin(2 * np.pi * fx * t);
Y = Ay * np.sin(2 * np.pi * fy * t + phi);
Z = X + Y;

np.savetxt("out_2_numpy", np.array([X, Y, Z]).T, fmt = "%.3f", delimiter = "\t");
