from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np

def f(x, a):
    return a**x - x**2 -2

def Newton(f, f_prime, a, epsilon):
    x = a
    ecart = 1 + epsilon
    while ecart >= epsilon :
        x_old = x
        x = x - f(x) / f_prime (x)
        ecart = abs(x - x_old)
    return x

def suite_Newton(f, f_prime, a, n):
    X = [0]*(n+1)
    X[0] = a
    for k in range(n):
        X[k+1] = X[k] - f(X[k]) / f_prime(X[k])
    return X

def P(x):
    return x**4 + x**3 - 23*x**2 + 3*x + 90

def dP(x):
    return 3 + x*(-46 + x*(3 + x*4))

# X0 = [-12, -10, -8, -6, -4, -2, -1, 0, 2, 4, 6]
# for x0 in X0:
#     X = suite_Newton(P, dP, x0, 10)
#     plt.plot(X)
# plt.show()

X = np.linspace(-3.4646, -3.4632, 100000)
Y = [Newton(P, dP, x0, 1e-8) for x0 in X]

plt.plot(X, Y)
plt.show()










