"""
author: Thomas Pfurtscheller
created: 2020/03/08

simulation of overhead crane
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import parameter as param

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False)
ax.set_yticklabels([])
# ax.grid()

ax.set_xlim([-0.4, 6.4])
ax.set_ylim([0, 3.3])

# set up empty lines to be updates later on
l1, = ax.plot([], [], 'b', lw=4)
rope, = ax.plot([], [], 'r', lw=2)
l3, = ax.plot([], [], 'k', lw=8)
l4, = ax.plot([], [], 'k', lw=3)
l5, = ax.plot([], [], 'k', lw=3)
load, = ax.plot([], [], 'o', markersize=20)
mass, = ax.plot([], [], 'r', lw=8)

time_text = ax.text(0.08, 0.02, '', transform=ax.transAxes)
x1_text = ax.text(0.08, 0.07, '', transform=ax.transAxes)
x2_text = ax.text(0.08, 0.12, '', transform=ax.transAxes)
phi_text = ax.text(0.08, 0.17, '', transform=ax.transAxes)
dx1_text = ax.text(0.5, 0.07, '', transform=ax.transAxes)
dx2_text = ax.text(0.5, 0.12, '', transform=ax.transAxes)
dphi_text = ax.text(0.5, 0.17, '', transform=ax.transAxes)
current_text = ax.text(0.08, 0.23, '', transform=ax.transAxes)



class simVisu:
    # visualization of the frame
    def sim(stateVector, timeVector):

        posBeam, posCarriage, anglePendulum, current = [], [], [], []
        velBeam, velCarriage, velPendulum = [], [], []
        for row in stateVector:
            velBeam.append(row[1])
            posBeam.append(row[0])
            velCarriage.append(row[3])
            posCarriage.append(row[2])
            velPendulum.append(row[5])
            anglePendulum.append(row[4])
            current.append(row[6])

        def frameInit():
            i, t = 0, 0
            while(i < param.n):
                yield i
                i += 1
            time_text.set_text('')
            return posBeam, posCarriage, anglePendulum

        def settings(i):
            t = param.dt*i
            time_text.set_text('Simulationszeit = %1.2lf s' % t)
            x1_text.set_text('Position x1 = %.1f mm' % (posBeam[i]*1000))
            x2_text.set_text('Position x2 = %.1f m' % posCarriage[i])
            phi_text.set_text('Winkel phi = %.lf °' % (anglePendulum[i]*180/np.pi))
            dx1_text.set_text('Geschwindigkeit dx1 = %.lf m/s' % velBeam[i])
            dx2_text.set_text('Geschwindigkeit dx2 = %.lf m/s' % velCarriage[i])
            dphi_text.set_text('Omega Pendel = %.lf rad/s' % velPendulum[i])
            current_text.set_text('Strom i = %.lf mA' % (current[i]*1000))


        def frame(i):
            x1 = posBeam[i]
            l3.set_data(np.array([-0.2 + x1, 6.2 + x1]), np.array([3.0, 3.0]))
            l4.set_data(np.array([0.0, x1]), np.array([0.0, 3.0]))
            l5.set_data(np.array([6.0, 6.0 + x1]), np.array([0.0, 3.0]))


        def carrieage(i):
            x2 = posCarriage[i]
            hight = 0.25
            length = 0.8
            l1.set_data(np.array([-length/2, length/2, length/2, -length/2, -length/2]) + x2,
                        np.array([3.0, 3.0, 3.0 - hight, 3.0 - hight, 3.0]))

        def pendulum(i):
            x2 = posCarriage[i]
            phi = anglePendulum[i]
            hight = 0.25
            rope.set_data(np.array([x2, x2 + (param.l-param.radius)*np.sin(phi)]), np.array([3.0, 3.0 - (param.l-param.radius)*np.cos(phi)]) - hight)
            #load.set_data(x2 + param.l*np.sin(phi), 3.0 - param.l*np.cos(phi) - hight)

            x = np.linspace(0,2 * np.pi, 101)
            a = np.array([x2 + param.l*np.sin(phi) + np.cos(x)*param.radius])
            b = np.array([3.0 - param.l*np.cos(phi) - hight + np.sin(x)*param.radius])
            mass.set_data(a, b)

        frameAni = animation.FuncAnimation(fig, frame, frameInit, interval=10)
        pendulumAni = animation.FuncAnimation(fig, pendulum, frameInit, interval=10)
        carriageAni = animation.FuncAnimation(fig, carrieage, frameInit, interval=10)
        settingsAni = animation.FuncAnimation(fig, settings, frameInit, interval=10)
        plt.show()