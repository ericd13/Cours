import matplotlib.pyplot as plt

def Newton (f ,f_prime ,a , epsilon):
    x = a
    ecart = 1 + epsilon
    while ecart >= epsilon:
        x_old = x
        x = x - f(x)/f_prime(x)
        ecart = abs(x - x_old)
    return x

def suite_Newton (f ,f_prime ,a , n):
    x = a
    out = [0]*(n+1)
    out[0] = a
    for i in range(n):
        x = x - f(x)/f_prime(x)
        out[i+1] = x
    return out

def P(x):
    return x**4 + x**3 - 23*x**2 + 3*x + 90

def dP(x):
    return 3 + x*(-46 + x*(3 + x*4))

def suite(a, b, n):
    pas = (b-a)/(n-1)
    out = [0]*n
    for i in range(n):
        out[i] = a  + i*pas
    return out

X = suite(-4, 6, 1000)

Y = [P(x) for x in X]
Z = [0 for x in X]

# plt.plot(X, Y)
# plt.plot(X, Z)
# plt.show()
# 
# X0 = [-10, -8, -6, -4, -2, 0, 2, 4]
# for x0 in X0:
#     N = suite_Newton(P, dP, x0, 10)
#     plt.plot(N)
# plt.show()

# X = suite(-6, 4, 100000)
# 
# n = len(X)
# Y = [0]*n
# for i in range(n):
#     Y[i] = Newton(P, dP, X[i], 1e-5)
#     
# 
# Y1 = [0]*n
# for x in X:
#     Y1[i] = Newton(P, dP, x, 1e-5)
#     
# Y2 = [Newton(P, dP, x, 1e-5) for x in X]
# 
# plt.plot(X, Y)
# plt.show()
















