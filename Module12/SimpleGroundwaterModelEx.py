# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:57:08 2015

@author: lejoflores


"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt

ti = 0.0
tf = 300.0

xl = 0.0
xr = 2000.0

nx = 100
nt = 200

Ks  = 3000

hri = 8.0
hrf = 8.0
hli = 7.0
hlf = 3.0

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
    
    # Plot simulated pressure head

"""
Make a 3-D surface plot
"""    
T, X = np.meshgrid(t, x)
fig = plt.figure(2)
ax = fig.gca(projection='3d')
ax.plot_surface(T, X, h, cmap=cm.jet)


