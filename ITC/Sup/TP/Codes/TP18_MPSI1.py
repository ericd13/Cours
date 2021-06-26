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
        c = a + k*pas + pas/2
        s = s + f(c)
    return s*pas

def f1(t):
    return 4/(1+t**2)

# for p in [1, 2, 3, 4, 5, 6, 7]:
#     n = 10**p
#     err = abs(rect_g(f1, 0, 1, n) - pi)
#     print("L'erreur pour {} points est {}".format(n, err))

# for p in [1, 2, 3, 4, 5, 6, 7]:
#     n = 10**p
#     err = abs(point_m(f1, 0, 1, n) - pi)
#     print("L'erreur pour {} points est {}".format(n, err))

N = list(range(5000, 500001, 5000))
err_g = [abs(rect_g(f1, 0, 1, n) - pi) for n in N]
err_m = [abs(point_m(f1, 0, 1, n) - pi) for n in N]

plt.yscale("log")
plt.plot(N, err_g, label = "Rectangles")
plt.plot(N, err_m, label = "Point_milieu")
plt.xscale('log')
plt.legend()
plt.show()

