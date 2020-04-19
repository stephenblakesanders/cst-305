##############################################################
#                                                            #
# Logan Hoots                                                #
# Stephen Blake Sanders                                      #
#                                                            #
# Ricardo Citro                                              #
# 19 April 2020                                              #
# CST-305                                                    #
#                                                            #
# Project 7: Code Errors and Butterfly Effect Part 2 b       #
#                                                            #
##############################################################

#Initializes variables lam, mu, and rho
lam = 125.0
mu = 500.0
rho = 0.25

#a) Utilization Function
def Utilization(lam, mu):
    rho = lam / mu #Calculates rho
    return rho #Returns Rho

#b) Throughput Function
def Throughput(mu):
    X = (1 / (1 - rho)) * (1 / mu) #Calculates Throughput
    return X #Returns Throughput

#c) Mean Number Function
def Mean_number(rho):
    E_n = rho / (1 - rho) #Calculates Mean Number
    return E_n #Returns Mean Number

#d) Mean Time Function
def Mean_time(lam):
    E_t = 1 / lam #Calculates Mean Time
    return E_t #Returns Mean Time

#Outputs the Ultilzation example
print("\nUtilization with a value of lam = 125, mu = 500 and then lam = 250, mu = 1000")
print(Utilization(lam, mu)) #Original
print(Utilization(2 * lam, 2 * mu)) #Changed numbers
print("\n")

#Ouputs the Throughput Example
print("Throughput with a value of mu = 500, rho = .25 and then mu = 1000")
print(Throughput(mu)) #Original
print(Throughput(2 * mu)) #Changed Numbers
print("\n")

#Outputs the Mean Number Example
print("E[N] with a value of rho = .25")
print(Mean_number(rho)) #Original
print(Mean_number(rho)) #Changed numbers
print("\n")

#Outputs the Mean Time Example
print("E[T] with a value of lam = 125 and then lam = 250")
print(Mean_time(lam)) #Original
print(Mean_time(2 * lam)) #Changed numbers
print("\n")