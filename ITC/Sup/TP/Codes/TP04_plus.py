import cmath 

def racines3(u):
    r = [0]*3
    v = u**(1/3)
    w = cmath.rect(1, 2*cmath.pi/3)
    for i in range(3):
        r[i] = v*w**i
    return r

def solutions1(p, q):
    delta  = q**2 + 4*p**3/27
    u = (-q + delta**(1/2))/2
    r = racines3(u)
    for i in range(3):
        r[i] = r[i] -p/(3*r[i])
    return r

def solutions(a, b, c):
    p = b - a**2/3
    q = c - a*b/3 + 2*a**3/27
    d = -a/3
    if p == 0:
        r = racines3(-q)
    else:
        r = solutions1(p, q)
    for i in range(3):
        r[i] = r[i] + d
    return r

def longueur(n):
    a = n
    for i in range(n*n):
        if a == 1:
            return i
        elif a%2 == 0:
            a = a//2
        else:
            a = 3*a + 1
        
# l_max = 1
# n0 = 1
# for n in range(2, 1500001):
#     l = longueur(n)
#     if l >= l_max:
#         n0 = n
#         l_max = l
# 
# print(n)

def suivant(k, sens, n):
    if sens > 0:
        if k < n:
            return k + 1, 1
        else:
            return n - 1, -1
    else:
        if k > 1:
            return k - 1, -1
        else:
            return 2, 1
   
# fin = 2020
# 
# d7 = 1
# sens7 = 1
# d8 = 1
# sens8 = 1
# somme = 0
# for i in range(2, fin + 1):
#     d7, sens7 = suivant(d7, sens7, 7)
#     d8, sens8 = suivant(d8, sens8, 8)
#     if d7 == 2 and d8 == 2:
#         somme = somme + i
# print(somme)

# def carres(n, p):
#     m = min(n, p)
#     nb = 0
#     for k in range(1, m + 1):
#         nb = nb + (n + 1 - k)*(p + 1 - k)
#     return nb
# 
# for i in range(1, 100):
#     for j in range(i, 100):
#         if carres(i, j) == 6400:
#             print(i, j, i*j)

# from itertools import permutations
# 
# def test(suite):
#     n = 0
#     for k in range(1, 10):
#         n = n*10 + suite[k-1]
#         if n%k != 0:
#             return False, 0
#     return True, n
# 
# for x in permutations((1, 2, 3, 4, 5, 6, 7, 8, 9)):
#     rep, n = test(x)
#     if rep:
#         print(n)

def suivant_conway(liste):
    n = len(liste)
    i = 0
    out = []
    while i < n:
        p = liste[i]
        j = i + 1
        while j < n and liste[j] == p:
            j = j + 1
        out.append(j - i)
        out.append(p)
        i = j
    return out

def conway(k, n):
    L = [k]
    for i in range(n):
        L = suivant_conway(L)
    return L
        
