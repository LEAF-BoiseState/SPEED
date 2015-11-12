# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 2015

@author: kawatson

Purpose: Demonstrate how to import time series data from a text file and 
         how to plot that data

"""


# Import required modules
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO

# Specify name of text file (assumed to be in the same directory as the script)
filename = 'SNOTEL.csv'

# Import data to using a converter to import the date/time information
Date, SWE = np.genfromtxt(filename, delimiter=',', skip_header=1, \
    converters={0:mdates.datestr2num}, unpack=True)

# Create and format the plot
fig, ax = plt.subplots()
ax.plot_date(Date, SWE,'k.')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=MO))
ax.xaxis.set_minor_locator(mdates.DayLocator())
plt.ylabel('SWE (in)')
plt.title('SNOTEL Site: Banner Summit')
plt.show()
