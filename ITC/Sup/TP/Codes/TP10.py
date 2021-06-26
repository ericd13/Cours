# from time import time
# import matplotlib.pyplot as plt
# 
# repet = 1000
# long = [100, 200, 500, 1000, 2000, 5000, 10000]
# app = []
# mult = []
# for n in long:
#     a = time()
#     for _ in range(repet):
#         l = [0]*n
#         for i in range(n):
#             l[i] = i
#     app.append(time() - a)
#     a = time()
#     for _ in range(repet):
#         l = []
#         for i in range(n):
#             l.append(i)
#     mult.append(time() - a)
# 
# plt.plot(long, app, label = "adjonction")
# plt.plot(long, mult, label = "remplissage")
# plt.legend()
# plt.show()

from random import randint

#L = [randint(-2, 3) for _ in range(30)]
Ex = [0, -2, 1, -2, -2, -1, 2, 3, 3, 0, 0, 0, 1, 2, 0,
      -2, -1, -1, 1, 3, 3, 1, 3, 0, 2, -1, -1, 1, 1, 1]

Expr = "1+2*(7-(4-3)*((2-5)+2*((12/4-8)+2*3)))"
Expr1 = "(1+2))*((5-3)"

def positifs(L):
    pos = []
    for x in L:
        if x > 0:
           pos.append(x)
    return pos

def positions(x, L):
    n = len(L)
    pos = []
    for i in range(n):
        if L[i] == x:
           pos.append(i)
    return pos

def indices_max(L):
    maxi = L[0]
    for x in L:
        if x > maxi:
            maxi = x
    return positions(maxi, L)

def indices_max(L):
    n = len(L)
    maxi = L[0]
    pos = [0]
    for i in range(1, n):
        if L[i] > maxi:
            maxi = L[i]
            pos = [i]
        elif L[i] == maxi:
            pos.append(i)
    return pos


def sans_doublon(L):
    n = len(L)
    L1 = [L[0]]
    for i in range(1, n):
        if L[i] != L[i-1]:
            L1.append(L[i])
    return L1

def testPar(ch):
    n = len(ch)
    ouv = 0
    for i in range(n):
        car = ch[i]
        if car == "(":
            ouv = ouv + 1
        if car == ")":
            if ouv == 0:
                return False
            else:
                ouv = ouv - 1
    return ouv == 0

def listePar(ch):
    n = len(ch)
    par = []
    ouv = []
    for i in range(n):
        car = ch[i]
        if car == "(":
            ouv.append(i)
        if car == ")":
            j = ouv.pop()
            par.append((j, i))
    return par

def mauvaisePar(ch):
    n = len(ch)
    ouv = []
    for i in range(n):
        car = ch[i]
        if car == "(":
            ouv.append(i)
        if car == ")":
            if ouv == []:
                return i
            else:
                j = ouv.pop()
    if ouv == []:
        return -1
    else:
        return ouv.pop()
 
def parentheses(ch):
    n = len(ch)
    par = []
    ouv = []
    for i in range(n):
        car = ch[i]
        if car == "(":
            ouv.append(i)
        if car == ")":
            if ouv == []:
                par.append((-1, i))
            else:
                j = ouv.pop()
                par.append((j, i))
    while ouv != []:
        i = ouv.pop()
        par.append((i, -1))
    return par



