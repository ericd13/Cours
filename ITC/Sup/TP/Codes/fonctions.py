## Importations


## Fonctions
def hypo1(a, b):
    """Entrées : deux nombres
      Sortie : l'hypothénuse du traingle rectangle de cotes a et b"""
    (a**2 + b**2)**0.5

def hypo2(a, b):
    """Entrées : deux nombres
      Sortie : l'hypothénuse du traingle rectangle de cotes a et b"""
    h = (a**2 + b**2)**0.5

def hypo3(a, b):
    """Entrées : deux nombres
      Sortie : l'hypothénuse du traingle rectangle de cotes a et b"""
    h = (a**2 + b**2)**0.5
    print(h)


## Principal

# print(hypo3(4, 7))

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3, 5, 1000)
Y = (np.cos(X)+np.cos(3*X)/9+np.cos(5*X)/25)*8/np.pi**2

def derivee(f, x, h = 1.0e-5):
    acc = (f(x+h) - f(x-h))/(2*h)
    acc = (f(x+h) - f(x))/h
    return acc
import math as m

print(derivee(m.sin, 1, 1e-3) - m.cos(1))
print(derivee(m.sin, 1, 1e-4) - m.cos(1))
print(derivee(m.sin, 1, 1e-5) - m.cos(1))
print(derivee(m.sin, 1, 1e-6) - m.cos(1))
print(derivee(m.sin, 1, 1e-7) - m.cos(1))
print(derivee(m.sin, 1, 1e-8) - m.cos(1))
print(derivee(m.sin, 1, 1e-9) - m.cos(1))
print(derivee(m.sin, 1, 1e-10) - m.cos(1))

def fn_derivee(f):
    h = 1.0e-1
    def df(x):
        return (f(x+h) - f(x-h))/(2*h)
    return df
f1 = np.vectorize(fn_derivee(m.sin))

plt.plot(X, np.cos(X))
plt.plot(X, np.cos(X))
plt.plot(X, f1(X))
plt.show()
