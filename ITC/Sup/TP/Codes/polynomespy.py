A = [1, 1, 1, 1, 1, 2]
B = [-1, 1]

def degre(P):
    """Entrée : une liste qui représente un polynome
       Sortie : le degré du polynôme, -1 pour le polynome nul"""
    deg = -1
    for k in range(len(P)):
        if P[k] != 0:
            deg = k
    return deg

def reduire(P):
    """Entrée : une liste qui représente un polynome
       Sortie : une liste qui représente le même polynôme 
                et dont le dernier terme est non nul"""
    d = degre(P)
    return P[0:d+1] # On doit garder P[d]

def derive(P):
    """Entrée : une liste qui représente un polynome
       Sortie : une liste qui représente la dérivée"""
    n = len(P)
    deri=[]
    for k in range(1, n):
        deri.append(k*P[k])
    return reduire(deri)

def calculNaif(x,  P):
    """Entrée : un nombre 
                et une liste représentant un polynome
       Sortie : la valeur de P(x)"""
    n = len(P)
    val = 0
    for k in range(n):
        val = val + P[k]*x**(k)
    return val

def horner(x, P):
    """Entrée : un nombre 
                et une liste représentant un polynome
       Sortie : la valeur de P(x)"""
    n = len(P)
    res = 0
    for k in range(1, n+1):
        res= x*res + P[-k]
    return res 

def sommeP(P1,P2):
    """Entrée : deux listes
       Sortie : une liste qui représente la somme des
                polynômes représentés par les listes"""
    n1 = len(P1)
    n2 = len(P2)
    som = []
    for i in range(min(n1, n2)):
        som.append(P1[i] + P2[i])
    if n1 < n2:
        som = som + P2[n1:n2]
    elif n2 < n1:
        som = som + P1[n2:n1]
    return reduire(som)

def produitMonome(P, a, k):
    """Entrée : une liste P, un réel a et un entier positif k
       Sortie : une liste qui représente le produit par aX**k
                du polynôme représenté par la liste P"""
    n = len(P)
    res = []
    for i in range(k):
        res.append(0)
    for i in range(n):
        res.append(a*P[i])
    return reduire(res)

def produitP(P1, P2):
    """Entrée : deux listes 
       Sortie : une liste qui représente le produit des
                deux polynômes représentés par les listes"""
    n = len(P1)
    res = []
    for k in range(n):
        res = sommeP(res, produitMonome(P2, P1[k], k))
    return reduire(res)

def division(A, B):
    n = degre(A)
    m = degre(B)
    q = max(0, n-m+1)
    Q = [0]*q
    r = n
    R = A
    while r >= m:
        a = R[r]/B[m]
        Q[r-m] = a
        P1 = produitMonome(B, -a, r-m)
        R = sommeP(R, P1)
        r = degre(R)
    return R, Q

