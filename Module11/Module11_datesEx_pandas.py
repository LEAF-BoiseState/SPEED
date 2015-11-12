# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 2015

@author: kawatson

Purpose: Demonstrate how to import time series data from a text file and 
         plot that data using pandas

"""

# Import required modules
import pandas as pd

# Specify name of text file (assumed to be in the same directory as the script)
filename = 'SNOTEL.csv'

# Import data from file
df = pd.read_csv(filename,parse_dates=[0],index_col=0)

# Create the plot
df.plot()
