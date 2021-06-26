import math

def logarithme(x, base = math.e):
    """Entrees : un nombre positif, x
                 un nombre positif optionnel, base
                 qui vaut e par défaut
      Sortie : le logarithme en base "base" de x"""
    y = math.log(x)/math.log(base)
    return y
