from math import inf
import matplotlib.pyplot as plt
import numpy as np
import scipy 
from scipy import optimize
from scipy.sparse import csr_matrix



import scipy.sparse as sp


x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
                 # Display the plot
print("hei")
'''
ANS = scipy.optimize.linprog(
    c = [-1, -2], 
    A_ub=[[1, 1]], 
    b_ub=[6],
    bounds=(1, 5),
    method='highs'
)
'''
f= np.array([[-1, 0]])
H0 = np.array([[1,0], [0,1 ], [-1,0], [0,-1], [1,0], [0,1]])
h0=np.array([[1000], [1000], [1000],[1000],[5],[5]])
h01=np.array([[1000, 1000, 1000,1000,5,5]])
print("f")
print(f)
print("H0")
print(H0)
print("h0")
print(h0)

# Q = np.array([[-1], [0]])
# A = np.array([[1,0], [0,1 ], [-1,0], [0,-1], [1,0], [0,1]])
# b = np.array([[1000], [1000], [1000],[1000],[5],[5]])
# m = gp.Model()
# x = m.addMVar(2, ub=1.0)

# m.setMObjective(Q, b, xQ_L=None, xQ_R=None, xc=None, sense=None)
# m.addMCinstrs(A, x, sense, b)
# m.optimize()

# print(x.X)
# print('Obj: %g' % m.ObjVal)


OPT = optimize.linprog(-1*f, A_ub = H0, b_ub=h0, bounds=(None, 0), method='highs-ds') 
print(OPT.fun)
print(OPT.x)
print(OPT.success)

def daug(A, B):
    Am = np.shape(A)[0]
    An = np.shape(A)[1]
    Bm = np.shape(B)[0]
    Bn = np.shape(B)[1]
    C = np.zeros((Am+Bm, An+Bn))
    C[0:Am, 0:An]=A
    C[Am:Am+Bm, An:An+Bn]=B
    return C


a = np.array([[9, 2, 3], [1, 2, 3], [2,4,5]])
b = np.array([[2, 2, 3], [1, 2, 3], [5,8,9]])
d = np.array([[2, 2, 3], [2, 3, 4]])
e = np.array([[1], [4], [5]])
print("a")
print(a)
print("d")
print(d)
print(daug(d,e))
A = sp.eye(3)
F = e.dot(A)

print(5*e)