from math import *
from scipy.optimize import fsolve

def newton(f, df, x0, epsilon = 1e-8) :
    h = 1 + epsilon
    x = x0
    while h > epsilon :
        x_old = x
        x = x - f(x)/df(x)
        h = abs (x - x_old)
    return x

def newton1(f, x0, epsilon = 1e-8):
    h = 1 + epsilon
    e = epsilon/10
    x = x0
    while h > epsilon :
        x_old = x
        dfx = (f(x+e) - f(x-e))/(2*e)
        x = x - f(x)/dfx
        h = abs (x - x_old)
    return x

def f(x):
    return cos(x/2)

def df(x):
    return -sin(x/2)/2

print(newton(f, df, 3))

print(newton1(f, 3))

t = [1, 2]
f[2]