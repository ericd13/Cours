import math as m
import matplotlib.pyplot as plt
from random import randint

def carres(liste):
    n = len(liste)
    L = [0]*n
    for i in range(n):
        L[i] = liste[i]**2
    return L

def appliquer(f, liste):
    n = len(liste)
    L = [0]*n
    for i in range(n):
        L[i] = f(liste[i])
    return L

def harmo(x):
    return (x+4)/(x+1)

def listeX(a, b, n):
    pas = (b-a)/(n-1)
    X = [0]*n
    for k in range(n):
        X[k] = a + k*pas 
    return X

def listeX(a, b, n):
    pas = (b-a)/(n-1)
    X = [0]*n
    for k in range(n):
        X[k] = a + k*pas 
    return X

def f(x):
    return m.exp(-x)*m.cos(2*m.pi*x)
    
# X = listeX(0, 5, 500)
# Y = appliquer(f, X)
# plt.plot(X, Y)
# plt.show()
# 
# X = listeX(-3, 5, 500)
# Y1 = appliquer(m.cos, X)
# Y2 = appliquer(m.sin, X)
# plt.plot(X, Y1, label="cosinus")
# plt.plot(X, Y2, label="sinus")
# plt.legend()
# plt.show()

def tiragesDe(n):
    """Entrée : un entier positif
       Sortie : la liste des tirages de n dés""" 
    resultat = [0]*n
    for i in range(n):
        resultat[i] = randint(1, 6)
    return resultat

def occurrences(liste):
    """Entrée : un entier positif
       Sortie : la liste de la distribution des valeurs
                d'une liste d'entiers de 1 à 6""" 
    n = len(liste)
    resultat = [0]*6
    for i in range(n):
        k = liste[i] - 1
        resultat[k] += 1
    return resultat

# X = tiragesDe(1200)
# valeurs = [1, 2, 3, 4, 5, 6]
# occ = occurrences(X)
# plt.bar(valeurs, occ)
# plt.show()

def echanger(liste, i, j):
    temp = liste[i]
    liste[i] = liste[j]
    liste[j] = temp

def retourner(liste):
    n = len(liste)
    for i in range(n//2): 
        echanger(liste, i, n-1-i)

def decaler1(liste):
    n = len(liste)
    temp = liste[-1]
    for i in range(n-1, 0, -1): 
        liste[i] = liste[i-1]
    liste[0] = temp

def decaler(k, liste):
    for i in range(k):
        decaler1(liste)

def inverser(liste, i, j):
    m = (j + i)//2
    for k in range(i, m):
        echanger(liste, k, i + j - k -1)

def decalerbis(k, liste):
    n = len(liste)
    retourner(liste)
    inverser(liste, 0, k)
    inverser(liste, k, n)

def zero_un(liste):
    n = len(liste)
    k = 0
    for i in range(n):
        if liste[i] == 0:
            echanger(liste, k, i)
            k = k + 1

def flag(liste):
    n = len(liste)
    k1 = 0
    k2 = 0
    for i in range(n):
        if liste[i] == -1:
            echanger(liste, i, k2)
            echanger(liste, k1, k2)
            k1 = k1 + 1
            k2 = k2 + 1
        if liste[i] == 0:
            echanger(liste, i, k2)
            k2 = k2 + 1
        print(liste)
