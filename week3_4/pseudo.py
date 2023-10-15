def motif_greed(dna, k, t):
    motif_b = []
    for i in range(t):
        motif_b.append(dna[i][:k])
    for i in range(len(dna[0]) - k + 1):
        Motifs = []
        Motifs.append(dna[0][i: i + k])
        for j in range(1, t):
            prof = prof_create(Motifs)
            Motifs.append(most_prob(dna[j], prof, k))
        if score(motif_b) > score(Motifs):
            motif_b = Motifs
    return motif_b



def score(Motifs):
    consen_string = consen(Motifs)
    score = 0
    for motif in Motifs:
        score += dist_ham(consen_string, motif)
    return score

def probab(prof, string):
    probablity = 1
    for i in range(0, len(string)):
        if string[i] == 'A':
            probablity = probablity * prof[i][0]
        elif string[i] == 'G':
            probablity = probablity * prof[i][2]
        elif string[i] == 'T':
            probablity = probablity * prof[i][3]
        elif string[i] == 'C':
            probablity = probablity * prof[i][1]
    return probablity

def consen(Motifs):
    lenght = len(Motifs[0])
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
        elif numc >= max(numa, numg, numt):
            consen_string += "C"
        elif numt >= max(numc, numg, numa):
            consen_string += "T"
        elif numg >= max(numc, numa, numt):
            consen_string += "G"
    return consen_string

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
        prof.append([numa / (lenght + 4), numc/ (lenght + 4),
                        numg / (lenght + 4), numt / (lenght + 4)])
    return prof


def dist_ham(str1, str2):
    num = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            num += 1
    return num

def most_prob(dna_list, prof, k):
    patbest = dna_list[0:0 + k]
    probbest = 0
    for i in range(len(dna_list) - k + 1):
        string = dna_list[i:i + k]
        newprob = probab(prof, string)
        if newprob > probbest:
            patbest = string
            probbest = newprob
    return patbest


if __name__ == "__main__":
    data = "".join(open('motif_greed_pseudocounts.txt')).split()
    print(*motif_greed(data[2: ], int(data[0]), int(data[1])))