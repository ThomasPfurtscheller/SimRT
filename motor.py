"""
author: Thomas Pfurtscheller
created: 2020/03/12

parameter identification of motor
"""
import csv
import matplotlib.pyplot as plt
import parameter as param
import numpy as np
import control.matlab as ctrl

file = open("meas_deformation.csv", "r")
csv_reader = csv.reader(file, delimiter=",")

time, meas = [], []

for row in csv_reader:
   time.append(float(row[0]))
   meas.append(float(row[1]))

file.close()

#plot
fig, ax = plt.subplots(2, 1, figsize=(16, 5), sharex=True)

lines = ax[0].plot(time, meas)


plt.ylabel('y')
plt.xlabel('Zeit in Sekunden')

ax[0].grid()

plt.show()
















