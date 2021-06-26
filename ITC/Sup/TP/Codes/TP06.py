import matplotlib.pyplot as plt

T0 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
           1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
           2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0,
           3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]

X0 = [0.00, 0.84, 1.56, 2.18, 2.70, 3.12, 3.45, 3.70, 3.87,
            3.96, 4.00, 3.97, 3.88, 3.75, 3.58, 3.37, 3.13,
            2.87, 2.59, 2.29, 2.00, 1.70, 1.40, 1.12, 0.86,
            0.62, 0.41, 0.24, 0.11, 0.02, 0.00, 0.03, 0.12,
            0.29, 0.54, 0.87, 1.29, 1.81, 2.43, 3.15, 4.00]

Y0 = [1.64, 3.64, 5.71, 6.16, 8.08, 9.31, 9.82, 9.91, 10.8,
            10.6, 11.4, 10.7, 10.8, 10.6, 9.58, 9.43, 8.85,
            8.95, 7.92, 6.66, 6.04, 4.79, 5.24, 4.05, 3.91,
            3.12, 2.82, 1.92, 2.21, 2.03, 1.42, 1.82, 2.45,
            2.18, 2.58, 3.95, 4.85, 6.29, 6.83, 8.61, 10.5]

Z0 = [1, 6, 7, 3, 7, 2, 9, 4, 0, 6, 2, 2, 1, 5,
      3, 6, 2, 7, 3, 3, 2, 4, 5, 4, 0, 3, 9, 8,
      5, 9, 6, 2, 2, 1, 4, 5, 5, 4, 8, 3, 9]

def moyenne(X):
    n = len(X)
    somme = 0
    for x in X:
        somme = somme + x
    return somme/n

def var(X):
    n = len(X)
    mX = moyenne(X)
    somme = 0
    for x in X:
        somme = somme + (x - mX)**2
    return somme/n

def cov(X, Y):
    n = len(X)
    mX = moyenne(X)
    mY = moyenne(Y)
    somme = 0
    for i in range(n):
        somme = somme + (X[i] - mX)*(Y[i] - mY)
    return somme/n

def regression(X, Y):
    a = cov(X, Y)/var(X)
    b = moyenne(Y) - a*moyenne(X)
    return a, b

# a , b = regression ( X0 , Y0 )
# c = a *4 + b
# plt . plot ( X0 , Y0 , 'o')
# plt . plot ([0 , 4] , [b , c ])
# plt . show ()

def tout_positif(liste):
    """Entrée : une liste de nombre
      Sortie : True si tous les termes sont positifs
               False sinon"""
    resultat = True
    for x in liste:
        if x < 0:
            resultat = False
    return resultat

def existe_positif(liste):
    """Entrée : une liste de nombre
      Sortie : True si au moins un terme est positif
                False sinon"""
    resultat = False
    for x in liste:
        if x >= 0:
            resultat = True
    return resultat

def croissante(liste):
    """Entrée : une liste de nombre
      Sortie : True si tous la liste est croissante
               False sinon"""
    n = len(liste)
    resultat = True
    for i in range(n-1):
        if liste[i] > liste[i+1]:
            resultat = False
    return resultat

def minimum(liste):
    mini = liste[0]
    for x in liste:
        if x < mini:
            mini = x
    return mini

def indiceMax(liste):
    n = len(liste)
    i_max = 0
    for i in range(1, n):
        if liste[i] >= liste[i_max]:
            i_max = i
    return i_max

def maximum3(liste):
    n = len(liste)
    max3 = liste[0] + liste[1] + liste[2]
    for i in range(1, n-2):
        s3 = liste[i] + liste[i+1] + liste[i+2]
        if s3 > max3:
            max3 = s3
    return max3

def second(liste):
    n = len(liste)
    max1 = max(liste[0], liste[1])
    max2 = min(liste[0], liste[1])
    for i in range(2, n):
        x = liste[i]
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
    return max2

def augMax(liste):
    n = len(liste)
    augM = 0
    for i in range(n-1):
        for j in range(i, n):
            aug = liste[j] - liste[i]
            if aug > augM:
                augM = aug
    return augM

def second(liste):
    n = len(liste)
    max1 = liste[0]
    max2 = liste[0]
    for i in range(1, n):
        x = liste[i]
        if x > max1:
            max2 = max1
            max1 = x
        elif (max1 == max2 > x) or (max1 > x > max2):
            max2 = x
    return max2


def majoritaire(liste):
    n = len(liste)
    nb_maj = 1
    maj = liste[0]
    encours = 1
    for i in range(1, n):
        if liste[i] == liste[i-1]:
            encours += 1
            if encours > nb_maj:
                nb_maj = encours
                maj = liste[i]
        else:
            encours = 1
    return maj

def pivot(liste):
    n = len(liste)
    gauche = 0
    droite = 0
    for x in liste:
        droite = droite + x
    e_min = abs(droite - gauche)
    i_min = 0
    for i in range(n):
        x= liste[i]
        gauche = gauche + x
        droite = droite - x
        e = abs(gauche - droite)
        if e < e_min:
           e_min = e
           i_min = i + 1
    return i_min

def augMax1(liste):
    n = len(liste)
    augM = 0
    mini = liste[0]
    for i in range(1, n):
        mini = min(mini, liste[i])
        aug = liste[i] - mini
        if aug > augM:
            augM = aug
    return augM

def trancheMax(liste):
    n = len(liste)
    tMax = 0
    sMin = 0
    S = 0
    for i in range(n):
        S = S + liste[i]
        t = S - sMin
        if t > tMax:
            tMax = t
        sMin = min(sMin, S)
    return tMax

