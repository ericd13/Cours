import matplotlib.pyplot as plt
from numpy import polyfit


def Newton(f, f_prime, x0, eps):
    x = x0
    ecart = 1 + eps
    while ecart >= eps:
        x_old = x
        x = x - f(x)/f_prime(x)
        ecart = abs(x - x_old)
    return x

def suite_Newton(f, f_prime, x0, n):
    x = x0
    out = [0]*(n+1)
    out[0] = x0
    for i in range(n):
        x = x - f(x)/f_prime(x)
        out[i+1] = x
    return out

def P(x):
    return x**4 + x**3 -23*x**2 + 3*x +90

def dP(x):
    return 3 + x*(-46 + x*(3 + x*4))


# X0 = [-10, -8, -6, -4, -2, 0, 2, 4]
# N = 10
# for x0 in X0:
#     Y = suite_Newton(P, dP, x0, N)
#     plt.plot(Y)
# plt.show()

def suite(a, b, n):
    out = [0]*n
    h = (b-a)/(n-1)
    for i  in range(n):
        out[i] = a + i*h
    return out
N = 100000
a = -5
b = 2
eps = 1e-8

X = suite(a, b, N)

Y = [0]*N
for i in range(N):
    x0 = X[i]
    y = Newton(P, dP, x0, eps)
    Y[i] = y
    
Y1 = [Newton(P, dP, x0, eps) for x0 in X]

plt.plot(X, Y)
plt.show()
    
    
    
