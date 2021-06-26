from scipy.integrate import quad
from math import *


def integrale(f, a, b, n = 1000):
    pas = (b-a)/n
    s = 0
    for k in range(n):
        ak = a + k*pas
        s = s + (f(ak) + f(ak+pas))/2
    return s*pas

def integrale1(f, a, b, n = 1000):
    pas = (b-a)/n
    s = (f(a) + f(b))/2
    for k in range(1, n):
        ak = a + k*pas
        s = s + f(ak)
    return s*pas

def integrale(f, a, b):
    I, e = quad(f, a, b)
    return I

def liste_a(f, N, T):
    omega = 2*pi/T
    A = [0]*(N+1)
    A[0] = integrale(f, -T/2, T/2)/T
    for n in range(1, N+1):
        def fn(t):
            return cos(n*omega*t)*f(t)
        A[n] = integrale(fn, -T/2, T/2)*2/T
    return A

def liste_b(f, N, T):
    omega = 2*pi/T
    B = [0]*(N+1)
    for n in range(1, N+1):
        def fn(t):
            return sin(n*omega*t)*f(t)
        B[n] = integrale(fn, -T/2, T/2)*2/T
    return B

def f(x):
    return abs(cos(x))

def liste_a(f, N, T):
    omega = 2*pi/T
    A = [0]*(N+1)
    A[0] = integrale(f, -T/2, T/2)/T
    def fcos(t, n):
        return cos(n*omega*t)*f(t)
    for n in range(1, N+1):
        A[n] = quad(fcos, -T/2, T/2, args = (n))[0]*2/T
    return A

def triangle(x):
    T = 2
    x1 = -1/2 + x/T
    return abs(x1)


































