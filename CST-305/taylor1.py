##############################################################
# Project 6: Numeric Computations with Taylor Polynomials    #
#                                                            #
# Logan Hoots, Stephen Sanders                               #
# CST - 305                                                  #
# 5/6/2020                                                   #
# Professor R. Citro                                         #
##############################################################

# Imports all the necessary modules
import numpy as np
import sympy as sy
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

# Defines the derivatives 
ddx = [1, -1, 0, -2, -2]
n = int(input("input n value: "))

# Taylor polynomial can be calculated up to the 500th degree
d = 5 
for i in range(500):
    tmp = 2 * (i + 3) * ddx[d-2]
    ddx.append(tmp)
    d += 1

# Returns the factorial of a given integer
def f_(n):
    if n == 1:
        return n
    else:
        return n*f_(n-1)

# Takes the output of the taylor polynomial and places it in an array
def taylor(n, t):
    y = 1
    for i in range(n):
        y = y + (ddx[i + 1] / f_(i + 1)) * t ** (i + 1)
    return y

# Converts to a first order ODE allowing odeint to solve the equation
# Taylor approximations are returned as the solution
def func(Y, t):
    return [Y[1], 2 * t * Y[1] - (t ** 2) * Y[0]]
y0 = [1, -1]

x = np.linspace(0, 3.5)

# Prints the value of the equation at the point 3.5
p1 = taylor(n, x)
print(p1)
act = odeint(func, y0, x)
print('Actual value of y(3.5): ', act[-1][0])
t = 3.5
print('Taylor approximation of y(3.5) when n = 4', 1 - t - (1 / 3) * t ** 3 - (1 / 12) * t ** 4)

a = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4
b = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5
c = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5 - (1 / 45) * x ** 6
d = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5 - (1 / 45) * x ** 6 - (1 / 42) * x ** 7

# Plots the equation among the different approximations 
plt.plot(x, act[:, 0], 'b', label = 'Actual(Odeint)')
plt.plot(x, a, 'k--', label = 'Approximation (n = 4)')
plt.plot(x, b, 'y--', label = 'Approximation (n = 5)')
plt.plot(x, c, 'm--', label = 'Approximation (n = 6)')
plt.plot(x, d, 'r--', label = 'Approximation (n = 7)')
plt.plot(x, p1, 'r', label = 'User')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.title('Part 1')
plt.show()