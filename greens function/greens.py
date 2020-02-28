##############################################################
#                                                            #
# Logan Hoots                                                #
# Stephen Blake Sanders                                      #
#                                                            #
# Ricardo Citro                                              #
# 27 February 2020                                           #
# CST-305                                                    #
#                                                            #
# Greens Function for Python                                 #
#                                                            #
##############################################################

from numpy import *
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import sympy as sy

# declare variables for sympy processing of equations
x = sy.symbols("x")
t = arange(0.0, 10.0, 0.1)

# defines the function for the first equation
def model1(t):
    # the first equation is put into terms for sympy to process
    eq = sy.Poly((x ** 2) + (2 * x) + (0), x)

    # extracts the coefficients from the sympy equation
    ans = eq.all_coeffs()

    # initializes q1 and q2 variables for use as Lambda1 and Lambda2
    q1 = 1.0
    q2 = 1.0

    # takes the values of the coefficients as floats for calculations
    a = float(ans[0])
    b = float(ans[1])
    c = float(ans[2])
    temp = 0

    # stores b^2 - 4ac in variable d in order to process for the potential of an imaginary number
    d = b * b - 4 * a * c
    if (d < 0):
        # sets d to a positive value if its negative to handle taking the square root of a negative number
        temp = d
        d = -d

    # finalizes the calculations for Lambda1 and Lambda2
    q1 = (-b + sqrt(d)) / (2 * a)
    q2 = (-b - sqrt(d)) / (2 * a)

    # determines the case of the equation based on Lambda values
    if (q1 == q2):
        case = 3
    elif (temp < 0):
        case = 2
    elif (q1 != q2):
        case = 1

    # calls the caseStatement funciton that allows the mathematical value of the general solution to be solved
    return caseStatement(q1, q2, case, t)

# defines the function for the second equation
def model2(t):
    # the second equation is put into terms for sympy to process
    eq = sy.Poly((x ** 2) + (0 * x) + (1), x)

    # extracts the coefficients from the sympy equation
    ans = eq.all_coeffs()

    # takes the values of the coefficients as floats for calculations
    a = float(ans[0])
    b = float(ans[1])
    c = float(ans[2])
    temp = 0

    # stores b^2 - 4ac in variable d in order to process for the potential of an imaginary number
    d = b * b - 4 * a * c
    if (d < 0):
        # sets d to a positive value if its negative to handle taking the square root of a negative number
        temp = d
        d = -d

    # finalizes the calculations for Lambda1 and Lambda2
    q1 = (-b + sqrt(d)) / (2 * a)
    q2 = (-b - sqrt(d)) / (2 * a)

    # determines the case of the equation based on Lambda values
    if (q1 == q2):
        case = 3
    elif (temp < 0):
        case = 2
    elif (q1 != q2):
        case = 1

    # calls the caseStatement funciton that allows the mathematical value of the general solution to be solved
    return caseStatement(q1, q2, case, t)

# calculates the general solution for the equation based on the given case
def caseStatement(q1, q2, case, t):
    if (case == 1):
        # returns the general solution for case 1
        return (-.5 * exp(2 * t) * exp(q1 * t)) + (.5 * exp(q2 * t))
    elif (case == 2):
        # returns the general solution for case 2
        return (-sin(t) * exp(0 * t) * cos(q1 * t)) + ((cos(t) / (-sin(t) * sin(-t) + cos(t) ** 2)) * exp(0 * t) * sin(q2 * t))
    elif (case == 3):
        # case 3 does not exist in the given equations so the general solution is not calculated
        return 3

    # returns zero if the case is not 1, 2 or 3 for error checking
    return 0

# calculates the value of greens function's solution of equation 1
def greens1(t):
    # returns the value of greens function's solution
    return t - .5 * (1 - exp(-2 * t))

# calculates the value of greens function's solution of equation 2
def greens2(t):
    # returns the value of greens function's solution
    return -4 * (-1 + cos(t))

# plots greens function's solution and the homogeneous solution for equation 1 in plot 1
plt1.plot(t, greens1(t), 'g-', linewidth=2, label='Homogeneous')
plt1.plot(t, model1(t), 'b--', linewidth=2, label='Green\'s')
plt1.xlabel("t")
plt1.ylabel("y")
plt1.title("Comparison of Green's Function and\n Homogeneous"
           " Equation for Equation 1")

# shows the legend and the plot for plot 1
plt1.legend()
plt1.show()

# plots greens function's solution and the homogeneous solution for equation 2 in plot 2
plt2.plot(t, greens2(t), 'g-', linewidth=2, label='Homogeneous')
plt2.plot(t, model2(t), 'b--', linewidth=2, label='Green\'s')
plt1.xlabel("t")
plt1.ylabel("y")
plt1.title("Comparison of Green's Function and\n Homogeneous"
           " Equation for Equation 2")

# shows the legend and the plot for plot 2
plt2.legend()
plt2.show()
