##############################################################
#                                                            #
# Logan Hoots                                                #
# Stephen Blake Sanders                                      #
#                                                            #
# Ricardo Citro                                              #
# 19 April 2020                                              #
# CST-305                                                    #
#                                                            #
# Project 7: Code Errors and Butterfly Effect Part 1         #
#                                                            #
##############################################################

#included Libraries
import numpy as np #imports numpy
import matplotlib.pyplot as plt #Imports Matplot
from mpl_toolkits.mplot3d import Axes3D

#Creates a boolean variable for looping through the code
repeat = True

#Loops while repeat is set to true
while (repeat == True): 
    #Takes user input for Sigma, Rho, Beta
    s = float(input("Enter sigma value: ")) #Asks user to input sigma value
    r = float(input("Enter rho value: "))   #Asks user to input rho value
    b = float(input("Enter beta value: "))  #Asks user to input beta value

    #Lorenz Function to Calculate the graph values
    def lorenz(x, y, z):
        x_dot = s*(y - x)     #Define x_dot equation
        y_dot = x*(r - z) - y #Define y_dot equation
        z_dot = x*y - b*z     #Define z_dot equation
        return x_dot, y_dot, z_dot #Returns x_dot, y_dot and z_dot

    #Creates variables
    dt = 0.01 #Sets variable for rate
    steps = 10000 #Sets step size

    #Creates arrays for graphing
    xs = np.empty(steps + 1) #Sets array to each step size
    ys = np.empty(steps + 1) #Sets array to each step size
    zs = np.empty(steps + 1) #Sets array to each step size

    #Setting initial values of the system
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    #Iterate through the graph, representing the value of continguous space left in the filesystem at a given point in time
    for i in range(steps):
        #Setes x_dot, y_dot, z_dot to the lorenz function returned values
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt) #Calculates xs 
        ys[i + 1] = ys[i] + (y_dot * dt) #Calculates ys 
        zs[i + 1] = zs[i] + (z_dot * dt) #Calculates zs 

    #Plot graph in 3d space, to give easier examination of graph
    fig = plt.figure() #Defines the figure for the plot
    ax = fig.gca(projection='3d') #Defines the graph in three dimensions

    #Name plot and axis, defining the graph and displaying the graph
    ax.plot(xs, ys, zs, lw=0.5) #Plots the graph of xs by ys by zs
    ax.set_xlabel("X Axis") #Labels x axis
    ax.set_ylabel("Y Axis") #Labels y axis
    ax.set_zlabel("Z Axis") #Labels z axis
    ax.set_title("Project 7: Code Errors and Butterfly Effect") #Adds Graph Title
    plt.show() #Plots the Graph
    
    #Asks the user to continue
    repeat_ = int(input("Enter 0 to quit, 1 to continue: "))

    if (repeat_ == 0): #Checks if user input is 0
        repeat = False #Stops the loop
        