import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

g = 9.81
l = 0.5 
t_fin = 10 # temps final pour l'étude
N  = 100000  # nombre de points
T = np.linspace(0, t_fin, N)

def psi(y, v, t):
    return -g/l*np.sin(y)

def Euler(phi, y0, T):
    n = len(T)           
    Y = [0]*n 
    Y[0] = y0 
    for i in range(n-1): 
        pas = T[i+1] - T[i]
        Y[i+1] = Y[i] + pas*phi(Y[i], T[i])
    return Y

def Euler2(psi, y0, v0, T):
    n = len(T)           
    Y = [0]*n 
    Y[0] = y0 
    V = [0]*n 
    V[0] = v0 
    for i in range(n-1): 
        pas = T[i+1] - T[i]
        Y[i+1] = Y[i] + pas*V[i]
        V[i+1] = V[i] + pas*psi(Y[i], V[i], T[i])
    return Y, V

y0 = np.pi/2
v0 = 0
Y, V = Euler2(psi, y0, v0, T)

plt.plot(T, Y, label = "Angle")
plt.plot(T, V, linestyle = "dashed", label = "Vitesse")
plt.legend()
plt.show()

def psi1(y, v, t):
    return -g/l*y
Y0 = [0.3,  0.9,  1.5]
v0 = 0
for y0 in Y0:
    Y, V = Euler2(psi, y0, v0, T)
    plt.plot(T, Y)
    Y1, V1 = Euler2(psi1, y0, v0, T)
    plt.plot(T, Y1)
plt.legend(loc = "lower right")
plt.show()

Y0 = [0.5, 1.0, 1.5, 2.0, 2.5]
v0 = 0
for y0 in Y0:
    Y, V = Euler2(psi, y0, v0, T)
    plt.plot(Y, V, label = "Angle initial = {}".format(y0))
plt.legend()
plt.show()

a  = 12.0e-2
b  =  3.0e-2
c  =  5.0e-2
kF =  7.8
kG  = 2.0

def phi(u, t):
    x, y = u
    dx = kF*(a - x - y)*(b - x)
    dy = kG*(a - x - y)*(c - y)
    return np.array([dx, dy])

T = np.linspace(0, 60, 10000)
u0 = np.array([0, 0])
U = Euler(phi, u0, T)

X = [u[0] for u in U]
Y = [u[1] for u in U]
plt.plot(T, X, label = "Fructose")
plt.plot(T, Y, label = "Glucose")
plt.legend()
plt.show()

def phi(u,t):
    y, v = u
    a = -g/l*np.sin(y)
    return np.array([v, a])
    
T = np.linspace(0, 20, 200)
u0 = np.array([np.pi/6, 0])
U = Euler(phi, u0, T)
Y = [u[0] for u in U]
plt.plot(T, Y, label = "Euler")
U = odeint(phi, u0, T)
Y = [u[0] for u in U]
plt.plot(T, Y, label = "odeint")
plt.legend()
plt.show()

