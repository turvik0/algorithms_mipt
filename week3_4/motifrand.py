import numpy
import random

def probmprof(dna_list, prof, k):
    patbest = dna_list[0:0 + k]
    probbest = 0
    for i in range(len(dna_list) - k + 1):
        string = dna_list[i:i + k]
        newprob = probab(prof, string)
        if newprob > probbest:
            patbest = string
            probbest = newprob
    return patbest

def motifiter(dna, k ,t):
    i = 0
    motif_b = []
    for i in range(t):
        motif_b.append(dna[i][:k])
    while i < 1000:
        Motifs = motifrand(dna, k, t)
        if score(Motifs) < score(motif_b):
            motif_b = Motifs
        i = i+1
    return motif_b

def score(Motifs):
    consen_string = consen(Motifs)
    score = 0
    for motif in Motifs:
        score += dist_ham(consen_string, motif)
    return score

def motifrand(dna, k, t):
    motif_b = motifgetr(dna, k)
    while True:
        prof = prof_create(motif_b)
        Motifs = create_motifs(prof, dna)
        if score(Motifs) < score(motif_b):
            motif_b = Motifs
        else:
            return motif_b


def create_motifs(prof, dna):
    Motifs = []
    for i in dna:
        Motifs.append(probmprof(i, prof, len(prof)))
    return Motifs

def motifgetr(dna,k):
    Motifs = []
    for i in dna:
        dot = random.randint(0, len(i)-k)
        Motifs.append(i[dot:dot + k])
    return Motifs




def prof_create(Motifs):
    lenght=len(Motifs[0])
    prof =[]
    for i in range(lenght):
        numa, numc, numg, numt = 1, 1, 1, 1
        for motif in Motifs:
            if motif[i] == 'A':
                numa += 1
            elif motif[i] == 'T':
                numt += 1
            elif motif[i] == 'G':
                numg += 1
            elif motif[i] == 'C':
                numc += 1
        prof.append([numa / (len(Motifs) + 4), numc/ (len(Motifs) + 4),
                        numg / (len(Motifs) + 4), numt / (len(Motifs) + 4)])
    return prof


def probab(prof, string):
    probablity = 1
    for i in range(0, len(string)):
        if string[i] == 'A':
            probablity = probablity * prof[i][0]
        elif string[i] == 'T':
            probablity = probablity * prof[i][3]
        elif string[i] == 'G':
            probablity = probablity * prof[i][2]
        elif string[i] == 'C':
            probablity = probablity * prof[i][1]
    return probablity
#-----------------------------------------
def dist_ham(str1, str2):
    num = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            num += 1
    return num


def consen(Motifs):
    lenght=len(Motifs[0])
    consen_string = ''
    for i in range(lenght):
        numa, numc, numg, numt = 0, 0, 0, 0
        for motif in Motifs:
            if motif[i] == 'A':
                numa += 1
            elif motif[i] == 'T':
                numt += 1
            elif motif[i] == 'G':
                numg += 1
            elif motif[i] == 'C':
                numc += 1
        if numa >= max(numc, numg, numt):
            consen_string += "A"
        elif numt >= max(numc, numg, numa):
            consen_string += "T"
        elif numg >= max(numc, numa, numt):
            consen_string += "G"
        elif numc >= max(numa, numg, numt):
            consen_string += "C"
    return consen_string

if __name__ == "__main__":
    data = "".join(open('motifrand.txt')).split()
    motif_b = motifiter(data[2:], int(data[0]), int(data[1]))
    for i in motif_b:
        print(i)