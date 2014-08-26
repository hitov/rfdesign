#!/bin/python

#RF Circuit Design 2ed
#Small signal RF Amplifier design

#Design using S parameters

#Stability

from math import *
from numpy import conjugate

def pol2rec(magnitude, angle):
    return magnitude * cos(angle) + 1j * magnitude * sin(angle)

def deg2rad(deg):
    return deg * (pi/180)

def rollet_stability_factor(s11, s12, s21, s22):
    Ds = s11*s22 - s12*s21
    K = (1 + abs(Ds)**2 - abs(s11)**2 - abs(s22)**2) / (2 * abs(s21) * abs(s12))
    return K

def calc_mag(s11, s12, s21, s22):
    Ds = s11*s22 - s12*s21
    K = rollet_stability_factor(s11, s12, s21, s22)
    B1 = 1 + abs(s11)**2 - abs(s22)**2 - abs(Ds)**2
    MAG = 10*log10(abs(s21)/abs(s12)) + 10*log10(K + (-B1/abs(B1)) * sqrt(K**2 - 1))
    return MAG

def load_reflection(s11, s12, s21, s22):
    Ds = s11*s22 - s12*s21
    C2 = s22 - Ds * conjugate(s11)
    B2 = 1 + abs(s22)**2 - abs(s11)**2
    GamaL = ( B2 - (B2/abs(B2)) * sqrt(B2**2 - 4*(abs(C2)**2)) ) / (2 * abs(C2))
     
    

S11 = pol2rec(0.4, deg2rad(162))
S12 = pol2rec(0.04, deg2rad(60))
S21 = pol2rec(5.2, deg2rad(63))
S22 = pol2rec(0.35, deg2rad(-39))

print rollet_stability_factor(S11, S12, S21, S22)
print pol2rec(3, pi/2)
print calc_mag(S11, S12, S21, S22)

