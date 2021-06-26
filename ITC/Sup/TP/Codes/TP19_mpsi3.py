from math import *
from scipy.integrate import quad
import matplotlib.pyplot as plt

def integrale(f, a, b):
    I, e  = quad(f, a, b)
    return I

def liste_a(f, N, T):
    A = [0]*(N+1)
    omega = 2*pi/T
    for n in range(N+1):
        def fn(t):
            return f(t)*cos(n*omega*t)
        I = integrale(fn, -T/2, T/2)
        if n == 0:
            A[0] = I/T
        else:
            A[n] = I*2/T
    return A

def liste_b(f, N, T):
    B = [0]*(N+1)
    omega = 2*pi/T
    for n in range(N+1):
        def fn(t):
            return f(t)*sin(n*omega*t)
        I = integrale(fn, -T/2, T/2)
        B[n] = I*2/T
    return B

def somme_fourier(A, B, T, x):
    N = len(A)
    assert(N == len(B))
    y = A[0]
    omega = 2*pi/T
    for n in range(1, N):
        t = n*omega*x
        y = y + A[n]*cos(t) + B[n]*sin(t)
    return y

def triangle(t):
    u = 1/2 - t/2
    k = floor(u)
    return abs(t + 2*k)

X = [-1+k/100 for k in range(400)]
Y = [triangle(t) for t in X]
plt.plot(X, Y)
plt.show()

