import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import quad
from scipy.optimize import fsolve

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
#     
# "Partie 1.2"
# 
# def creneau(t, per):
#     x = t%per
#     if x < per/2:
#         return 1
#     else:
#         return -1
#     
# cren = np.vectorize(creneau)
# 
# f = 500
# per = 1/f
# R2 = 1000
# R3 = 1000
# C = 1.0e-6
# 
# N = 1000
# t_max = 0.02
# T = np.linspace(0, t_max, N)
# for R1 in [50, 100, 200, 500, 1000, 2000, 5000]:
#     def phi2(y, t):
#         return ((R2 + R3)/R3*creneau(t, per) - y)/(R1*C)
#     y0 = 0
#     Y = Euler(phi2, y0, T)
#     plt.plot(T, Y)
# 
# Y0 = cren(T, per)
# plt.plot(T, Y0)
# plt.show()
# 
# 
# "Partie 2.1"
# 
# 
# def phi3(y, t):
#     return -20*y
# 
# # for n in [100, 101, 102]:
# #     T = np.linspace(0, 10, n)
# #     y0 = 1
# #     Y = Euler(phi3, y0, T)
# #     plt.plot(T, Y)
# # plt.show()
#     
# def implicite3(y0, T):
#     n = len(T)
#     Y = [0]*n
#     Y[0] = y0
#     for k in range(n-1):
#         Y[k+1] = Y[k]/(1+ 20*(T[k+1] - T[k]))
#     return Y
#     
# for n in [100, 101, 102]:
#     T = np.linspace(0, 10, n)
#     y0 = 1
#     Y = implicite3(y0, T)
#     plt.plot(T, Y)
# plt.show()
    

def Heun(phi, y0, T):
    n = len(T)
    Y = [0]*n
    Y[0] = y0
    for k in range(n-1):
        pas = T[k+1] - T[k]
        pente1 = phi(Y[k], T[k])
        z = Y[k] + pas*pente1
        pente2 = phi(z, T[k+1])
        pente = (pente1 + pente2)/2
        Y[k+1] = Y[k] + pas*pente
    return Y
    
def phi4(y, t):
    return y - 2*np.exp(-t)
# 
# y0 = 1
# 
# T = np.linspace(0, 30, 1000000)
# 
# Y_e = Euler(phi4, y0, T)
# Y_h = Heun(phi4, y0, T)
# Y_o = odeint(phi4, y0, T)
# 
# Sol = np.exp(-T) # = [np.exp(-t) for t in T]
# 
# plt.plot(T, Y_e, label = "Euler")
# plt.plot(T, Y_h, label = "Heun")
# plt.plot(T, Y_o, label = "odeint")
# 
# plt.plot(T, Sol, label = "Solution exacte")
# plt.legend()
# plt.ylim([-10, 10])
# plt.show()

    
    
    
    
    
    
    
    
    
    
        
