#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def g(x):
	return x*x*x*x*x

def trapezoidal(func, a, b, N):
	[a, b, N] = map(float, [a, b, N])
	h = (b - a)/N
	x = np.arange(1, N) * h + a
	return h * (sum(func(x)) + func(a)/2 + func(b)/2)

def simpson(func, a, b, N):
	[a, b, N] = map(float, [a, b, N])
	h = (b - a)/N
	key = np.arange(1, N) * h + a
	mid = np.arange(0, N) * h + a + h/2
	return h * (sum(func(key))/3 + 2*sum(func(mid))/3 \
		+ func(a)/6 + func(b)/6)

N = np.arange(1, 36)
plt.clf()

plt.subplot(2, 1, 1)
trap_integral = np.array(map(lambda N: trapezoidal(np.exp, 0, 1, N), N))
trap_error = trap_integral - 1.7182818284590452354
plt.plot(N, trap_error, "g.-", label = "Trapezoidal")
simp_integral = np.array(map(lambda N: simpson(np.exp, 0, 1, N), N))
simp_error = simp_integral - 1.7182818284590452354
plt.plot(N, simp_error, "b.-", label = "Simpson")
plt.legend()
plt.ylabel("Approximation - $\int_0^1 \exp(x)\,dx$")

ax = plt.subplot(2, 1, 2)
plt.plot(N, trap_error, "g.-", label = "Trapezoidal")
plt.plot(N, simp_error, "b.-", label = "Simpson")
plt.legend()
plt.xlabel("$N$")
plt.ylabel("Approximation - $\int_0^1 \exp(x)\,dx$")
plt.ylim(simp_error.min(), simp_error.max())
ax.yaxis.set_major_formatter(FormatStrFormatter("%0.4f"))
plt.tight_layout()
plt.savefig("latex/approximation_errors.pdf")
