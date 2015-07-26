# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 13:58:04 2015

@author: lejoflores
"""

# Import important libraries
import numpy as np
import matplotlib.pyplot as plt
import math as m

Ntime = 10 # Number of time steps to run (years)
Ring = 5 # Number of rings of cells to evaluate neighborhood

# Set Transition probabilities
P_WU_lonely  = 0.00
P_WU_crowded = 0.06
f_UrbanCrit  = 0.25
k_logistic   = 10.0


# Let's assume once a wild pixel is converted to urban, there's no going back. Thus, 
# the transition probability of urban to wild (P_UW) is zero

# Load the initial city map
CityMap = np.load('InitialCity.npy')
CityMapInit = np.copy(CityMap) #Clone the initial condition. We'll be over-writing CityMap

dims = np.shape(CityMap)
Nrows = dims[0]
Ncols = dims[1]

for i in xrange(0,Ntime):
    
    CityMapUpdated = np.copy(CityMap)    
    
    for j in xrange(0,Nrows):
        
        for k in xrange(0,Ncols):
            
            if(CityMap[j,k] == 0.0): # Only need to consider wild pixels
                
                # Get the starting and ending row and column numbers N=Ring pixels 
                # in the each direction of the pixel in question (the neighborhood)
                StartRow = np.max((j-Ring-1,0))
                EndRow   = np.min((j+Ring+1,Nrows-1))
                StartCol = np.max((k-Ring-1,0))
                EndCol   = np.min((k+Ring+1,Ncols-1))
                
                # Get the 1s and 0s of the surrounding neighborhood
                HoodMap = CityMap[StartRow:EndRow,StartCol:EndCol]

                # Get the fraction of urbanized pixels in the neighborhood
                dimsHoodMap = np.shape(HoodMap)
                NHoodPix = float(dimsHoodMap[0]*dimsHoodMap[1])
                NHoodUrb = np.sum(HoodMap)
                
                f_Urban = NHoodUrb/NHoodPix
                
                # Get the urbanization weighted transition probability
                # Transform neighborhood fraction to 
                g_Urban = np.tan((f_Urban - 0.5)*m.pi)
                g_UrbanCrit = np.tan((f_UrbanCrit - 0.5)*m.pi)
                
                P_WU = P_WU_crowded / (1 + np.exp(-k_logistic*(g_Urban - g_UrbanCrit))) + P_WU_lonely
                
                if(np.random.uniform() < P_WU): # Transition if true
                    CityMapUpdated[j,k] = 1.0 # Now urbanized
                    
    print "Completed time step " + format(i) + ". " + format(float(i+1)/float(Ntime)*100.0) + "% complete"
    CityMap = np.copy(CityMapUpdated)
    
# Make some plots
plt.figure(1)
plt.subplot(221)
plt.imshow(CityMapInit,cmap='gray')
plt.title("Initial condition")
plt.axis('off')

plt.subplot(222)
plt.imshow(CityMap,cmap='gray')
plt.title("Final condition")
plt.axis('off')

plt.subplot(223)
plt.imshow(CityMap+CityMapInit,cmap='bwr')
plt.title("Change")
plt.axis('off')

# Save a figure
#OutFileName = "SimpleUrbanSTM_Ring" + format(Ring) + "_fcrit%0.2f.png" % f_UrbanCrit
#plt.savefig(OutFileName,dpi=300)


