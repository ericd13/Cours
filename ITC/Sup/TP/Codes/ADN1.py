import random as rd

ch0 = 'GATGCATTAGTAAGGGGTAGA'

def ADN(n):
    ch = ""
    for i in range(n):
        ch = ch + rd.choice('ACGT')
    return ch

def nb_lettres(chaine, lettre):
    n = 0
    for car in chaine:
        if car == lettre:
            n = n + 1
    return n

print(nb_lettres(ch0, 'A'))

def composition(chaine):
   n = len(chaine)
   print('La chaîne', chaine, 'contient')
   for lettre in 'ACGT':
       k = nb_lettres(chaine, lettre)
       print('{:2d} fois {}, soit {:5.2f} %'.format(k, lettre, k/n*100))

composition(ch0)

def renverse(chaine):
    eniahc = ""
    for car in chaine:
       eniahc = car + eniahc
    return eniahc

print(renverse(ch0))

def changement(chaine, k, car):
    return chaine[ :k] + car + chaine[k+1 : ]

print('un changement :',changement(ch0, 5, 'C'))
def mutation(chaine):
    n = len(chaine)
    k = rd.randint(0, n-1)
    car = rd.choice('ACGT')
    while car == chaine[k]:
        car = rd.choice('ACGT')
    return changement(chaine, k, car)

print("Une mutation", mutation(ch0))

def mutations(chaine, T):
    alpha = 1.5e-2
    N = len(chaine)
    p = int(alpha*N*T)
    for i in range(p):
        chaine = mutation(chaine)
    return chaine

ch1 = mutations(ch0, 10)
print("Mutations", ch1)

def choix(car):
    if car  == "A":
        return 'GGGGCT'
    elif car  == "C":
        return 'TTTTAG'
    elif car  == "G":
        return 'AAAACT'
    else:
        return 'CCCCAG'
    
def mutationK(chaine):
    n = len(chaine)
    k = rd.randint(0, n-1)
    chx = choix(chaine[k])
    car = rd.choice(chx)
    return car == chx[0], changement(chaine, k, car)

def mutationsK(chaine, T):
    alpha = 1.5e-2
    N = len(chaine)
    p = int(alpha*N*T)
    meme = 0
    for i in range(p):
        mm, chaine = mutationK(chaine)
        if mm:
            meme = meme + 1
    return meme, p - meme, chaine

def difference(ch1, ch2):
    n = len(ch1)
    diff = ""
    for i in range(n):
        if ch1[i] != ch2[i]:
            diff = diff + 'X'
        else:
            diff = diff + ' '
    print(ch1)
    print(ch2)
    print(diff)
    
    
difference(ch0, ch1)

def reperage_codons(chaine):
    position_start = []
    position_stop = []
    for i in range(len(chaine)-2):
        codon = chaine[i:i+3]
        if codon =='ATG':
            position_start+=[i]
        if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
            position_stop += [i]     
    return(position_start, position_stop)

print(reperage_codons(ch0))

print(reperage_codons(renverse(ch0)))

def seq_codantes(chaine):
    eniahc = renverse(chaine)
    sequences = []
    for ch in [chaine, eniahc]:
        start, stop = reperage_codons(ch)   
        for i in start:
            for j in stop:
                if j > i  and (j-i)%3 == 0:
                    sequences.append(ch[i+3:j])
    return sequences

print(seq_codantes(ch0))
# ch1 = 'GGTGCCTTGACAAGGGGGAAA'
# 
# ch0 = ADN(100)
# 
# ch1 = mutations(ch0, 10)
# a, b, ch2 = mutationsK(ch0, 10)
# 
# 
# difference(ch0, ch1)
# difference(ch0, ch2)
