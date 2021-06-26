import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

l1 = 1.2
l2 = 1
m1 = 1
m2 = 2
g = 9.81

def phi(u, t):
    theta1, theta2, dtheta1, dtheta2 = u
    A = l1*np.cos(theta1 - theta2)
    B = l2
    C = l1*dtheta1**2*np.sin(theta1 - theta2)-g*np.sin(theta2)
    AA = (m1+m2)*l1
    BB = m2*l2*np.cos(theta1 - theta2)
    CC = m2*l2*dtheta2**2*np.sin(theta2 - theta1) - (m1+m2)*g*np.sin(theta1)
    d2theta1 = (C*BB - CC*B)/(A*BB - AA*B)
    d2theta2 = (A*CC - AA*C)/(A*BB - AA*B)
    return np.array([dtheta1, dtheta2, d2theta1, d2theta2])

theta1_0 =3
theta2_0 = 2
u0 = np.array([theta1_0, theta2_0, 0, 0])
t_max = 50
dt = 0.005
T = np.arange(0, t_max, dt)
U = odeint(phi, u0, T)
Theta1 = [u[0] for u in U]
Theta2 = [u[1] for u in U]

X1 = l1*np.sin(Theta1) 
X2 = X1 + l2*np.sin(Theta2)
Y1 = -l1*np.cos(Theta1) 
Y2 = Y1 - l2*np.cos(Theta2)

cadre = plt.figure()
d = (l1 + l2)*1.1
dessin = cadre.add_subplot(111, ylim = [-d, d], xlim = [-d, d])
#dessin.plot(X2, Y2)

ligne, = dessin.plot([], [], linestyle = "-", marker = "o", markerfacecolor="red")
texte = dessin.text(-0.95*d, 0.8*d, '')


def init():
    ligne.set_data([0, X1[0], X2[0]], [0, Y1[0], Y2[0]])
    texte.set_text('t = 0.00s')
    return ligne, texte


def animer(i):
    x = [0, X1[i], X2[i]]
    y = [0, Y1[i], Y2[i]]
    ligne.set_data(x, y)
    texte.set_text("t = {:.2f}s".format(i*dt))
    return ligne, texte

ani = animation.FuncAnimation(cadre, animer, range(1, len(U)),
                              interval=2, blit=True, init_func=init)


plt.show()
    