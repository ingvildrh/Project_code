from re import U
import numpy as np
from MPC_setup import * 
import math as math

tend = 100

if (MODEL == 1):
    xinit = np.matrix([[5], [-2]])
    xinit = np.matrix([[-6], [1.1]])

x0 = xinit

xsave = np.zeros((nx, tend+1))
usave = np.zeros((nu, tend))
zsave = np.zeros((nu, tend))
tosave = np.zeros((1, tend))
feasflag = 1

xsave[:,0:1]= xinit

f = np.zeros((n*nu, 1))

nc = np.shape(Gz)[0]
Hinv = np.linalg.inv(Hess)
IGi = np.subtract(np.identity(nc), (Gz.dot(Hinv)).dot(np.transpose(Gz)))
IGIs = (IGi) #not able to make this sparse yet
hif = Hinv@f0 

HGz = -Hinv@np.transpose(Gz)
HGzu = HGz[1:nu, :]
hifu = -hif[1:nu, :]

actsets = np.zeros((nc,1))
Qsp0 = np.identity(nc)


for i in range(tend):
    feasflag = False

    actset = actsets
    solved = False
    izold = 0
    ix = 0

    Qmat0i = Qsp0y0 = np.subtract(-Sz@x0, Wz)
    y0 = np.subtract(-Sz.dot(x0), Wz)
    while (not (solved)):

        ix = ix +1
        
        if (ix == 1): 
            y = y0
        else:
            y = y0-y0[iz]@vAd
            y0 = y
        
        lam = np.multiply(y,actset) #elementvis?
        i1 = min(lam)
        i1z = np.argmin(lam)

        if (i1>=-10*np.finfo(float).eps):
            i1 = []

        if (not i1):
            iz = i1z
            actset[iz] = 0 
            qc = 1
        else:
            i2 = max(y-lam)
            i2z = np.argmax(y-lam)
            if (not i2):
                iz = i2z
                actset[iz] = 1
                qc = -1
            else:
                iz = []
        
        if (not iz):
            qu = IGIs[:, iz]
            vA = np.multiply(Qmat0i,qu)
            qdiv = qc+vA[iz] #her er problemet :)
            vAd = (1/qdiv)@vA

            if ((abs(qdiv) < 1*math.e**(-13)) or (abs(qdiv) > 1*math.e**(12))):

                feasflag = 0
                print("Infeasible påroblem detected")

                feasflag = False

                break

            Qmat1i = np.subtract(Qmat0i, -vAd@Qmat0i[iz,:])
            Qmat0i = Qmat1i

        else:
            solved = True
            feasflag = True
        
    if (feasflag == 0):
        break
    
    lam = actset*y #element wise?

    u = HGzu@lam+hifu@x0

    x1 = A@x0+B@U

    x0 = x1
    xsave[:, ik+1] = x0
    usave[:, ik] = U
    tosave[1, ik] = tk 




