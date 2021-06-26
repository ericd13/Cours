def occurrences(chaine, motif):
    n = len(chaine)
    p = len(motif)
    occ = []
    for i in range(n-p+1):
        if chaine[i : i+p] == motif:
            occ.append(i)
    return occ


ch = "AACTGTCAGGACTGTCGTACTG"
mtf = "ACT"