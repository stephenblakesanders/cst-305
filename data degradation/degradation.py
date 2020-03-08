##############################################################
#                                                            #
# Logan Hoots                                                #
# Stephen Blake Sanders                                      #
#                                                            #
# Ricardo Citro                                              #
# 1 March 2020                                               #
# CST-305                                                    #
#                                                            #
# Project 4 Benchmark: Data Degradation                      #
#                                                            #
##############################################################

#included Libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from sympy import *

#Function to graph our intial equaion
def model(x, t):
  #This is the model of the equation
  sol = exp(-1 * (o + d + m + b + v) * t)
  return sol

#Function graphing the derivative with respect to o
def model2(x, t):
  #This is the model of the derivative
  sol = -1 * o * exp(o * t)
  return sol

#Function graphing the derivative with respect to d
def model3(x, t):
  #This is the model of the derivative
  sol = -1 * d * exp(d * t)
  return sol

#Function graphing the derivative with respect to m
def model4(x, t):
  #This is the model of the derivative
  sol = -1 * m * exp(m * t)
  return sol

#Function graphing the derivative with respect to b
def model5(x, t):
  #This is the model of the derivative
  sol = -1 * b * exp(b * t)
  return sol

#Function graphing the derivative with respect to v
def model6(x, t):
  #This is the model of the derivative
  sol = -1 * v * exp(v * t)
  return sol

#Initializes variables x0 and t
x0 = 100
t = np.linspace(0, 8)

#Each degradation condition is initialized at a different value to show realistic conditions in hard drive degradation
o = .1
d = .2
m = .3
b = .4
v = .5

#Sets each equation to the ODEINT of each model
x1 = odeint(model, x0, t)
x2 = odeint(model2, x0, t)
x3 = odeint(model3, x0, t)
x4 = odeint(model4, x0, t)
x5 = odeint(model5, x0, t)
x6 = odeint(model6, x0, t)

#Plots each model on the graph
plt.plot(t, x1, 'k', linewidth = 2, label = 'general')
plt.plot(t, x2, 'r', linewidth = 2, label = 'o')
plt.plot(t, x3, 'g', linewidth = 2, label = 'd')
plt.plot(t, x4, 'b', linewidth = 2, label = 'm')
plt.plot(t, x5, 'c', linewidth = 2, label = 'b')
plt.plot(t, x6, 'm', linewidth = 2, label = 'v')

#Adds cosmetics to the graph
plt.title("ODEINT")
plt.xlabel("Time")
plt.ylabel("Data Degradation")

#Displays legend and graph
plt.legend()
plt.show()
