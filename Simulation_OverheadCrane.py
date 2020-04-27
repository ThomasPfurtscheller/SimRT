"""
author: Thomas Pfurscheller
created: 2020/03/05

main file for the simulation of project overhead crane
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import control.matlab as ctrl
import parameter as param
import animation as anim
import model as model

# settings
# initial state vector x = [z dz b db phi dphi i]^T
x0 = [0.0, 0.0, 0.0, 0.0, np.pi/4, 0.0, 0.0]  # initial state

tSim = np.linspace(param.tStart, param.tEnd, param.n)

# statespace model
c1 = (param.mW+2*param.mL)*param.l
A = [[-param.r1/param.mb, -param.k1/param.mb, 0, 0, 0, 0, 2*param.Kt/param.Dw],
              [1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, param.r2/c1, -param.mL*param.g/(param.mW+2*param.mL), -2*param.Kt/(param.Dw*(param.mW+2*param.mL))],
              [0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, -param.r2*(param.mW+param.mL)/(param.l*param.mL*c1), param.g*(param.mW+param.mL)/c1, 2*param.Kt/(param.Dw*c1)],
              [0, 0, 0, 0, 0, 1, 0],
              [2*param.Kt/(param.Dw*param.L), 0, -2*param.Kt/(param.Dw*param.L), 0, 0, 0, -param.R/param.L]]

b = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [1 / param.L]]
c = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
d = [[0.0]]

#u = np.zeros(n)

#SystemCrane = ctrl.ss(A, b, c, d)
#tLsim, yLsim, xLsim = ctrl.lsim(SystemCrane, u, tSim, x0)


#input trajectory
ue = np.zeros(100)
ue = np.concatenate([ue, np.full(100, 30)])
ue = np.concatenate([ue, np.zeros(100)])
ue = np.concatenate([ue, np.full(100, -30)])
ue = np.concatenate([ue, np.zeros(601)])

#ue = np.zeros(n)
ue = 30

# solver
if param.simNonLinear == 1:
    xOde = odeint(model.overheadCrane.nonLinearModel3, x0, tSim, args=(ue, param))
if param.simLinear == 1:
    xOde = odeint(model.overheadCrane.linearModel, x0, tSim, args=(ue, param))

# plot result
#fig, ax = plt.subplots(2, 1, figsize=(16, 5), sharex=True)
#lines = ax[0].plot(tSim, xOde)
#lines = ax[1].plot(tSim, ue)
#lines[0].set_label('test')

#ax[0].grid()
#ax[1].grid()
#plt.show()

anim.simVisu.sim(stateVector=xOde, timeVector=tSim)