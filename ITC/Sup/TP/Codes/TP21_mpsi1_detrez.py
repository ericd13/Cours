import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def Euler(phi, y0, T):
    n = len(T)
    Y = [0]*n
    Y[0] = y0
    for k in range(n-1):
        Y[k+1] = Y[k] + (T[k+1] - T[k])*phi(Y[k], T[k])
    return Y

# "Partie 1.1"
# 
# def phi1(y, t):
#     return y + t
# 
# def sol(t):
#     return np.exp(t)/2 - t - 1
# 
# y0 = -0.5
# 
# for n in [3, 6, 10, 20, 40, 100, 1000, 10000]:
#     T = np.linspace(0, 3, n)
#     Y = Euler(phi1, y0, T)
#     plt.plot(T, Y, label = "Euler avec {} points".format(n))
# 
# 
# 
# T0 = np.linspace(0, 3, 10000)
# Y0 = sol(T0)
# plt.plot(T0, Y0, linestyle = "dashed", label = "Solution exacte")
# 
# plt.legend()
# plt.show()
    
"Partie 1.2"

def creneau(t, per):
    x = t%per
    if x < per/2:
        return 1
    else:
        return -1
    
cren = np.vectorize(creneau)

f = 500
per = 1/f
R2 = 1000
R3 = 1000
C = 1.0e-6

N = 1000
t_max = 0.02
T = np.linspace(0, t_max, N)
for R1 in [50, 100, 200, 500, 1000, 2000, 5000]:
    def phi2(y, t):
        return ((R2 + R3)/R3*creneau(t, per) - y)/(R1*C)
    y0 = 0
    Y = Euler(phi2, y0, T)
    plt.plot(T, Y)

Y0 = cren(T, per)
plt.plot(T, Y0)
plt.show()



        
