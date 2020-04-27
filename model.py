"""
author: Thomas Pfurscheller
created: 2020/03/27

implementation of non linear and linear model overhead crane
__________________________________________
    x :     state vector
    t :     time
    u :     input
    param:  parameter for model
__________________________________________
"""
import numpy as np

class overheadCrane():
    # not linear model overhead crane
    def nonLinearModel(x, t, u, param):
        x1, x2, x3, x4, x5, x6, x7 = x
        c1 = param.Dw * np.power(param.l, 2) * param.mL * (np.power(np.cos(x6), 2) * param.mL - param.mL - param.mW)

        dx1 = -param.r1 / param.mb * x1 - param.k1 / param.mb * x2 + 2 * param.Kt * x7 / (param.Dw * param.mb)
        dx2 = x1
        dx3 = (-param.Dw * (np.sin(x6) * param.l * param.g * param.mL + param.r2 * x5) * np.cos(x6) - np.sin(
            x6) * np.power(x5, 2) * np.power(param.l, 2) * param.mL * param.Dw + 2 * param.Kt * param.l * x7) / (
                          param.l * param.Dw * (np.power(np.cos(x6), 2) * param.mL - param.mL - param.mW))
        dx4 = x3
        dx5 = ((np.sin(x6) * np.power(param.l, 2) * param.Dw * np.power(param.mL, 2) * np.power(x5,
                                                                                                2) - 2 * param.Kt * param.l * param.mL * x7) * np.cos(
            x6) + param.Dw * (param.mW + param.mL) * (np.sin(x6) * param.l * param.g * param.mL + param.r2 * x5)) / c1
        dx6 = x5
        dx7 = -param.R * x7 / param.L - 2 * param.Kt * (x3 - x1) / (param.Dw * param.L) + u / param.L

        return np.array([dx1, dx2, dx3, dx4, dx5, dx6, dx7])

    # not linear model overhead crane, EOM with Lagrange old version
    def nonLinearModel3(x, t, u, param):
        x1, x2, x3, x4, x5, x6, x7 = x

        fric = np.sign(x3-x1)*param.viscoseFriction*(x3-x1)

        Q = np.matrix([[1, 0, 0, 0, 0, 0, 0],
                       [0, param.M1, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, param.M2+param.M3, 0, param.M3*param.l*np.cos(x5), 0],
                       [0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, param.M3*param.l*np.cos(x5), 0, param.M3*np.power(param.l, 2), 0],
                       [0, 0, 0, 0, 0, 0, param.L]])

        Qinv = np.linalg.inv(Q)

        R = np.matrix([[0, 1, 0, 0, 0, 0, 0],
                       [-param.k, -param.r, 0, 0, 0, 0, -2*param.Kt/param.Dw + fric],
                       [0, 0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 2*param.Kt/param.Dw + fric],
                       [0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, -param.d, 0],
                       [0, 2*param.Kt/param.Dw, 0, -2*param.Kt/param.Dw, 0, 0, -param.R]])

        s = np.array([0, 0, 0, param.M3*param.l*np.sin(x5)*np.power(x6, 2), 0, param.M3*param.l*np.sin(x5)*x6*x4 - param.M3*param.l*np.sin(x5)*param.g, u])

        v = Qinv * R
        dx = v.dot(x) + Qinv.dot(s)

        return np.array([dx[0, 0], dx[0, 1], dx[0, 2], dx[0, 3], dx[0, 4], dx[0, 5], dx[0, 6]])


    # linear model overhead crane
    def linearModel(x, t, u, param):
        x1, x2, x3, x4, x5, x6, x7 = x

        c1 = param.l * param.mL - param.l * (param.mW + param.mL)

        dx1 = -param.r1 / param.mb * x1 - param.k1 / param.mb * x2 + 2 * param.Kt * x7 / (param.Dw * param.mb)
        dx2 = x1
        dx3 = param.r2 * x5 / (param.l * param.mW) - param.mL * param.g * x6 / param.mW - 2 * param.Kt * x7 / (
                    param.Dw * param.mW)
        dx4 = x3
        dx5 = param.r2 * (param.mW + param.mL) * x5 / (param.l * param.mL * c1) - param.g * (
                    param.mW + param.mL) * x6 / c1 - 2 * param.Kt * x7 / (param.Dw * c1)
        dx6 = x5
        dx7 = -param.R * x7 / param.L + -2 * param.Kt * (x3 - x1) / (param.Dw * param.L) + u / param.L

        return np.array([dx1, dx2, dx3, dx4, dx5, dx6, dx7])