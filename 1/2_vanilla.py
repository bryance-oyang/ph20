#!/usr/bin/python

import math as m

#fx = input("fx: ");
#fy = input("fy: ");
#Ax = input("Ax: ");
#Ay = input("Ay: ");
#phi = input("phi: ");
#dt = input("Delta t: ");
#N = input("N: ");

fx = 1;
fy = 2;
Ax = 1;
Ay = 1;
phi = 0;
dt = 1./8;
N = 10;

t = [dt * i for i in range(0, N+1)];

X = [Ax * m.sin(2 * m.pi * fx * i) for i in t];
Y = [Ay * m.sin(2 * m.pi * fy * i + phi) for i in t];
Z = [x + y for x, y in zip(X, Y)];

output = file("out_2_vanilla", "w");
for x, y, z in zip (X, Y, Z):
	output.write("%.3f\t%.3f\t%.3f\n" % (x, y, z));
