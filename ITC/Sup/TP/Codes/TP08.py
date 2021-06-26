def longueurCollatz(a):
    u = a
    n = 0
    while u > 1:
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
        n = n + 1
    return n

def hauteurCollatz(a):
    u = a
    maximum = a
    n = 0
    n_max = 0
    while u > 1:
        n = n + 1
        if u%2 == 0:
            u = u//2
        else:
            u = 3*u + 1
        if u > maximum:
            maximum = u
            n_max = n
    return maximum, n_max

def longueurSeuil(s):
    l= 1
    a = 1
    while l < s:
        a = a + 1
        l = longueurCollatz(a)
    return a, l

def hauteurSeuil(s):
    h = 1
    a = 1
    n = 0
    while h < s:
        a = a + 1
        h, n = hauteurCollatz(a)
    return h, a, n

def taux_H(n):
    taux = 1
    k = 1
    while taux < n:
        k = k+1
        h = hauteurCollatz(k)
        if h/k > taux:
            taux = h/k
            print(k, taux)
    return k, taux

def L(s):
    LC = 1
    k = 1
    while LC < n:
        k = k+1
        l = longueurCollatz(k)
        if l > LC:
            LC = l
    return k, LC

def somme2(liste, k):
    n = len(liste)
    for i in range(n-1):
        for j in range(i+1, n):
            if liste[i] + liste[j] == k:
                return (i, j)
    return (-1, -1)

def somme2(liste, k):
    n = len(liste)
    i = 0
    j = n-1
    while i < j:
        s = liste[i] + liste[j]
        if s == k:
            return (i, j)
        elif s < k:
            i = i + 1
        else:
            j = j - 1
    return (-1, -1)

L = [1, 4, 5, 8, 11, 17, 21, 22, 25, 33]
