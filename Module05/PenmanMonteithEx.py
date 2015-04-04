# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import *

def AirDensity(RH, Tc, P=101.2):
    Rd =  286.9  # Specific gas constant of dry air in J/(kg*K)    
    q  =  0.622*(RH*SatVapor(Tc))/P # Mixing ratio in kg/kg
    Tv = (Tc + 273.15)*(1.0 + 0.61*q) # Compute virtual temperature in K
    P  *= 1000.0 # Convert pressure from kPa to Pa (= Nm/m^3 = J/m^3)
    rho_a = P/(Rd*Tv) # Compute air density in kg/
    return rho_a
    
def PsychConst(P, cP=1.013, lambda_v=2.26e3):
    gamma = (cP*P/(0.622*lambda_v))
    return gamma
    
def SatVaporPress(Tc):
    eSat = 0.61*exp(17.27*Tc/(237.3 + Tc))
    return eSat

def SlopeSatVaporPress(Tc):
    delta = 4098.0*SatVaporPress(Tc)/(237.3 + Tc)**2
    return delta

def AeroReist(um, zm, z0, d, zmp=zm):
    k = 0.4
    r_a = 1.0/(k**2*um)*log((zm - d)/z0)*log((zmp-d)/(z0/10.0))
    return r_a

def SurfResist(g0, S, D, Tc, SM, SM0):
    g_c = Gee_C()
    g_R = Gee_R(S)
    g_D = Gee_D(D)
    g_T = Gee_T(Tc + 273.15)
    g_M = Gee_M(SM, SM0)
    g_s = g0*g_c*g_R*g_D*g_T*g_M
    r_s = 1.0/g_s
    return r_s
    
def Gee_c():
    g_c = 1.0
    return g_c
    
def Gee_R(S, K_R=200.0):
    g_R = (S*(1000.0 + K_R))/(1000.0*(S+K_R))
    return g_R
    
def Gee_D(D,K_D1=-0.307, K_D2=0.019):
    g_D = 1.0 + K_D1*D + K_D2*D**2
    return g_D
    
def Gee_T(TK, TL=273.0, TH=313.0, T0=293.0):
    alpha_T = (TH - T0)/(T0 - TL)
    g_T = ((TK - TL)*(TH - TK)**alpha_T)/((T0 - TL)*(TH - T0)**alpha_T)
    return g_T

def Gee_M(SM, SM0, K_M1, K_M2):
    g_SM = 1.0 - K_M1*exp(K_M2*(SM - SM0))
    return g_SM    
    
def PenmanMonteithPET(Tc, RH, Rn, S, SM, um, z0, d, g0, SM0, P=101.2, zm=2.0):
    cP    = 1.013 # Define specific heat of air in kJ/(kg*K)
    rho_a = AirDensity(RH, Tc, P)
    D     = (1.0 - RH)*SatVaporPress(Tc)
    delta = SlopeSatVaporPress(Tc)
    gamma = PsychConst(P)
    r_a   = AeroReist(um, zm, z0, d)
    r_s   = SurfResist(g0, S, D, Tc, SM, SM0)
    
    LE    = (delta*Rn + (rho_a*cP*D)/r_a)/(delta + gamma*(1.0 + r_s/r_a))
    
    return LE
    
    
    