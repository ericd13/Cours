import math as m
import matplotlib.pyplot as plt
import numpy as np

def muller_b_c(n):
#     u = Fraction(5, 2)
#     v = Fraction(17, 5)
    u = 5/2
    v = 17/5
    for i in range(n):
        w = 30 - 129/v + 100/u/v
        u = v
        v = w
    den = ((v - 29)*u + 100)/72
    num4 = -((v - 26)*u + 25)/63
    num25 = ((v - 5)*u + 4)/504
    beta = num4/4**n/den
    gamma = num25/25**n/den
    return float(u), float(beta), float(gamma)

def muller(n):
    u = 11/2
    v = 61/11
    for i in range(n):
        w = 111 - 1130/v + 3000/u/v
        u = v
        v = w
    return u

from fractions import Fraction

def muller_frac(n):
    u = Fraction(11, 2)
    v = Fraction(61, 11)
    for i in range(n):
        w = 111 - 1130/v + 3000/u/v
        u = v
        v = w
    return float(u)

def coef(c0, c1, c2, u, v):
    den = (c0 - c1)*(c0 - c2)
    C2 = 1/ den
    C1 = (-c1 - c2)/den
    C0 = c1*c2/den
    return C2*u*v + C1*u + C0

def muller_general(n, a = 5, b = 6, c = 100, u0 = None, u1 = None, i = 0):
    if u0 == None:
        u0 = (a + b)/2
    if u1 == None:
        u1 = (a**2 + b**2)/(a + b)
    A = a + b + c
    B = a*b + a*c + b*c
    C = a*b*c
    M = [0]*(n+1)
    M[0] = u0
    M[1] = u1
    for k in range(2, n+1):
        M[k] = A - B/M[k-1] + C/M[k-1]/M[k-2]
    plt.subplot(2, 1, 1)
    plt.plot(M)
    plt.title("Suite $(a_n)$")
    alpha = coef(a, b, c, M[i], M[i+1])/a**i*2
    beta  = coef(b, a, c, M[i], M[i+1])/b**i*2
    gamma = coef(c, a, b, M[i], M[i+1])/c**i*2
    print(alpha, beta, gamma, i)
#     P = [0]*(n+1)
#     for k in range(n+1):
#         P[k] = M[k] - (alpha*a**(k+1) + beta*b**(k+1) + gamma*c**(k+1))/(alpha*a**k + beta*b**k + gamma*c**k)
#     plt.subplot(2, 1, 2)
#     plt.plot(P)
#     plt.title("Valeurs de $a_n-u_n$, coefficients calculés en $a_{}$ et $a_{}$".format(i, i+1))
    plt.show()
    
def kahan(n, u0 = None, u1 = None, i = 0):
    a = 4
    b = 36
    c = 42
    if u0 == None:
        u0 = (a + b)/2
    if u1 == None:
        u1 = (a**2 + b**2)/(a + b)
    A = a + b + c
    B = a*b + a*c + b*c
    C = a*b*c
    M = [0]*(n+1)
    M32 = np.zeros(n+1, dtype = 'f4')
    M[0] = u0
    M[1] = u1
    for k in range(2, n+1):
        M[k] = A - B/M[k-1] + C/M[k-1]/M[k-2]
    plt.plot(M, label = "64 bits")
    M32[0] = u0
    M32[1] = u1
    for k in range(2, n+1):
        M32[k] = A - B/M32[k-1] + C/M32[k-1]/M32[k-2]
    plt.plot(M32, label = "32 bits")
    plt.ylim([0, 60])
    plt.legend()
    plt.title("Suite de Rump")
    plt.show()
    alpha = coef(a, b, c, M[i], M[i+1])/a**i*2
    beta  = coef(b, a, c, M[i], M[i+1])/b**i*2
    gamma = coef(c, a, b, M[i], M[i+1])/c**i*2
    print(gamma/beta, i, M[222:224])
    

def muller3(n):
    c = -3.75e-18
    u = 5/2
    v = 17/5
    for i in range(n):
        w = 30 - 129/v + 100/u/v
        u = v
        v = w
    normal = (1+4**(n+1))/(1+4**n)
    erreur = (1+4**(n+1)+c*25**(n+1))/(1+4**n+c*25**n)
    return u, normal, erreur-u
   
    
    



    