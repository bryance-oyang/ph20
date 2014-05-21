#!/usr/bin/python

import numpy as np

h = np.loadtxt("data/h.dat")

# do euler method for $\ddot{x} = -x$, with initial conditions
# $x(0) = 1; \dot{x}(0) = 0$
def euler(h):
	#$\begin{pmatrix}1 & h\\-h & 1\end{pmatrix} \begin{pmatrix}x_i\\v_i\end{pmatrix} = \begin{pmatrix}x_{i+1}\\v_{i+1}\end{pmatrix}$
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

# save euler method data from $0$ to $6\pi$
(x, v) = euler(h);
t = np.arange(0, int(6*np.pi/h)) * h
np.savetxt("data/problem1.dat", np.array([t, x, v]).T, delimiter = " | ")

# save error data
x_anal = np.cos(t)
v_anal = -np.sin(t)
np.savetxt("data/problem2.dat", np.array([t, x_anal - x, v_anal - v]).T, delimiter = " | ")

hs = 0.03 * 2.**-np.arange(0,5)
maxes = np.array([])
for hi in hs:
	(x, v) = euler(hi)
	t = np.arange(0, int(6*np.pi/hi)) * hi
	x_anal = np.cos(t)
	maxe = np.max(np.abs(x - x_anal))
	maxes = np.append(maxes, maxe)

# save max errors vs $h$
np.savetxt("data/problem3.dat", np.array([hs, maxes]).T, delimiter = " | ")

# energy as function of $t$
(x, v) = euler(h);
t = np.arange(0, int(6*np.pi/h)) * h
E = x**2 + v**2;
np.savetxt("data/problem4.dat", np.array([t, E]).T, delimiter = " | ")

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

# max errors vs $h$
hs = 0.03 * 2.**-np.arange(0,5)
maxes_imp = np.array([])
maxes_exp = np.array([])
for hi in hs:
	(x, v) = euler(hi)
	t = np.arange(0, int(6*np.pi/hi)) * hi
	x_anal = np.cos(t)
	maxe = np.max(np.abs(x - x_anal))
	maxes_exp = np.append(maxes_exp, maxe)

	(x, v) = euler_implicit(hi)
	maxe = np.max(np.abs(x - x_anal))
	maxes_imp = np.append(maxes_imp, maxe)

# save max errors vs $h$
np.savetxt("data/problem5_1.dat", np.array([hs, maxes_imp, maxes_exp]).T, delimiter = " | ")

# energy as function of $t$
(x, v) = euler(h);
t = np.arange(0, int(6*np.pi/h)) * h
E = x**2 + v**2;
(x, v) = euler_implicit(h);
E_imp = x**2 + v**2;
np.savetxt("data/problem5_2.dat", np.array([t, E, E_imp]).T, delimiter = " | ")

# phase space of explicit/implicit
t = np.arange(0, int(6*np.pi/h)) * h
(x, v) = euler(h)
(x_imp, v_imp) = euler_implicit(h);
np.savetxt("data/p2_problem1.dat", np.array([x, v, x_imp, v_imp]).T, delimiter = " | ")

def euler_symp(h, end):
	initial_cond = np.matrix([[1, 0]]).transpose()
	x = np.array([initial_cond[0, 0]]);
	v = np.array([initial_cond[1, 0]]);
	symp = np.matrix([[1, h], [-h, 1 - h**2]])
	cur = initial_cond;
	for k in range(1, int(end/h)):
		cur = symp * cur
		x = np.append(x, cur[0, 0])
		v = np.append(v, cur[1, 0])
	return (x, v)

# phase space of symp
t = np.arange(0, int(6*np.pi/h)) * h
(x, v) = euler_symp(h, 6*np.pi)
(x_anal, v_anal) = (np.cos(t), -np.sin(t))
np.savetxt("data/p2_problem2.dat", np.array([x, v, x_anal, v_anal]).T, delimiter = " | ")

# energy as function of $t$
(x, v) = euler_symp(h, 6 * np.pi);
t = np.arange(0, int(6*np.pi/h)) * h
E = x**2 + v**2;
np.savetxt("data/p2_problem3.dat", np.array([t, E]).T, delimiter = " | ")

# long term evolution; plotting last 3 cycles after 360 cycles total
# to see lag between symp and anal
cycles = 360;
(x, v) = euler_symp(h, 2 * np.pi * cycles)
t = np.arange(0, int(2 * np.pi * cycles/h))*h
cutoff = int(2 * np.pi * (cycles - 3) / h)
t = t[cutoff:]
x = x[cutoff:]
x_anal = np.cos(t)
np.savetxt("data/p2_problem4.dat", np.array([t, x, x_anal]).T, delimiter = " | ")
