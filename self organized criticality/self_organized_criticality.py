##############################################################
#                                                            #
# Logan Hoots                                                #
# Stephen Blake Sanders                                      #
#                                                            #
# Ricardo Citro                                              #
# 15 March 2020                                              #
# CST-305                                                    #
#                                                            #
# Project 5 Benchmark: Self Organized Criticality            #
#                                                            #
##############################################################

#included Libraries
import numpy as np #imports numpy
import matplotlib.pyplot as plt #Imports Matplot
from mpl_toolkits.mplot3d import Axes3D

#File Corruption Function
def file_c(x, y, s=15.0, f=30.0):
    x_dot = s*(y - x) #Sets x_dot equal to s * (y - x)
    y_dot = f*x - y - x*x #Sets y_dot equal to r * x - y - x * x
    return x_dot, y_dot #Returns x_dot and y_dot

#Creates variables
dt = 0.01 #Sets variable for rate
steps = 10000 #Sets step size

#Creates arrays for graphing
xs = np.empty(steps + 1) #Sets array to each step size
ys = np.empty(steps + 1) #Sets array to each step size

#Setting initial values of the system
xs[0], ys[0] = (0., 1.)

#Iterate through the graph, representing the value of continguous space left in the filesystem at a given point in time
for i in range(steps):
    x_dot, y_dot = file_c(xs[i], ys[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)

#Plot graph in 3d space, to give easier examination of graph
fig = plt.figure()
ax = fig.gca(projection='3d')

#Name plot and axis, defining the graph and displaying the graph
ax.plot(xs, ys, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("File Corruption")
plt.show()