import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def Euler(phi, y0, T):
    n = len(T)
    Y = [0]*n
    Y[0] = y0
    for k in range(n-1):
        Y[k+1] = Y[k] + (T[k+1] - T[k])*phi(Y[k], T[k])
    return Y

def phi(y, t):
    return y + t

def sol(t):
    return np.exp(t)*0.5 - t - 1

y0 = -0.5

# for n  in [3, 6, 10, 20, 50, 100, 1000, 10000, 100000]:
#     T = np.linspace(0, 3, n)
#     Y = odeint(phi, y0, T)
#     plt.plot(T, Y)
# 
# T0 = np.linspace(0, 3, 10000)
# Y0 = sol(T0)
# plt.plot(T0, Y0, linestyle = "dashed")
# plt.show()

# Partie 2.1
k = 100
def phi2(y, t):
    return -k*y

def solution6(y0, T):
    n = len(T)
    Y = [0]*n
    Y[0] = y0
    for  k in range(n-1):
        Y[k+1] = Y[k]/(1 + k*(T[k+1] - T[k]))
    return Y

y0 = 1
for n in [500]:
    T = np.linspace(0, 10, n)
    Y = Euler(phi2, y0, T)
    plt.plot(T, Y, label = "explicite, {} points".format(n))
    Y1 = solution6(y0, T)
    plt.plot(T, Y1, label = "implicite, {} points".format(n))

plt.plot(T, np.exp(-20*T), label = "exacte")
plt.legend()
plt.show()











