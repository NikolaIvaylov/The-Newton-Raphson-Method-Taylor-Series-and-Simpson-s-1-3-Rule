import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.misc import derivative

#Variables you can play with:
x0 = 3 #Starting point
a = 10 #value of a (a > 0)
check = 0.00000001 #how close it should be to zero? (use 0.00000001 for 10^-8)
digits_behind_comma = 10 #how many digits behind the comma?

#Variables you cannot play with:
x_values = [] #list for all values of x
x_values.append(x0) #add the starting value x0

#the original function f(x) (can be changed):
def func(x):
    return x**2 - a

def first_derivative(x):
    return derivative(func, x, dx=1e-6)

last_x = x_values[-1]
#Every iteration check if the func(x) is close enough to zero:
while func(last_x) > check or func(last_x) < -(check):
    last_x = x_values[-1] #get the last x value (Xn)
    next_x = last_x - (func(last_x)/first_derivative(last_x)) #use xn to calculate next x (Xn+1)
    x_values.append(next_x) #add Xn+1 to the list of all values of x


x_differences = [] #list of the differences between the x values
#calculate the differences between the x values:
for i in range(1, len(x_values)):
    x_diff = abs(x_values[i-1] - x_values[i])
    x_differences.append(x_diff)
    
#output logic:
def output():
    pd.set_option("display.precision", digits_behind_comma) #set tables precision
    
    x_data = {'x':x_values}
    print(pd.DataFrame(x_data, columns=["x"]))
    print()

    #print table of differences between x values:
    diff_data = {'difference':x_differences}
    print(pd.DataFrame(diff_data, columns=["difference"]))

    n_values = range(0, len(x_values)) #make a list of numbers from 0 to n

    #Displaying the x_values graph:
    plt.figure(dpi=300) 
    plt.title(f"Newton-Raphson Method (x values)")
    plt.xlabel("n")
    plt.ylabel("x")
    plt.plot(n_values, x_values, color="blue")
    plt.show()

    #Displaying the x_differences graph:
    plt.figure(dpi=300) 
    plt.title(f"Newton-Raphson Method (x differences)")
    plt.xlabel("n")
    plt.ylabel("difference in x")
    plt.plot(range(0, len(x_values)-1), x_differences, color="red")
    plt.plot(range(0, len(x_values)-1), np.zeros(len(x_values)-1), color="gray")
    plt.show()

output()