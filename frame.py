#author: Thomas Pfurtscheller
#created: 2020/03/06
#
#deformation frame overhead crane
import csv
import matplotlib.pyplot as plt
import parameter as param
import numpy as np
import control.matlab as ctrl

file = open("meas_deformation.csv", "r")
csv_reader = csv.reader(file, delimiter=",")

time = []
pos = []

for row in csv_reader:
   time.append(float(row[0]))
   pos.append(float(row[1]))

file.close()

#frame model without carriage
A = np.matrix([[-param.r1/param.mb, -param.k1/param.mb],[1.0, 0.0]])
b = np.array([[0.0], [0.0]])
c = np.array([0.0, 1.0])
d = 0.0

#settings
u = 0.0
x0 = np.array([0.0, 1.0e-3])
tSim = np.linspace(0.0, 50.0, len(pos))


SystemCrane = ctrl.ss(A, b, c, d)
tLsim, yLsim, xLsim = ctrl.lsim(SystemCrane, u, tSim, x0)


#plot of deformation
fig, ax = plt.subplots(2, 1, figsize=(16, 5), sharex=True)

lines = ax[0].plot(time, pos)
lines = ax[0].plot(yLsim, tLsim)

lines = ax[1].plot(time, np.absolute(tLsim-pos))

plt.ylabel('Position Frame in Meter')
plt.xlabel('Zeit in Sekunden')

ax[0].grid()
ax[1].grid()

plt.show()
