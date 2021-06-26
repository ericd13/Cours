from scipy.integrate import quad
import numpy as np
import math as m
import matplotlib.pyplot as plt

def f(x):
    return abs(m.sin(x))

def integrale(f, a, b):
    I, e = quad(f, a, b)
    return I

def liste_a(f, N, T):
    omega = 2*m.pi/T
    A = [0]*(N+1)
    A[0] = integrale(f, -T/2, T/2)/T
    for n in range(1, N+1):
        def fn(t):
            return f(t)*m.cos(n*omega*t)
        A[n] = integrale(fn, -T/2, T/2)*2/T
    return A

def liste_b(f, N, T):
    omega = 2*m.pi/T
    B = [0]*(N+1)
    for n in range(1, N+1):
        def fn(t):
            return f(t)*m.sin(n*omega*t)
        B[n] = integrale(fn, -T/2, T/2)*2/T
    return B

A = liste_a(f, 5, 2*m.pi)
B = liste_b(f, 5, 2*m.pi)

def somme_Fourier(A, B, T, x):
    s = 0
    w = 2*m.pi/T
    p = len(A)
    for n in range(p):
        s = s + A[n]*m.cos(n*w*x) + B[n]*m.sin(n*w*x)
    return s

X = [-4 + k/100 for k in range(1000)]

Y = [f(x) for x in X]
Yf = [somme_Fourier(A, B, 2*m.pi, x) for x in X]

plt.plot(X, Y)
plt.plot(X, Yf)
plt.show()