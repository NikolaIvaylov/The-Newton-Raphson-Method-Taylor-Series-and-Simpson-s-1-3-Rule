import sympy as sym
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

#the original function (can be changed):
def func(x):
    return 9 * x**4 * math.exp(-12*x)

#Variables you can play with:
a = 0.075 #the point around which the graphs will be shown
graph_range = 0.05 #determines how zoomed in/out the graph is
n = 4 #determines how much terms the Taylor Series have

#Variables you cannot play with:
fx_original = [] #list for all values of f(x) for the original function
fx_Taylor = [] #list for all values of f(x) for the Taylor Series
x_axis = np.linspace(a-graph_range, a+graph_range, 100000) #list of all values of x

#calculating all values of f(x) for the original function:
for x in x_axis:
    f_x = func(x) #use the function to find f(x) at x
    fx_original.append(f_x) #add the calculated value to the list

#calculating all values of f(x) for the Taylor Series:
for x in x_axis:
    x_Taylor = func(a) #the first term in the Taylor Series is always = f(a)
    for i in range (1, n):
        #calculating the i-th order derivative of f(a):
        i_th_derivative = derivative(func, a, dx=1e-6, n=i, order=5)
        #adding the i-th derivative * (x - a)^i / i! to the other terms:
        x_Taylor = x_Taylor + i_th_derivative * ( (x - a)**i / math.factorial(i) )
    fx_Taylor.append(x_Taylor) #add the final approximated x value to the list 

#output logic:
def output():
    #displaying the original function f(x):
    plt.figure(dpi=300) 
    if n == 1:
        plt.title(f"Taylor Series (with 1 term)")
    else:
        plt.title(f"Taylor Series (with {n} terms)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x_axis, fx_original, color="blue", label="original")

    #displaying the Taylor series:
    plt.plot(x_axis, fx_Taylor, color="red", label="Taylor series")

    plt.legend()
    plt.show()

output()
