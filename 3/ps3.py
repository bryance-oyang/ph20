#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# do euler method for $\ddot{x} = -x$, with initial conditions
# $x(0) = 1; \dot{x}(0) = 0$
def euler(h):
	# 1   h   xi     x{i+1}
	#       *      = 
	# -h  1   vi     v{i+1}
	#$\begin{pmatrix}1 & h\\-h & 1\end{pmatrix} \begin{pmatrix}x_i\\v_i\end{pmatrix} = \begin{pmatrix}x_{i+1}\\v_{i+1}\end{pmatrix}
	initial_cond = np.matrix([[1, 0]]).transpose()
	x = np.array([initial_cond[0, 0]]);
	v = np.array([initial_cond[1, 0]]);
	explicit = np.matrix([[1, h], [-h, 1]])
	cur = initial_cond;
	for k in range(1, int(6*np.pi/h)):
		cur = explicit * cur
		x = np.append(x, cur[0, 0])
		v = np.append(v, cur[1, 0])
	return (x, v)

# make euler method plot from $0$ to $6\pi$
h = 0.1
(x, v) = euler(h);
t = np.arange(0, int(6*np.pi/h)) * h
plt.subplot(2, 1, 1)
plt.plot(t, x, "b.-")
plt.ylabel("$x(t)$")
plt.title("$h = %0.3f$" % (h))
plt.subplot(2, 1, 2)
plt.plot(t, v, "g.-")
plt.xlabel("$t$")
plt.ylabel("$v(t)$")
plt.savefig("latex/problem1.pdf")

# make error plots
x_anal = np.cos(t)
v_anal = -np.sin(t)
plt.clf()
plt.subplot(2, 1, 1)
plt.plot(t, x_anal - x, "b.-")
plt.ylabel("$x_{anal} - x(t)$")
plt.title("$h = %0.3f$" % (h))
plt.subplot(2, 1, 2)
plt.plot(t, v_anal - v, "g.-")
plt.xlabel("$t$")
plt.ylabel("$v_{anal} - v(t)$")
plt.savefig("latex/problem2.pdf")

hs = 0.03 * 2.**-np.arange(0,5)
maxes = np.array([])
for h in hs:
	(x, v) = euler(h)
	t = np.arange(0, int(6*np.pi/h)) * h
	x_anal = np.cos(t)
	maxe = np.max(np.abs(x - x_anal))
	maxes = np.append(maxes, maxe)

# plot of max errors vs $h$
plt.clf()
plt.plot(hs, maxes, "g.-")
plt.xlabel("$h$")
plt.ylabel("Max error")
plt.savefig("latex/problem3.pdf")

# energy as function of $t$
h = 0.1;
(x, v) = euler(h);
t = np.arange(0, int(6*np.pi/h)) * h
E = x**2 + v**2;
plt.clf()
plt.plot(t, E, ".-");
plt.ylim([0, plt.ylim()[1]]);
plt.xlabel("$t$");
plt.ylabel("$E = x^2 + v^2$");
plt.title("$h = %0.3f$" % (h))
plt.savefig("latex/problem4.pdf")

# implicit thing
def euler_implicit(h):
	initial_cond = np.matrix([[1, 0]]).transpose()
	x = np.array([initial_cond[0, 0]]);
	v = np.array([initial_cond[1, 0]]);
	# inverse of [[1, -h], [h, 1]]
	implicit = np.matrix([[1, h], [-h, 1]]) / (1 + h**2)
	cur = initial_cond;
	for k in range(1, int(6*np.pi/h)):
		cur = implicit * cur
		x = np.append(x, cur[0, 0])
		v = np.append(v, cur[1, 0])
	return (x, v)

hs = 0.03 * 2.**-np.arange(0,5)
maxes_imp = np.array([])
maxes_exp = np.array([])
for h in hs:
	(x, v) = euler(h)
	t = np.arange(0, int(6*np.pi/h)) * h
	x_anal = np.cos(t)
	maxe = np.max(np.abs(x - x_anal))
	maxes_exp = np.append(maxes_exp, maxe)

	(x, v) = euler_implicit(h)
	maxe = np.max(np.abs(x - x_anal))
	maxes_imp = np.append(maxes_imp, maxe)

# plot of max errors vs $h$
plt.clf()
plt.plot(hs, maxes_imp, "b.-", label = "Implicit")
plt.plot(hs, maxes_exp, "g.-", label = "Explicit")
plt.xlabel("$h$")
plt.ylabel("Max error")
plt.legend(loc = "upper left")
plt.savefig("latex/problem5_1.pdf")

# energy as function of $t$
h = 0.1;
(x, v) = euler(h);
t = np.arange(0, int(6*np.pi/h)) * h
E = x**2 + v**2;
plt.clf()
plt.plot(t, E, "b.-", label = "Explicit");
(x, v) = euler_implicit(h);
E = x**2 + v**2;
plt.plot(t, E, "g.-", label = "Implicit")
plt.ylim([0, plt.ylim()[1]]);
plt.xlabel("$t$");
plt.ylabel("$E = x^2 + v^2$");
plt.title("$h = %0.3f$" % (h))
plt.legend(loc = "upper left");
plt.savefig("latex/problem5_2.pdf")
