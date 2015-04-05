# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:43:53 2015

@author: lejoflores
"""
from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt
import sys

#=================================#
# 1. Define simulation conditions #
#=================================#

xl = 0.0     # Origin [m]
xr = 100.0   # Right-hand extent of domain [m]

ti = 0.0     # Initial time [s]
tf = 100.0   # Final time [s]
dx = 0.25     # Spatial step [m]

u  = 1.5    # Advection wind speed [m/s]

Pi = 50.0    # Initial number of seeds present in first 1 m

plot_tstep = 15.0 # Time interval between plots

Cmax = 0.95

#==================================#
# 2. Define time and space vectors #
#==================================#
# Back-calculate dt for a maximum Courant condition to ensure stability
dt = Cmax*dx/u

x = np.arange(xl,xr+dx,dx)
t = np.arange(ti,tf+dt,dt)

Nx = len(x)
Nt = len(t) 

# Compute Courant condition
C = u*(dt/dx)
print "Courant condition = %.3f" % C
if (C >= 1.0):
    print "Courant condition should be <= 1"    
    sys.exit(1)
    
#===========================================#
# 3. Specify initial and bounday conditions #
#===========================================#
P0 = np.zeros(Nx)
P0[0] = Pi
P0[1] = Pi

Pl = np.zeros(Nt)
Pl[0] = Pi

#=================================================#
# 4. Create containers to store simulation values #
#=================================================#
P = np.zeros((Nx,Nt))

#=================================================#
# 5. Run the time loop                            #
#=================================================#
for i in range(Nt):
    
    if (i==0):
        P[:,i] = P0
    else:
        Pprev    = P[:,i-1]

        Pnext    = np.zeros(Nx)
        Pnext[0] = Pl[i]
        Pnext[1:Nx] = Pprev[1:Nx] - u*(dt/dx)*(Pprev[1:Nx] - Pprev[0:(Nx-1)])

        P[:,i] = Pnext
        
    # Plot simulated seed count every mod(i,floor(plot_tstep/dt))==0 steps
    if (i==0) or (np.mod(float(i),np.floor(plot_tstep/dt)) == 0):
        fig1 = plt.figure(1)
        plt.plot(x,P[:,i],'b')

plt.xlabel('Distance [m]')
plt.ylabel('Seed numbers [#]')
plt.show()

#=================================================#
# 6. Make a 3-D surface plot
#=================================================#

T, X = np.meshgrid(t, x)
fig2 = plt.figure(2)
ax2 = fig2.gca(projection='3d')
ax2.plot_surface(X, T, P, rstride=1, cstride=1, cmap=cm.Spectral, linewidth=0)
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Distance [m]')
ax2.set_zlabel('Seed numbers [#]')
