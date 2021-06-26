def nb_chiffres(n):
    """Entrée : un entier positif
       Sortie : le nombre de chiffres de n"""
    p = 0
    while n > 0:
        p = p + 1
        n = n//10
    return p

def chiffres(n):
    """Entrée : un entier positif
       Sortie : les chiffres de n sous forme d'une liste"""
    p = nb_chiffres(n)
    chf = [0]*p
    for i in range(p):
        c = n%10 # le chiffre
        n = n//10
        chf[p-1-i] = c
    return chf

def nombre(liste):
    p = len(liste)
    n = 0
    for i in range(p):
        n = 10*n + liste[i]
    return n

def retournement(n):
    liste = chiffres(n)
    etsil = liste[ : : -1]
    return nombre(etsil)

def test(n):
    m = retournement(n)
    return n == m

def suite(u0, n):
    u = u0
    for i in range(n):
        u = u + retournement(u)
        print(u)
    return u

nb = 0
for a in range(1, 1000):
    u = a
    n = 0
    while n < 50 and not test(u):
        u = u + retournement(u)
        n = n + 1
    if n == 50:
        print(a)
        nb = nb + 1
print(nb)

for a in range(1, 196):
    u = a
    n = 0
    while not test(u):
        u = u + retournement(u)
        n = n + 1
    if n == 24:
        print(a)
        print(u)
        break


# nb = 0
# n_max = 1
# a_n_max = 1
# u_max = 1
# a_u_max = 1
# for a in range(1, 10000):
#     u = a
#     n = 0
#     while n < 25 and not test(u):
#         u = u + retournement(u)
#         n = n + 1
#     if n == 25:
#         print("Lychrel :", a)
#         nb = nb + 1
#     if n == 24:
#         print("Longueur 24 pour", a, "u =", u)


def facto(n):
    f = 1
    for i in range(n):
        f = f*(i+1)
    return f
    
l = chiffres(facto(100))
somme = 0
for x in l:
    somme = somme + x
print("La somme des chiffres de 100! est",somme)
       
fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
for n in range(1, 1000000):
    l = chiffres(n)
    s = 0
    for x in l:
        s = s + fact[x]
    if n ==  s:
        print(n)

def sum_c(n):
    l = chiffres(n)
    s = 0
    for x in l:
        s = s + x
    return s

max = 1
a_max = 1
b_max = 1
for a in range(100):
    for b in range(101):
        s = sum_c(a**b)
        if s > max:
            print(a, b, s)
            max = s
            a_max = a
            b_max = b
print(a_max, b_max, max)


for i in range(5):
    for j in range(5):
        print(i, j)
        if i + j == 7:
            break
