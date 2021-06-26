from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def Newton(f, f_prime, a, epsilon):
    """ Entrées : deux fonctions réelles, 2 réels
        Requis : f est C1 sur un intervalle contenant a
                 f_prime est la dérivée de f
                 epsilon > 0
        Sortie : c appartenant à [a;b] tel qu'il existe un 
                 zero c' de f avec |c - c'| de l'ordre de epsilon """
    x = a
    ecart = 1 + epsilon
    while ecart >= epsilon:
        x_old = x
        x = x - f(x)/f_prime(x)
        ecart = abs(x - x_old)
    return x

def P(x):
 return 90 + x*(3 + x*(-23+x*(1+x)))
 
def dP(x):
 return 3 + x*(-46+x*(3+x*4))

def suite(a, b, n):
    pas  = (b-a)/(n-1)
    X = [0]*n
    for i in range(n):
        X[i] = a + pas*i
    return X

X = suite(-5, 2, 100000)
Y = [Newton(P, dP, x, 0.0001) for x in X]
plt.plot(X, Y)
plt.show()

a = -0.5361498906
n = 8
for k in range(n):
    h = 10**(-k)
    X = suite(a-h, a+h, 10000)
    Y = [Newton(P, dP, x, 0.0001) for x in X]
    plt.subplot((n+1)//2, 2, k+1)
    plt.plot(X, Y)
plt.show()

