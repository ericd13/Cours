from math import *
import matplotlib.pyplot as plt

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

taille = 100
pas = 5000
N  = [0]*taille
err_g = [0]*taille
err_m = [0]*taille
for i in range(taille):
    N[i] = (i+1)*pas
    err_g[i] = abs(pi - rect_g(f1, 0, 1, N[i]))
    err_m[i] = abs(pi - point_m(f1, 0, 1, N[i]))
    
plt.subplot(1, 2, 1)
plt.plot(N, err_g, label = "Rectangles")
plt.plot(N, err_m, label = "Point milieu")
plt.legend()

plt.subplot(1, 2, 2)
plt.xscale('log')
plt.yscale('log')
plt.plot(N, err_g, label = "Rectangles")
plt.plot(N, err_m, label = "Point milieu")
plt.legend()

plt.show()

X = [k/1000 for k in range(1001)]
Y = [f1(x) for x in X]

n = len(Y)

pi1 = 0
for i in range(n-1):
    pi1 = pi1 + Y[i]
pi1 = pi1*(X[1] - X[0])
print(pi -pi1)

pi2 = Y[0]/2 + Y[n-1]/2
for i in range(1, n-1):
    pi2 = pi2 + Y[i]
pi2 = pi2*(X[1] - X[0])
print(pi-pi2)

pi3 = 0
for i in range(1, n, 2):
    pi3 = pi3 + Y[i]
pi3 = pi3*(X[2] - X[0])
print(pi-pi3)


