from operator import matmul
import os
from xml.dom.minidom import Identified
import numpy as np
import control as ct
from termset import *

#a function for easier debug and matlab comp
def deb(A):
    print(A)
    print("dimention:")
    print(A.shape)

MODEL = 1

def daug(A, B):
    dimM = np.shape(A)[0]
    dimN = np.shape(A)[1]
    ABdaug = np.zeros((dimM*2, dimN*2))
    ABdaug[0:dimM, 0:dimN] = A
    ABdaug[dimM:dimM*2, dimN:dimN*2] = B
    return ABdaug



if (MODEL == 1):
    A = np.array([[1, 1], [0, 1]])
    B = np.array([[1], [0.3]])
    C = np.identity(2)

    nx = 2
    ny = 2
    nu = 1
    n = 10

    qy = np.identity(2) 
    Q = (C.transpose()).dot(qy).dot(C)
    R = 1

    umin = -1
    umax = 1
    ymin = -5*np.array([[1], [1]])
    ymax = 5*np.array([[1], [1]])

    sys = ct.ss(A,B,C,0,1)


K, S, E = ct.lqr(sys, Q, R) #stusser litt på at E ikke er identisk med matlab, men tror ikke det er av betydning


#Qh = daug(np.kron(np.identity(n-1), Q), S)
#print("Qh")

#print(Qh)
#Rh = np.kron(np.identity(n), R)


Hy = np.kron(np.identity(n-1),C)
hy = np.kron(np.ones(( n-1, 1)), ymax) 

F=np.kron(np.identity(n-1), -1*C)
Hy = np.concatenate((Hy,F))
hy = np.concatenate((hy, np.kron(np.ones((n-1,1)),-1*ymin)))

Hh, hn = termset(A,B,C,K,ymax,ymin,umax,umin)

# #prover å implementere linje 110 på mandag
# W = np.array([[1, 2, 3], [3, 4, 5],  [3, 4, 5]])
# V = np.array([[5, 6, 1], [7, 8, 1],  [3, 4, 5]])
#     # T = np.array([[9, 1], [2, 3]])
# print(-1*W)
   




