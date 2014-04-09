#!/usr/bin/python

import numpy as np

def f(x):
	return x*x

def trapezoidal(func, a, b, N):
	[a, b, N] = map(float, [a, b, N]);
	h = (b - a)/N;
	x = np.arange(a + h, b, h);
	return h * (sum(f(x)) + f(a)/2 + f(b)/2);

a = input("a = ");
b = input("b = ");
N = input("N = ");
print trapezoidal(f, a, b, N);
