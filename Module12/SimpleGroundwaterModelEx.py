# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:57:08 2015

@author: lejoflores


"""

from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt

ti = 0.0
tf = 300.0

xl = 0.0
xr = 2000.0

nx = 100
nt = 200

Ks  = 1500

hri = 8.0
hrf = 8.0
hli = 7.0
hlf = 3.0

plot_tstep = 60.0

x = np.linspace(xl,xr,nx)
t = np.linspace(ti,tf,nt)

deltax = x[1] - x[0]
deltat = t[1] - t[0]

"""
Create appropriate boundary conditions
"""
hr = hri*np.ones(nt)
hl = ((hlf - hli)/(tf - ti))*(t - ti) + hli

"""
Create appropriate initial conditions
"""
h0 = ((hri - hli)/(xr - xl))*(x - xl) + hli

"""
Build incidence matrix A
"""
alpha    = Ks*deltat/deltax**2
Delta2   = np.diagflat(-2.0*np.ones(nx)) + np.diagflat(np.ones(nx-1),-1) + np.diagflat(np.ones(nx-1),1)
I        = np.eye(nx)
A        = I - alpha*Delta2
A[0,0]   = 1.0
A[0,1]   = 0.0
A[-1,-1] = 1.0
A[-1,-2] = 0.0

"""
Create storage container for solution
"""
h = np.zeros((nx,nt))

for i in range(len(t)):
    if (i==0):
        h[:,i] = h0
    else:
        hinit = h[:,i-1]
        hinit[0] = hl[i-1]
        hinit[-1] = hr[i-1]
        hnext = np.dot(np.linalg.pinv(A), hinit)
        h[:,i] = hnext
    
    # Plot simulated pressure head every mod(i,floor(plot_tstep/dt))==0 steps
    if (i==0) or (np.mod(float(i),np.floor(plot_tstep/deltat)) == 0):
        fig1 = plt.figure(1)
        plt.plot(x,h[:,i],'b')
        

plt.xlabel('Distance [m]')
plt.ylabel('Pressure head [m]')
plt.show()

"""
Make a 3-D surface plot
"""    
T, X = np.meshgrid(t, x)
fig2 = plt.figure(2)
ax2 = fig2.gca(projection='3d')
ax2.plot_surface(T, X, h, cmap=cm.jet)
ax2.set_xlabel('Time [yr]')
ax2.set_ylabel('Distance [m]')
ax2.set_zlabel('Pressure head [m]')

