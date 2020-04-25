##############################################################
#                                                            #
# Logan Hoots                                                #
# Stephen Blake Sanders                                      #
#                                                            #
# Ricardo Citro                                              #
# 26 April 2020                                              #
# CST-305                                                    #
#                                                            #
# Project 8: Numerical Integration                           #
#                                                            #
##############################################################

#imports libraries for math and plotting
import numpy as np
import matplotlib.pyplot as plt

def f(x): #Defines the function
    return .242633 * x + 102.1866 #Returns the natural log of x

#Declares the bounds of 0 -> e and allows user to input N 
a = 0; b = 30; N = 30
n = 100.0 #Shows the graph in more points, gives smoother shape
width_ = 0.0 #Initializes variable for column width

#Declaring the linespace for the points of the Reimann sum
x = np.linspace(a,b,N+1) #x values
y = .242633 * x + 102.1866 #y values

#Declaring the linespace for the Graph of ln(x)
X = np.linspace(a,b,n*N+1) #x values
Y = .242633 * X + 102.1866 #y values

#Creates a bit plot to allow the three graphs to show up
plt.figure(figsize=(15,5))

#Calculates the value of the width of the Reimann sum rectangles
width_ = (b - a) / N

#Initialization of variables for looping and printing out the value
#of the Reimann Sum
i = 0.0
Area = 0.0

plt.subplot(1,3,1) #Places the Left-Hand graph in the correct place
plt.plot(X,Y,'b') #Plots the Left-Hand graph
x_left = x[:-1] #X Left endpoints
y_left = y[:-1] #Y Left endpoints
plt.plot(x_left,y_left,'b.',markersize=10) #Plots the Left-hand graph points
plt.bar(x_left,y_left, width_,alpha=0.2,align='edge',edgecolor='b') #Plots the Left-Hand graph rectangles
plt.title('Left Riemann Sum, N = {}'.format(N)) #Titles the Left-Hand Graph
axis = plt.gca() #Frames the graph correctly
axis.set_xlim([0, 30]) #Creates Bounds for the x-axis
axis.set_ylim([80, 140]) #Creates Bounds for the y-axis


plt.subplot(1,3,2) #Places the Midpoint graph in the correct place
plt.plot(X,Y,'b') #Plots the Midpoint graph
x_mid = (x[:-1] + x[1:])/2 #X midpoints
y_mid = .242633 * x_mid + 102.1866 #Y midpoints
plt.plot(x_mid,y_mid,'b.',markersize=10) #Plots the Midpoint graph points
plt.bar(x_mid,y_mid, width_,alpha=0.2,edgecolor='b') #Plots the Midpoint graph rectangles
plt.title('Midpoint Riemann Sum, N = {}'.format(N)) #Titles the Midpoint Graph
axis = plt.gca() #Frames the graph correctly
axis.set_xlim([0, 30]) #Creates Bounds for the x-axis
axis.set_ylim([80, 140]) #Creates Bounds for the y-axis


plt.subplot(1,3,3) #Places the Right-Hand graph in the correct place
plt.plot(X,Y,'b') #Plots the Right-Hand graph
x_right = x[1:] #X Right endpoints
y_right = y[1:] #Y Right endpoints
plt.plot(x_right, y_right, 'b.', markersize = 10) #Plots the Right-Hand graph points
plt.bar(x_right, y_right, -1 * width_, alpha = 0.2, align = 'edge', edgecolor = 'b') #Plots the Right-Hand graph rectangles
plt.title('Right Riemann Sum, N = {}'.format(N)) #Titles the Right-Hand Graph
axis = plt.gca() #Frames the graph correctly
axis.set_xlim([0, 30]) #Creates Bounds for the x-axis
axis.set_ylim([80, 140]) #Creates Bounds for the y-axis

print("The approximate Left-Hand area is = ", y_left[N-1]) #Calculates approx area of Left-Hand sum
print("The approximate Middle area is = ", y_mid[N-1]) #Calculates approx area of Middle sum
print("The approximate Right-Hand area is = ", y_right[0] + 1) #Calculates approx area of Right-Hand sum

plt.show() #Shows the plot