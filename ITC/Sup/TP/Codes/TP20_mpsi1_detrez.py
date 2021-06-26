from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

def f(x, a, b):
    return a**x - x**2 - b

def Newton(f, f_prime, a, epsilon):
    x = a
    ecart = 1 + epsilon
    while ecart >= epsilon :
        x_old = x
        x = x - f(x)/f_prime(x)
        ecart = abs(x - x_old)
    return x

def suite_Newton(f, f_prime, a, n):
    out = [0]*(n+1)
    out[0] = a
    for k in range(n):
        x = out[k]
        out[k+1] = x - f(x)/f_prime(x)
    return out

def P(x):
    return x**4 + x**3 - 23*x**2 + 3*x + 90

def dP(x):
    # méthode de Hörner
    return 3 + x*(-46 + x*(3 + x*4))

# X0 = [-10, -8, -6, -4, -2, 0, 2, 4, 6]
# n = 10
# for x0 in X0:
#     X = suite_Newton(P, dP, x0, n)
#     plt.plot(X)
# plt.show()

X0 = np.linspace(-3.47, -3.46, 100000)
Y = [Newton(P, dP, x0, 0.0001) for x0 in X0]

plt.plot(X0, Y)
plt.show()
