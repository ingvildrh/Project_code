from math import inf
import matplotlib.pyplot as plt
import numpy as np
import scipy 

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
                 # Display the plot
print("hei")

ANS = scipy.optimize.linprog(
    c = [-1, -2], 
    A_ub=[[1, 1]], 
    b_ub=[6],
    bounds=(1, 5),
    method='highs'
)
f= np.array([[-1], [0]])
H0 = np.array([[1,0], [0,1 ], [-1,0], [0,-1], [1,0], [0,1]])
h0=np.array([[1000], [1000], [1000],[1000],[5],[5]])
print("f")
print(f)
print("H0")
print(H0)
print("h0")
print(h0)
OPT = scipy.optimize.linprog(-1*f, A_ub = H0, b_ub=h0, bounds=(None, None), method='highs-ds') 
print(OPT.fun)
print(OPT.x)
print(OPT.success)