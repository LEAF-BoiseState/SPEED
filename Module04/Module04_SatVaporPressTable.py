# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:22:13 2015

@author: lejoflores

PURPOSE: The purpose of this Python script is to demonstrate the use of a while 
         loop by creating ordered pairs of air temperature in degrees C and 
         the corresponding value of saturation vapor pressure in kPa.

         The code makes use of the Clausius-Clapeyron equation, equation 2.17 
         from "Terrestrial Hydrometeorology" by Jim Shuttleworth.
"""

from math import exp

Tc  = -15.0 # Initial temperature
dTc = 0.5  # Air temperature increment

while Tc <= 45.0:
    esat = 0.6108*exp(17.27*Tc/(237.3 + Tc))
    print "Tc = %.2f deg. C, esat = %.3f kPa" % (Tc,esat)
    Tc += dTc
    
