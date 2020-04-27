"""
author: Thomas Pfurtscheller
created: 2020/03/05

parameter of overhead crane
"""
import numpy as np

#general settings for simulation
simLinear = 0
simNonLinear = 1
noiseOn = 0

tStart = 0
tEnd = 20
n = 1001
dt = (tEnd - tStart) / (n-1)



# parameter
D_frame = 0.246423666678943
omega0_frame = 10.209622266104212
D_pendel = 0.064397827961716
omega0_pendel = 2.196112454498204

M1 = 98.32                               # kg
M2 = 3                                   # kg
M3 = 10                                  # kg
d = 11.5        # kg/s ... Dämpfung am Pendellager
#r = 2 * D_frame * omega0_frame                # kg/s ... Dämpfung des Rahmens
r = 475.486
k = np.power(omega0_frame,2) * M1              # kg/s^2 ... Steifigkeit des Rahmens
L = 49.6e-3                              # H
R = 34.63                                # Ohm
Kt = 0.73                                # Nm/A ... Drehmomentkonstante
Dw = 39.79e-3                            # m ... Wirkdurchmesser
l = 2000e-3                               # m
g = 9.81                                 # m/s^2 ... Erdbeschleunigung
iMax = 3.7                              # Ampere
viscoseFriction = 50                    # Ns/m
Ke = 43.98          # Spannungskonstante

#paramter frame
T = 0.6254
omega0_frame = 2*np.pi / T

#new parameter for own model
mb = 98.32                               # kg
mW = 3
mL = 10
r1 = 475
k1 = np.power(omega0_frame,2) * mb       # kg/s^2 ... Steifigkeit des Rahmens
r2 = 11.5                                  # kg/s ... Dämpfung am Pendellager

#visu geometry
radius = 0.075
