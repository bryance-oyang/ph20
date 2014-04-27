#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
from matplotlib.ticker import FormatStrFormatter

# use trapezoid thing to integrate using N subdivisions
# returns $\int_a^b func(x)\,dx$
def trapezoidal(func, a, b, N):
	[a, b, N] = map(float, [a, b, N])
	h = (b - a)/N
	x = np.arange(1, N) * h + a
	return h * (sum(func(x)) + func(a)/2 + func(b)/2)

# use simpson's thing to integrate using N subdivisions
# returns $\int_a^b func(x)\,dx$
def simpson(func, a, b, N):
	[a, b, N] = map(float, [a, b, N])
	h = (b - a)/N
	key = np.arange(1, N) * h + a
	mid = np.arange(0, N) * h + a + h/2
	return (h * (sum(func(key))/3 + 2*sum(func(mid))/3
		+ func(a)/6 + func(b)/6))

# make plots to see convergence of $\int_0^1 \exp(x)\,dx$ as
# number of subdivisions (N) increases for both trapezoid and simpson
N = np.logspace(0, 4, num = 100).astype(int)
plt.clf()
trap_integral = np.array(map(lambda N: trapezoidal(np.exp, 0, 1, N), N))
trap_error = trap_integral - 1.7182818284590452354
plt.loglog(N, trap_error, "g.-", label = "Trapezoidal")
simp_integral = np.array(map(lambda N: simpson(np.exp, 0, 1, N), N))
simp_error = simp_integral - 1.7182818284590452354
plt.loglog(N, simp_error, "b.-", label = "Simpson")
plt.ylabel("Approximation - $\int_0^1 \exp(x)\,dx$")
plt.legend()
plt.xlabel("$N$")
plt.tight_layout()
plt.savefig("latex/approximation_errors.pdf")

# evaluates $\int_a^b func(x)\,dx$ using simpson's thing
# with $N, 2N, 4N, 8N,$ etc subdivisions until requested accuracy is reached
# (simpson($2^{k+1} N$) - simpson($2^k N$))/simpson($2^k N$) < requested accuracy
def integrate(func, a, b, N, requested_accuracy):
	k = 0
	prev = simpson(func, a, b, N * 2**k)
	while True:
		cur = simpson(func, a, b, N * 2**(k+1))
		if abs((prev - cur)/prev) < requested_accuracy:
			break
		k += 1
		prev = cur
	return cur

# some tests
print ("\\int_0^1 e^x\\,dx \\approx %0.10f"
	% integrate(np.exp, 0, 1, 1, 0.00001))
print ("\\int_0^1 x^9\\,dx \\approx %0.10f"
	% integrate(lambda x: x**9, 0, 1, 1, 0.00001))

print scipy.integrate.quad(np.exp, 0, 1)
print scipy.integrate.romberg(np.exp, 0, 1)
