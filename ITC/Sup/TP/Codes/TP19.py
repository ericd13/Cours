from math import *
from scipy.integrate import quad
import matplotlib.pyplot as plt

def integrale(f, a, b):
    n = 1000
    pas = (b-a)/n
    somme = (f(a) + f(b))/2
    for k in range(1, n-1):
        ak = a + k*pas
        somme = somme + f(ak)
    return somme*pas

def integrale(f, a, b):
    I, e = quad(f, a, b)
    return I


def liste_a(f, N, T):
    A = [0]*(N+1)
    A[0] =  integrale(f, -T/2, T/2)/T
    omega = 2*pi/T
    for n in range(1, N+1):
        def fn(x):
            return f(x)*cos(omega*n*x)
        A[n] = 2*integrale(fn, -T/2, T/2)/T
    return A

def liste_b(f, N, T):
    B = [0]*(N+1)
    omega = 2*pi/T
    for n in range(1, N+1):
        def fn(x):
            return f(x)*sin(omega*n*x)
        B[n] = 2*integrale(fn, -T/2, T/2)/T
    return B

def somme_Fourier(A, B, T, x):
    N = len(A)
    s = 0
    w = 2*pi/T
    for n in range(N):
        s = s + A[n]*cos(n*w*x) + B[n]*sin(n*w*x)
    return s

def somme_Fejer(A, B, T, x):
    N = len(A)
    s = 0
    w = 2*pi/T
    for n in range(N):
        s = s + (A[n]*cos(n*w*x) + B[n]*sin(n*w*x))*(1-n/N)
    return s

def triangle(x):
    k = floor((x+1)/2)
    return abs(x-2*k)

a = -1
b = 3
n = 1000
pas  = (b-a)/n
X = [a + k*pas for k in range(n+1)]
Y = [triangle(x) for x in X]
plt.plot(X, Y)

A = liste_a(triangle, 20, 2)
B = liste_b(triangle, 20, 2)

for N in [1, 2, 3, 5, 20]:
    Y = [somme_Fourier(A[ : N+1], B[ : N+1], 2, x) for x in X]
    plt.plot(X, Y, label="Somme d'ordre {}".format(N))
plt.legend()
plt.show()

def rectangle(x):
    k = floor((x+1)/2)
    if x - 2*k > 0:
        return 1
    else:
        return -1

a = -1
b = 3
n = 1000
pas  = (b-a)/n
X = [a + k*pas for k in range(n+1)]
Y = [rectangle(x) for x in X]
plt.plot(X, Y)

A = liste_a(rectangle, 50, 2)
B = liste_b(rectangle, 50, 2)

for N in [1, 5, 10, 20, 50]:
    Y = [somme_Fourier(A[ : N+1], B[ : N+1], 2, x) for x in X]
    plt.plot(X, Y, label="Somme d'ordre {}".format(N))
plt.legend()
plt.show()

for N in [1, 5, 10, 20, 50]:
    Y = [somme_Fejer(A[ : N+1], B[ : N+1], 2, x) for x in X]
    plt.plot(X, Y, label="Somme d'ordre {}".format(N))
plt.legend()
plt.show()

