import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def Euler(phi, y0, T):
    n = len(T)
    Y = [0]*n
    Y[0] = y0
    for k in range (n -1) : 
        pas = T[k+1] - T[k]
        pente = phi (Y[k], T [k])
        Y [k+1] = Y[k] + pas*pente 
    return Y

# Question 1
def phi1(y, t):
    return y + t

def f(t):
    return 0.5*np.exp(t) - t - 1

# Question 02
# y0 = -0.5
# 
# for n in [3, 6, 10, 20, 40, 100, 1000]:
#     T = np.linspace(0, 3, n)
#     Y = Euler(phi1, y0, T)
#     plt.plot(T, Y, label = "Euler avec {} points".format(n))
# 
# n1 = 10000
# T1 = np.linspace(0, 3, n1)
# Y1 = f(T1)
# plt.plot(T1, Y1, linestyle = "dashed", label = "Solution exacte")
# 
# plt.legend()
# plt.show()


# Question 3

def creneau(t, T):
    x = t%T
    if x < T/2:
        return 1
    else:
        return -1
    
creneau1 = np.vectorize(creneau)
    
# Question 4

f = 500
per = 1/f
R2 = 1000
R3 = 1000
C = 1e-6

T = np.linspace(0, 0.02, 1000)
S = creneau1(T, per)
plt.plot(T, S, label = "Signal d'entrée")

res = [100, 200, 500, 1000, 2000]
for R1 in res:
    def phi4(y, t):
        return ((R2 + R3)/R2*creneau(t, per) - y)/(R1*C)
    Y = Euler(phi4, 0, T)
    plt.plot(T, Y, label = "Sortie pour R1 = {} ohms".format(R1))

plt.legend()
plt.show()

