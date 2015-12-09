# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:10:51 2015

@author: kawatson

Purpose: Download data from select SNOTEL sites for a given time period
         and save data to text files

Required libraries: Climata (available via PyPI | "pip install climata")
"""

# Import Climata
from climata.snotel import RegionDailyDataIO

# Download data for given specifications
sites = RegionDailyDataIO(
    start_date = "2012-10-01",
    end_date = "2013-09-30",
    state = "ID",
    county = "Boise",
    parameter = "WTEQ",
)

# Iterate over sites and write data to text files
for site in sites:
    f = open(site.stationtriplet.split(':')[0] + ".txt","w")
    print "Writing data to file for: " + site.name
    for row in site.data:
        f.write(str(row.date)+","+str(row.value)+"\n")
    f.close()