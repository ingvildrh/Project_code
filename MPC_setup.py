import numpy as np
from control import *
from termset import *
from daug import * 

#a function for easier debug and matlab comp
def deb(A):
    print(A)
    print("dimention:")
    print(A.shape)

MODEL = 1



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

    sys = ss(A,B,C,0,1)


K, S, E = lqr(sys, Q, R) #stusser litt på at E ikke er identisk med matlab, men tror ikke det er av betydning


Qh = daug(np.kron(np.identity(n-1), Q), S)

Rh = np.kron(np.identity(n), R)


Hy = np.kron(np.identity(n-1),C)
hy = np.kron(np.ones(( n-1, 1)), ymax) 

F=np.kron(np.identity(n-1), -1*C)
Hy = np.concatenate((Hy,F))
hy = np.concatenate((hy, np.kron(np.ones((n-1,1)),-1*ymin)))

#Hh, hn = termset(A,B,C,K,ymax,ymin,umax,umin)
#Dette er en hardkodet work-around som leser fra txt.fil generert i matlab og flyttet 
#manuelt til rett mappe
Hn = np.genfromtxt('A.txt')
hn = (np.genfromtxt('B.txt'))
hn = np.transpose(np.matrix(hn))

Hy = daug(Hy, Hn)

hy = np.concatenate((hy, hn))

#umax constraints
Hu = np.identity(n*nu)
hu = np.kron(np.ones((n,1)),umax)
#umin constraints
Hu = np.concatenate((Hu, -1*np.eye(n*nu)))
hu = np.concatenate((hu, np.kron(np.ones((n,1)), -1*umin)))

#above: specified the model and the constraints, now comes the solution to
#the problem

v = np.ones((n-1, 1))
Ia = np.subtract(np.identity(n*nx), np.kron(np.diagflat(v, -1), A))
Iai = np.linalg.inv(Ia)
Bh = np.kron(np.identity(n), B)


A0 = np.kron(np.concatenate((np.array([[1]]), np.zeros((n-1, 1)))),A)

Gy = (Hy.dot(Iai)).dot(Bh) #must wait due to Hy was not made with daug

Ssy = -1*(Hy.dot(Iai)).dot(A0) #must wait, same reason as before
Wy = hy

Gu = Hu
Ssu = np.zeros((np.shape(hu)[0],nx))
Wu = hu

G = np.concatenate((Gy, Gu))
Ss = np.concatenate((Ssy, Ssu))
W = np.concatenate((Wy, Wu))

Bhi = Iai@Bh
A0i = Iai@A0

Hess = np.transpose(Bhi)@Qh@Bhi+Rh #Qh not made due to daug problems
f0 = np.transpose(Bhi)@Qh@A0i

Wz = W
Gz = G
Sz = Ss+(G.dot(np.linalg.inv(Hess)).dot(f0)) 

#Assembling for use of upper and lower bounds on u by MOSEK quadprog.
high = hu[1:n*nu]
low = -hu[n*nu+1:2*n*nu]
#For mskqpopt (not very successful)
nyc = np.shape(hy)[0]
blc = np.ones((nyc,1))*(-np.Inf) #elementvis???
 
#git test



















