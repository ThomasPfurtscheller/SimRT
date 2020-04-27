# author: Thomas Pfurscheller
# created: 2020/03/26
#
# test of solver class
import numpy as np
import solver as solve
import matplotlib.pyplot as plt

r = 100
k = 1000
m = 10
x0 = np.array([0.0, 1.0])


def fun(x):
    x1 = x[0]
    x2 = x[1]

    # system of differential equations first order
    dx1 = -r/m*x1 - k/m*x2
    dx2 = x1

    return np.array([dx1, dx2])


timeVector = np.linspace(0,10,1001)

# solver
[t,x] = solve.expliciteEuler.solve(fun,timeVector,x0)



#plot
fig, ax = plt.subplots(2, 1, figsize=(16, 5), sharex=True)

lines = ax[0].plot(t,x)
lines = ax[1].plot(t,x)


plt.ylabel('y')
plt.xlabel('Zeit in Sekunden')

ax[0].grid()
ax[1].grid()

plt.show()












