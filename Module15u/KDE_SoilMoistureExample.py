# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:16:26 2015

@author: lejoflores
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

#================================================#
# 1. Read in the data
#================================================#
def ExtractSoiMoiData(SM_filename):

    SM2 = []
    SM8 = []
    SM20 = []

    infile = open(SM_filename, 'r') # Open the file
    for line in infile:
        words = line.split(',')
        SM2.append(float(words[3]))
        SM8.append(float(words[4]))
        SM20.append(float(words[5]))
    infile.close()
    SM2 = np.asarray(SM2)
    SM8 = np.asarray(SM8)
    SM20 = np.asarray(SM20)
    return SM2, SM8, SM20

SM_filename = 'BogusBasin_SM_WY2011.csv' # This is the name of the file to be read
(SM2, SM8, SM20) = ExtractSoiMoiData(SM_filename)

SM_plot = np.linspace(-5.0, 35.0, 1000)
bins = np.linspace(-5.0, 35.0, 10)

bw = bins[1] - bins[0]

fig, ax = plt.subplots(2,2)

# Histogram 1
ax[0, 0].hist(SM2, bins=bins, fc='#AAAAFF', normed=True)
ax[0, 0].text(-2.5, 0.14, "Histogram")
ax[0, 0].set_xlim(-5, 40)
ax[0, 0].set_ylim(0.0, 0.16)
ax[0, 0].set_ylabel('Normalized density')

# Histogram 1
ax[0, 1].hist(SM2, bins=bins+2.5, fc='#AAAAFF', normed=True)
ax[0, 1].text(-2.5, 0.14, "Histogram, bins shifted")
ax[0, 1].set_xlim(-5, 40)
ax[0, 1].set_ylim(0.0, 0.16)

# Tophat KDE
kde = KernelDensity(kernel='tophat', bandwidth=2.0).fit(SM2[:, np.newaxis])
log_dens = kde.score_samples(SM_plot[:, np.newaxis])
ax[1, 0].fill(SM_plot, np.exp(log_dens), fc='#AAAAFF')
ax[1, 0].text(-2.5, 0.14, "Tophat Kernel Density")
ax[1, 0].set_xlim(-5, 40)
ax[1, 0].set_ylim(0.0, 0.16)
ax[1, 0].set_xlabel('Soil moisture [%]')
ax[1, 0].set_ylabel('Normalized density')

# Gaussian KDE
kde = KernelDensity(kernel='gaussian', bandwidth=2.0).fit(SM2[:, np.newaxis])
log_dens = kde.score_samples(SM_plot[:, np.newaxis])
ax[1, 1].fill(SM_plot, np.exp(log_dens), fc='#AAAAFF')
ax[1, 1].text(-2.5, 0.14, "Gaussian Kernel Density")
ax[1, 1].set_xlim(-5, 40)
ax[1, 1].set_ylim(0.0, 0.16)
ax[1, 1].set_xlabel('Soil moisture [%]')

