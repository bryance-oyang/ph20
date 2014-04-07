#!/usr/bin/python

import math as m
import matplotlib.pyplot as plt

fx = input("fx: ");
fy = input("fy: ");
Ax = input("Ax: ");
Ay = input("Ay: ");
phi = input("phi: ");
dt = input("Delta t: ");
N = input("N: ");

t = [dt * i for i in range(0, N+1)];

X = [Ax * m.sin(2 * m.pi * fx * i) for i in t];
Y = [Ay * m.sin(2 * m.pi * fy * i + phi) for i in t];
Z = [x + y for x, y in zip(X, Y)];

output = file("latex/out_2_vanilla", "w");
for x, y, z in zip (X, Y, Z):
	output.write("%.3f\t%.3f\t%.3f\n" % (x, y, z));

plt.figure(figsize = (8, 5));

plt.plot(t, X, "b.-", label = "X");
plt.plot(t, Y, "r.-", label = "Y");
plt.plot(t, Z, "g.-", label = "Z");

plt.xlabel("t");
plt.legend();
plt.savefig("latex/plot_2_vanilla.pdf");
