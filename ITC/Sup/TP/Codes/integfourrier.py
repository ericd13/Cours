from math import *
from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np

def integ_trap(f,a,b,n=1000):
    h = (b-a)/n
    X = [a + h*k for k in range(n+1)]
    M = [a + h/2 + h*k for k in range(n)]
    a = 0
    for i in range(n):
        a += (f(X[i]) + f(X[i+1]) )*h/2
    return a

def liste_a(f,N,T):
    a,omega = [ 1/T*integ_trap(f,-(T/2),T/2)], (2*pi/T) 
    for n in range(1,N+1):
        def fn(x):
            return f(x)*cos(omega*n*x)
        a.append( 2/T*integ_trap(fn,-(T/2),T/2) )
    return a

def liste_b(f,N,T):
    b,omega = [0], (2*pi/T)
    for n in range(1,N+1):
        def fn(x):
            return f(x)*sin(omega*n*x)
        b.append( 2/T*integ_trap(fn,-(T/2),T/2) )
    return b

def somme_Fourrier(A,B,T,x):
    N = len(A)-1
    om = 2*pi/T
    return A[0]+sum( [A[n]*cos(n*om*x)+B[n]*sin(n*om*x) for n in range(1,N+1)] )
    
def triangle(x):
    return abs( -1 + (x+1)%2 )

def Snf(n,f,T,x):
    return somme_Fourrier(liste_a(f,n,T),liste_b(f,n,T),T,x)

def Fnf(N,f,T,x):
    A = liste_a(f,N,T)
    B = liste_b(f,N,T)
    om = 2*pi/T
    return A[0] + sum( [  (1-(n/(N+1)))*(A[n]*cos(n*om*x)+B[n]*sin(n*om*x)) for n in range(1,N+1)] )

def afftr(f=triangle,T=2):
    X = np.linspace(-1,3,100)
    Ytr = [triangle(x) for x in X]
    plt . plot (X , Ytr , label = " fun triangle " )
    for n in [1,2,3,5,20]:
        Yf = [Fnf(n,f,T,x) for x in X]
        plt . plot (X , Yf , label = " n = {}".format(n) )
        plt . legend ()
    plt . show ()
    
def rectangle(x):
    return 0 < x%2 < 1

def affrect(f=rectangle,T=2):
    X = np.linspace(-1,3,100)
    Ytr = [rectangle(x) for x in X]
    plt . plot (X , Ytr , label = " fun rectangle " )
    for n in [1,5,10,20,50]:
        Yf = [Fnf(n,f,T,x) for x in X]
        plt . plot (X , Yf , label = " n = {}".format(n) )
        plt . legend ()
    plt . show ()
    

affrect()

    
    

    


    
    



    
    
        

