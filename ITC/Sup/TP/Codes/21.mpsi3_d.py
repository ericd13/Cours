import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def Euler(phi, y0, T):
    n = len(T)
    Y = [0]*n
    Y[0] = y0
    for k in range (n -1) : 
        pas = T[k+1] - T[k]
        pente = phi (Y[k], T[k])
        Y [k+1] = Y[k] + pas*pente 
    return Y


# Question 1

def phi1(y, t):
    return y + t

def sol(t):
    return np.exp(t)*0.5 - t - 1

# Question 2
# for n in [3, 6, 10, 20, 50, 100, 1000, 10000]:
#     y0 = -0.5
#     T = np.linspace(0, 3, n)
#     Y = Euler(phi1, y0, T)
#     plt.plot(T, Y, label = "Euler avec {} points".format(n))
# 
# T1 = np.linspace(0, 3, 10000)
# Y1 = sol(T1)
# plt.plot(T1, Y1, linestyle = "dashed", label = "Solution exacte")
# 
# plt.legend()
# plt.show()

# Question 3
def creneau(t, per):
    x = t%per
    if x < per/2:
        return 1
    else:
        return -1
    
creneau1 = np.vectorize(creneau)
    
R2 = 1000
R3 = 1000
C = 1.0e-7
f = 500
per = 1/f

T = np.linspace(0, 0.02, 1000)
Ue = creneau1(T, per)

# Question 4
for R1 in [100, 200, 500, 1000, 2000]:
    def phi4(y, t):
        return ((R2 + R3)/R2*creneau(t, per) - y)/(R1*C)
    y0 =0
    Us = Euler(phi4, y0, T)
    plt.plot(T, Us, label = "Tension de sortie pour R1 = {}".format(R1))

plt.plot(T, Ue, label = "Tension d'entrée")
plt.legend()
plt.show()








    