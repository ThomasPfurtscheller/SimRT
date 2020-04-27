"""

author: Thomas Pfurscheller
created: 2020/03/26

explicit euler method for solving differential equations
"""
import numpy as np


class expliciteEuler():
    # solve differntial equations with the explicit euler method
    def __init__(self, increment):
        self.h = increment

    def solve(fun, timeVector, x0):
        # fun ... differential equation first order f(t)
        # timeVector ... vector of simulation time

        h = timeVector[1] - timeVector[0]       # calculation time increment from timeVector
        x = [[0 for i in range(len(x0))] for j in range(len(timeVector))]       # initialize matrix
        x[0] = x0

        for k in range(0,len(timeVector)-1):
            x[k+1] = x[k] + h * fun(x[k])


        y = []
        for row in x:
            y.append(row[1])

        return np.array([timeVector, y])


class heunMethod():
    # solve difential equations with heun method
    def __init__(self,increment):
        self.h = increment


    def solve(fun, timeVector, x0):
        return

