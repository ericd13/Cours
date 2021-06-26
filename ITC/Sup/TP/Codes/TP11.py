def diviseurs(n):
    div = []
    for k in range(1, n+1):
        if n%k == 0:
            div.append(k)
    return div

def diviseurs(n):
    div = []
    for k in range(1, n//2+1):
        if n%k == 0:
            div.append(k)
    div.append(n)
    return div

def premier(n):
    return len(diviseurs(n)) == 2

def premier(n):
    p = 2
    while p*p <= n:
        if n%p == 0:
            print(p)
            return False
        p = p + 1
    return p > 1

def crible(n):
    era = [True]*(n+1)
    prem = []
    era[0] = False
    era[1] = False
    for k in range(2, n+1):
        if era[k]:
            prem.append(k)
            for i in range(2*k, n+1, k):
                era[i] = False
    return prem

def pgcd(a, b):
    while b > 0:
        r = a%b
        a = b
        b = r
    return a

def euclide(a, b):
    while b > 0:
        r = a%b
        a = b
        b = r
    return a

def bezout(a, b):
    r = pgcd(a, b)
    if r == b:
        return (0, 1)
    else:
        p = 1
        while p*a % b != r:
            p = p + 1
        return (p, -((p*a)//b))
    
def decomposition(n):
    facteurs = []
    d = 2
    while d <= n:
        if n%d == 0:
            facteurs.append(d)
            n = n//d 
        else:
            d = d + 1
    return facteurs

def inter(L1, L2):
    n1 = len(L1)
    n2 = len(L2)
    int = []
    i1 = 0
    i2 = 0
    while i1 < n1 and i2 < n2:
        print(i1, i2)
        if L1[i1] == L2[i2]:
            int.append(L1[i1])
            i1 = i1 + 1
            i2 = i2 + 1
        elif L1[i1] < L2[i2]:
            i1 = i1 + 1
        else:
            i2 = i2 + 1
    return int

def produit(liste):
    p = 1
    for x in liste:
        p = p*x
    return p

def pgcd_dec(a, b):
    d1 = decomposition(a)
    d2 = decomposition(b)
    return produit(inter(d1, d2))

def bezout(a, b):
    p_a = 1
    q_a = 0
    p_b = 0
    q_b = 1
    while b > 0:
        r = a%b
        d = a//b
        a = b
        b = r
        p = p_a - d*p_b
        q = q_a - d*q_b
        p_a = p_b
        q_a = q_b
        p_b = p
        q_b = q
    return a, p_a, q_a

# Une écriture récursive

def bezout(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, p, q = bezout(b, a%b)
        return d, q, p - q*(a//b)


def g([x, y]):
    return y - x