#author: Thomas Pfurtscheller
#created: 2020/03/07
#
#damping of pendel
import csv
import matplotlib.pyplot as plt
import parameter as param
import numpy as np
import control.matlab as ctrl
from scipy.integrate import odeint

file = open("meas_pendel.csv", "r")
csv_reader = csv.reader(file, delimiter=",")

time = []
angel = []

for row in csv_reader:
   time.append(float(row[0]))
   angel.append(float(row[1]))

file.close()

#linear model pendel
A = np.matrix([[-param.r2/(np.power(param.l,2)*param.mL), -param.g/param.l],[1.0, 0.0]])
b = np.array([[0.0], [0.0]])
c = np.array([0.0, 1.0])
d = 0.0

#not linear model pendel
def nonLinearPendel(x, t, u, param):

   x1, x2 = x

   dx1 = -param.d/(np.power(param.l,2)*param.mL) * x1 - np.sin(x2)*param.g/param.l
   dx2 = x1

   return np.array([dx1, dx2])


#settings
u = 0.0
x0 = np.array([0.0, 0.0314])
tSim = np.linspace(0.0, 50.0, len(angel))


# solver
xOde = odeint(nonLinearPendel, x0, tSim, args=(u, param))

SystemPendel = ctrl.ss(A, b, c, d)
tLsim, yLsim, xLsim = ctrl.lsim(SystemPendel, u, tSim, x0)


alpha = []
for row in xOde:
   alpha.append(row[1])


#plot of deformation
fig, ax = plt.subplots(3, 1, figsize=(16, 5), sharex=True)

lines = ax[0].plot(time, angel)
lines = ax[0].plot(yLsim, tLsim)
lines = ax[0].plot(time, alpha)

lines = ax[1].plot(time, np.absolute(tLsim-angel))
lines = ax[2].plot(time, np.absolute(tLsim-alpha))

plt.ylabel('Winkel in Grad')
plt.xlabel('Zeit in Sekunden')

ax[0].grid()
ax[1].grid()
ax[2].grid()

plt.show()
