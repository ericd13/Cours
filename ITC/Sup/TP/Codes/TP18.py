from math import *
import matplotlib.pyplot as plt
from time import time

def rect_g(f, a, b, n):
    pas = (b-a)/n
    s = 0
    for k in range(n):
        c = a + k*pas
        s = s + f(c)
    return s*pas

def point_m(f, a, b, n):
    pas = (b-a)/n
    s = 0
    for k in range(n):
        c = a + (k + 1/2)*pas
        s = s + f(c)
    return s*pas

def f1(t):
    return 4/(1+t**2)

# for p in range(1, 8):
#     n = 10**p
#     e1 = abs(rect_g(f1, 0, 1, n) - pi)
#     e2 = abs(point_m(f1, 0, 1, n) - pi)
#     print("Pour n = {}, l'erreur est : ".format(n))
#     print("  {:7.1e} pour rect_g, {:7.1e} pour point_m".format(e1, e2))
# 
# t0 = time()
# taille = 100
# pas = 5000
# N  = [0]*taille
# err_g = [0]*taille
# err_m = [0]*taille
# for i in range(taille):
#     N[i] = (i+1)*pas
#     err_g[i] = abs(pi - rect_g(f1, 0, 1, N[i]))
#     err_m[i] = abs(pi - point_m(f1, 0, 1, N[i]))
# t1 = time()
# print(t1 - t0)
#     
# plt.subplot(1, 2, 1)
# plt.plot(N, err_g, label = "Rectangles")
# plt.plot(N, err_m, label = "Point milieu")
# plt.legend()
# 
# plt.subplot(1, 2, 2)
# plt.xscale('log')
# plt.yscale('log')
# plt.plot(N, err_g, label = "Rectangles")
# plt.plot(N, err_m, label = "Point milieu")
# plt.legend()
# 
# plt.show()
# 
# n = len(N)
# K_g = [0]*n
# K_m = [0]*n
# for i in range(n):
#     K_g[i] = err_g[i]*N[i]
#     K_m[i] = err_m[i]*N[i]**2
#     
# plt.plot(N, K_g, label = "Rectangles")
# plt.plot(N, K_m, label = "point milieu")
# plt.legend()
# plt.show()

N1 = 1001
T = [0]*N1
F1 = [0]*N1
for k in range(N1):
    T[k] = k/(N1 - 1)
    F1[k] = f1(T[k])
    
plt.plot(T, F1)
plt.show()

def integrale_rg(T, Y):
    s = 0
    n = len(T)
    pas = T[1] - T[0]
    for k in range(n-1):
        s = s + Y[k]
    return s*pas

print(abs(pi - integrale_rg(T, F1)))

def integrale_pm(T, Y):
    s = 0
    n = len(T)
    pas = T[2] - T[0]
    for k in range(1, n, 2):
        s = s + Y[k]
    return s*pas

print(abs(pi - integrale_pm(T, F1)))


def integrale_tr(T, Y):
    s = (Y[-1] - Y[0])/2
    n = len(T)
    pas = T[1] - T[0]
    for k in range(n-1):
        s = s + Y[k]
    return s*pas

print(abs(pi - integrale_tr(T, F1)))


