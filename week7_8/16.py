def seqrevv(seq):
    result = ''
    for i in seq:
        if i == 'A':
            result += 'T'
        elif i == 'T':
            result += 'A'
        elif i == 'G':
            result += 'C'
        elif i == 'C':
            result += 'G'
    return result[::-1]

def dnatorna(dna):
    return dna.replace('T', 'U')

def trlacprot(rna):
    proten = ""
    for i in range(0, len(rna), 3):
        if codrnna[rna[i:i + 3]]:
            proten += codrnna[rna[i:i + 3]]
        else:
            return proten
    return proten

def incodeprpept(dna, pept):
    seqncee = []
    lenghtprot = len(pept)
    for i in range(len(dna) - 3 * lenghtprot + 1):
        if trlacprot(dnatorna(dna[i:i + lenghtprot * 3])) == pept or trlacprot(dnatorna(seqrevv(dna[i:i + lenghtprot * 3]))) == pept:
            seqncee.append(dna[i:i + lenghtprot * 3])
    return seqncee

if __name__ == '__main__':
    data = "".join(open('pept.txt')).split()
    codrnna = dict()
    with open('table.txt') as f:
        for i in f:
            i = i.split()
            if len(i) > 1:
                codrnna[i[0]] = i[1]
            else:
                codrnna[i[0]] = []
    for i in incodeprpept(data[0], data[1]):
        print(i)