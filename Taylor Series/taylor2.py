##############################################################
# Project 6: Numeric Computations with Taylor Polynomials    #
#                                                            #
# Logan Hoots, Stephen Sanders                               #
# CST - 305                                                  #
# 5/6/2020                                                   #
# Professor R. Citro                                         #
##############################################################

# Imports all necessary libraries for the project
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt_
import math
from sympy import *

# Main function in which the general solution is calculated
def model_(input_):
    # Defines the first two values of a_0 and a_1, allowing the fist values to be calcuated into a_0 and a_1x
    a = [1, 1]

    # Declaring i as a float in order to get nonzero numbers
    i = 0.0

    # Iterates the amount of times the user inputs
    for x in range(0, input_ - 1):
        # Appends every new value into the array for every given iteration
        a.append(round((i**2 - i + 1) / (4 *(i + 2) * (i + 1 )) * a[x], 4))
        i += 1

    print("\nGENERAL SOLUTION: \n")
    print("y = "),

    # Prints out the first two cases of a_0 and a_1
    # Handles the coordinating association between a_0 and a_1 
    for x in range(0, len(a)):
        if (x == 0):
            print("a_0 +"),
        elif (x == 1):
            print("a_1x +"),
        elif (x % 2) == 0:
            print(str(a[x]) + " * a_0x^" + str(x) + " +"),
        elif (x % 2) != 0:
            print(str(a[x]) + " * a_1x^" + str(x) + " +"),

    print("...")
    print("\nGENERAL SOLUTION SIMPLIFIED: ")

    # Prints the simplified general solution
    print("\ny = a_0 ("),
    for x in range(0, len(a)):
        if (x % 2) == 0:
            print(str(a[x]) + "x^" + str(x) + " +"),

    # Prints the simplified general solution
    print("...) + a_1 ("),
    for x in range(0, len(a)):
        if (x % 2) != 0:
            print(str(a[x]) + "x^" + str(x) + " +"),
    print("...)")
        
# Calls the main function
model_(input("enter n value:" ))
print("\n")
