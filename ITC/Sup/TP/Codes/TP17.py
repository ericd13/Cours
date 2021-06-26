import numpy as np
import matplotlib.pyplot as plt
import random as rd
from math import exp, pi

def moyenne(liste):
    n = len(liste)
    s = 0
    for x in liste:
        s = s + x
    return s/n

def ecart_type(liste):
    n = len(liste)
    m = moyenne(liste)
    s = 0
    for x in liste:
        s = s + (x-m)**2
    return (s/n)**0.5

def maximum(liste):
    maxi = liste[0]
    for x in liste:
        if x > maxi:
            maxi = x
    return maxi

def minimum(liste):
    mini = liste[0]
    for x in liste:
        if x < mini:
            mini = x
    return mini

def comptage(liste, n):
    mini = minimum(liste)
    maxi = maximum(liste)
    h = (maxi - mini)/n
    histo = [0]*n
    for x  in liste:
        k = int((x-mini)/h)
        if k == n:
            k = n - 1
        histo[k] += 1
    return histo, h, mini

L0 = [4.3, 5.1, 7.8, 5.4, 4.4, 7.3, 6.8, 6.7, 5.9, 7.1]


def histogramme(liste, n):
    valeurs, h, mini = comptage(liste, n)
    centres = [0]*n
    for i in range(n):
        centres[i] = mini + (i+1/2)*h
    plt.bar(centres, valeurs, width = h)
    plt.show()

def liste_alea(x0, e, n):
    out = [0]*n
    for i in range(n):
        x = x0 + (2*rd.random() - 1)*e
        out[i] = x
    return out

# A = liste_alea(12.5, 0.05, 10000)
# B = liste_alea(8.3, 0.05, 10000)
# X = [A[i] + B[i] for i in range(len(A))]
# histogramme(X, 20)
# 
# A = liste_alea(12.5, 0.05, 10000)
# B = liste_alea(8.32, 0.005, 10000)
# X = [A[i] + B[i] for i in range(len(A))]
# histogramme(X, 20)
# 
# A = liste_alea(12.5, 0.05, 10000)
# B = liste_alea(8.3, 0.05, 10000)
# C = liste_alea(4.7, 0.05, 10000)
# D = liste_alea(13.4, 0.05, 10000)
# X = [(A[i] + B[i])/(C[i]+D[i]) for i in range(len(A))]
# histogramme(X, 20)

N = 100000
N1 = 100
A = [0]*N1
for i in range(N1):
    A[i] = liste_alea(12.5, 0.05, N)

M = [0]*N
for k in range(N):
    s = 0
    for i in range(N1):
        s = s + A[i][k]
    M[k] = s/N1

def gauss(x, m, s):
    return exp(-(x-m)**2/2/s**2)/s/(2*pi)**0.5

def histogramme_gauss(liste, n):
    valeurs, h, mini = comptage(liste, n)
    centres = [0]*n
    for i in range(n):
        centres[i] = mini + (i+1/2)*h
    plt.bar(centres, valeurs, width = h)
    m = moyenne(M)
    s = ecart_type(M)
    X = [m - 4*s + i*8*s/1000 for i in range(1000)]
    Y = [N*h*gauss(x, m, s) for x in X]
    plt.plot(X, Y, color="red")
    plt.show()


histogramme_gauss(M, 50)

