import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Variables you can play with:
---------------------------
>>> x0 is the lower limit of integration, should be greater or equal to zero.
>>> H is the height of the mast (m) (upper limit of integration), should be 
    greater than x0.
>>> n is the number of intervals, should be greater than zero and it must be 
    an EVEN number. Make it equal to -1 if you want the program to continue 
    until a certain percentage of error is achieved.
>>> error is maximum error allowed for the result of the program (in %). It
    is used only if n = -1.
'''
x0 = 0 
H = 30
n = -1 
error = 0.001

#the original function (can be changed):
def func(z):
    return 200 * (z / (5 + z)) * math.exp(-2*z/H)

#Variables you cannot play with:
force_values = [] #list for all force values
simpson_results = [] #list for results with different number of intervals
z_axis = np.linspace(x0, H, (H-x0)*10) #list of all values of z

#calculating all force values of f(x) for the original function:
for z in z_axis:
    force_value = func(z) #use the function to find f(x) at x
    force_values.append(force_value) #add the calculated value to the list

#implementing Simpson's 1/3:
def simpsonRule(x0,H,n):
    delta_z = (H - x0) / n #calculating step size
    
    integration = func(x0) + func(H) #both f(x0) and f(xn) are always a part of the equation
    
    for i in range(1,n):
            z_i = x0 + i*delta_z #the value of z at interval i
            
            #apply Simpson's 1/3 Rule formulas:
            if i%2 == 0: #check if a number is even
                integration = integration + 2 * func(z_i) 
            else:
                integration = integration + 4 * func(z_i)
    
    integration = integration * (delta_z / 3) #finding the final integration value
    return integration #return the final integration value as a result of the function

#in case the user wants to get a result with a certain maximum 
#error allowed the following lines of code will be executed:
if n == -1:
    result = simpsonRule(x0, H, 2) #using the simpsonRule() function to calculate with 2 interval
    simpson_results.append(result) #add the result from using 2 intervals
    result = simpsonRule(x0, H, 4) #using the simpsonRule() function to calculate with 4 intervals
    simpson_results.append(result) #add the result from using 4 intervals
    n_values = [2, 4] #list of all values of n
    n_total = 4 #a variable to keep track of the current value of n
    
    #iterate until the error requirement is met:
    while (simpson_results[-1] - simpson_results[-2]) > (((H-x0)*error)/100):
        n_total += 2
        result = simpsonRule(x0, H, n_total) #using the simpsonRule() function to calculate with n intervals
        n_values.append(n_total) #add the current value of n to the list of all n values
        simpson_results.append(result) #add the result from using n intervals
        

#in case the user wants to get a result with a certain number 
#of intervals the following lines of code will be executed:
else:
    result = simpsonRule(x0, H, n) #using the simpsonRule() function to calculate the total force

#output logic:
def output():
    #displaying the original function f(x):
    plt.figure(dpi=300) 
    plt.title("Simpson's 1/3 Rule")
    plt.xlabel("f(z)")
    plt.ylabel("z")
    plt.plot(force_values, z_axis, color="blue")
    plt.plot( np.zeros(len(z_axis)), z_axis, color="brown")
    plt.show()
    
    if n == -1:
        print(f"---------------------------------------------------------------------")
        print(f"The result of Simpson's 1/3 Rule with {error}% error is: {simpson_results[-1]:.10f} ({n_total} intervals required)")
        print(f"---------------------------------------------------------------------")
        
        #displaying the results form the Simson's 1/3 Rule function:
        plt.figure(dpi=300) 
        plt.title("Simpson's 1/3 Rule")
        plt.xlabel("n")
        plt.ylabel("results")
        plt.plot(n_values, simpson_results, color="blue")
        plt.plot(n_values, ([simpson_results[-1]] * len(n_values)), color="gray")
        plt.show()
        
        #print table of the results from the Simpson's 1/3 Rule function with different number of intervals
        pd.set_option("display.precision", 10) #set tables precision
        simpson_data = {'n':n_values, 'results':simpson_results}
        print(pd.DataFrame(simpson_data, columns=['n', 'results']).to_string(index=False))
    else:
        if n%2 == 0:
            print(f"---------------------------------------------------------------------")
            print(f"The result of Simpson's 1/3 Rule with {n} intervals is: {result:.10f}")
            print(f"---------------------------------------------------------------------")
        else:
            print(f"---------------------------------------------------------------------")
            print(f"ERROR: an ODD number of intervals is used. Use an EVEN number of intervals.")
            print(f"---------------------------------------------------------------------")

output()