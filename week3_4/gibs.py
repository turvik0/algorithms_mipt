import numpy

from random import randint

def pseudoprof(Motif):
    lenght = len(Motif[0])
    prof = []
    for i in range(lenght):
        merge = ''.join([Motif[j][i] for j in range(len(Motif))])
        prof.append([float(merge.count(i)+1)/float(len(merge)+4) for i in 'ACGT'])
    return prof

def motgifsample(dna_string, k, t, N, motini=None):
    if motini:
        Motif = motini
    else:
        inrand = [randint(0, len(dna_string[0]) - k) for a in range(t)]
        Motif = [dna_string[i][r:r + k] for i, r in enumerate(inrand)]

    num_best = [score(Motif), list(Motif)]

    for j in range(N):
        i = randint(0, t - 1)
        profcurr = pseudoprof([x for amotif, x in enumerate(Motif) if amotif != i])
        Motif[i] = kprofrand(dna_string[i], k, profcurr)
        numcurr = score(Motif)
        if numcurr < num_best[0]:
            num_best = [numcurr, list(Motif)]

    return num_best


def dist_ham(str1, str2):
    num = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            num += 1
    return num

def probmost(dna, k, prof):
    bprob = [-1, None]
    locnuc = {nucl:i for i,nucl in enumerate('ACGT')}
    for i in range(len(dna)-k+1):
        numb = 1
        for j, nucl in enumerate(dna[i:i+k]):
            numb *= prof[j][locnuc[nucl]]
        if numb > bprob[0]:
            bprob = [numb, dna[i:i+k]]

    return bprob[1]
def profmotif(prof, dna, k):
    return [probmost(i,k,prof) for i in dna]

def motprob(dna_string,k,t):
    inrand = [randint(0,len(dna_string[0])-k) for a in range(t)]
    Motif = [dna_string[i][r:r+k] for i,r in enumerate(inrand)]
    num_best = [score(Motif), Motif]
    while True:
        profcurr = pseudoprof(Motif)
        Motif = profmotif(profcurr, dna_string, k)
        numcurr = score(Motif)
        if numcurr < num_best[0]:
            num_best = [numcurr, Motif]
        else:
            return num_best

def score(Motif):
    lenght=len(Motif[0])
    score = 0
    for i in range(lenght):
        motif = ''.join([Motif[j][i] for j in range(len(Motif))])
        score += min([dist_ham(motif, homogeneous*len(motif)) for homogeneous in 'ACGT'])
    return score

def kprofrand(dna, k, prof):
    locnuc = {nucl: index for index, nucl in enumerate('ACGT')}
    listprobs = []
    for i in range(len(dna) - k):
        numb = 1.
        for j, nucl in enumerate(dna[i:i + k]):
            numb *= prof[j][locnuc[nucl]]
        listprobs.append(numb)

    i = numpy.random.choice(len(listprobs), p = numpy.array(listprobs) / numpy.sum(listprobs))
    return dna[i:i + k]


if __name__ == '__main__':
    data = "".join(open('gibs.txt')).split()
    k, t, N = int(data[0]), int(data[1]), int(data[2])
    dna_string = data[3:]
    motb = [k * t, None]
    for s in range(20):
        motcurr = motgifsample(dna_string, k, t, N)
        if motcurr[0] < motb[0]:
            motb = motcurr
    print('\n'.join(motb[1]))