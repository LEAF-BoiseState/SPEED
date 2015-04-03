# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:07:45 2015

@author: lejoflores

Purpose: The purpose of this code is to take an evapotranspiration rate given 
         as a mass flux in units of kg/(m^2*s) and convert it to an evapo-
         transpiration rate in unites of equivalent depth per day (mm/day)

"""

ET_mf  = 3.0e-5 # Given or input evapotranspiration mass flux rate in kg/(m^2*s)
rho    = 1000.0 # Assumed density of liquid water (kg/m^3)
m2mm   = 1000.0 # Conversion to mm from m
s2hr   = 3600.0 # Conversion from seconds to hours
hr2day = 24.0   # Conversion from hours to days

ET_dd = ET_mf*(1.0/rho)*m2mm*s2hr*hr2day

print "For ET = %.6f kg/(m^2*s), I get ET = %.6f mm/day"  % (ET_mf, ET_dd)
