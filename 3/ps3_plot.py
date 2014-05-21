#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

h = np.loadtxt("data/h.dat")

# make euler method plot from $0$ to $6\pi$
data = np.loadtxt("data/problem1.dat", delimiter = " | ")
t = data[:, 0]
x = data[:, 1]
v = data[:, 2]
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
data = np.loadtxt("data/problem2.dat", delimiter = " | ")
t = data[:, 0]
dx = data[:, 1]
dv = data[:, 2]
plt.clf()
plt.subplot(2, 1, 1)
plt.plot(t, dx, "b.-")
plt.ylabel("$x_{anal} - x(t)$")
plt.title("$h = %0.3f$" % (h))
plt.subplot(2, 1, 2)
plt.plot(t, dv, "g.-")
plt.xlabel("$t$")
plt.ylabel("$v_{anal} - v(t)$")
plt.savefig("latex/problem2.pdf")

# plot of max errors vs $h$
data = np.loadtxt("data/problem3.dat", delimiter = " | ")
hs = data[:, 0]
maxes = data[:, 1]
plt.clf()
plt.plot(hs, maxes, "g.-")
plt.xlabel("$h$")
plt.ylabel("Max error")
plt.savefig("latex/problem3.pdf")

# energy as function of $t$
data = np.loadtxt("data/problem4.dat", delimiter = " | ")
t = data[:, 0]
E = data[:, 1]
plt.clf()
plt.plot(t, E, ".-");
plt.ylim([0, plt.ylim()[1]]);
plt.xlabel("$t$");
plt.ylabel("$E = x^2 + v^2$");
plt.title("$h = %0.3f$" % (h))
plt.savefig("latex/problem4.pdf")

# plot of max errors vs $h$
data = np.loadtxt("data/problem5_1.dat", delimiter = " | ")
hs = data[:, 0]
maxes_imp = data[:, 1]
maxes_exp = data[:, 2]
plt.clf()
plt.plot(hs, maxes_imp, "b.-", label = "Implicit")
plt.plot(hs, maxes_exp, "g.-", label = "Explicit")
plt.xlabel("$h$")
plt.ylabel("Max error")
plt.legend(loc = "upper left")
plt.savefig("latex/problem5_1.pdf")

# energy as function of $t$
data = np.loadtxt("data/problem5_2.dat", delimiter = " | ")
t = data[:, 0]
E = data[:, 1]
E_imp = data[:, 2]
plt.clf()
plt.plot(t, E, "b.-", label = "Explicit");
plt.plot(t, E_imp, "g.-", label = "Implicit")
plt.ylim([0, plt.ylim()[1]]);
plt.xlabel("$t$");
plt.ylabel("$E = x^2 + v^2$");
plt.title("$h = %0.3f$" % (h))
plt.legend(loc = "upper left");
plt.savefig("latex/problem5_2.pdf")

# phase space of explicit/implicit
data = np.loadtxt("data/p2_problem1.dat", delimiter = " | ")
x = data[:, 0]
v = data[:, 1]
x_imp = data[:, 2]
v_imp = data[:, 3]
plt.clf()
plt.plot(x, v, "b.-", label = "explicit");
plt.plot(x_imp, v_imp, "g.-", label = "implicit")
plt.xlabel("$x$")
plt.ylabel("$v$")
plt.title("$h = %0.3f$" % (h))
plt.legend();
plt.grid(True);
plt.savefig("latex/p2_problem1.pdf")

# phase space of symp
data = np.loadtxt("data/p2_problem2.dat", delimiter = " | ")
x = data[:, 0]
v = data[:, 1]
x_anal = data[:, 2]
v_anal = data[:, 3]
plt.clf()
plt.plot(x, v, "r.-", label = "Symplectic");
plt.plot(x_anal, v_anal, "b.-", label = "Analytic");
plt.xlabel("$x$")
plt.ylabel("$v$")
plt.title("$h = %0.3f$" % (h))
plt.legend()
plt.grid(True);
plt.savefig("latex/p2_problem2.pdf")

# energy as function of $t$
data = np.loadtxt("data/p2_problem3.dat", delimiter = " | ")
t = data[:, 0]
E = data[:, 1]
plt.clf()
plt.plot(t, E, "r.-")
plt.xlabel("$t$");
plt.ylabel("$E = x^2 + v^2$");
plt.title("$h = %0.3f$" % (h))
plt.savefig("latex/p2_problem3.pdf")

# long term evolution; plotting last 3 cycles after 360 cycles total
# to see lag between symp and anal
data = np.loadtxt("data/p2_problem4.dat", delimiter = " | ")
t = data[:, 0]
x = data[:, 1]
x_anal = data[:, 2]
plt.clf()
plt.plot(t, x, "r.-", label = "Sympl")
plt.plot(t, x_anal, "b.-", label = "Analytic")
plt.legend()
plt.xlabel("$t$")
plt.ylabel("$x(t)$")
plt.title("$h = %0.3f$" % (h))
plt.savefig("latex/p2_problem4.pdf")
