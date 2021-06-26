from math import *
from scipy.integrate import quad
import matplotlib.pyplot as plt

def integrale(f, a, b):
    I, e = quad(f, a, b)
    return I

def liste_a(f, N, T):
    A = [0]*(N+1)
    omega = 2*pi/T
    for n in range (N + 1):
        def fn(x):
            return f(x)*cos(omega*n*x)
        I = integrale(fn, -T/2, T/2)
        if n > 0:
            A[n] = I*2/T
        else:
            A[n] = I/T
    return A

def liste_b(f, N, T):
    B = [0]*(N+1)
    omega = 2*pi/T
    for n in range (N + 1):
        def fn(x):
            return f(x)*sin(omega*n*x)
        I = integrale(fn, -T/2, T/2)
        B[n] = I*2/T
    return B

def somme_fourier(A, B, T, x):
    omega = 2*pi/T
#    assert(len(A) == len(B))
    N = len(A)
    y = A[0]
    for n in range(1, N):
        u = n*omega*x
        y = y + A[n]*cos(u) + B[n]*sin(u)
    return y
    
def triangle(t):
    T = 2
    u = 1/2 + t/T
    K = floor(u)
    return abs(t - K*T)

n = 1000
a = -2.5
b = 4.5
h = (b-a)/n
X = [a + k*h for k in range(n)]

Y = [triangle(t) for t in X]

plt.plot(X, Y)
plt.show()










