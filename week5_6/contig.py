def suffcomp(k, text, uniq=False):
    kmerslist = []
    for i in range(len(text)+1-k):
        kmerslist.append(text[i:i+k-1])
    if uniq:
        return sorted(list(kmerslist))
    else:
        return sorted(kmerslist)

def kmerstodeb(patt):
    kmerslist = []
    for i in patt:
        kmerslist = kmerslist+suffcomp(len(i), i, uniq=True)
    kmerslist = set(kmerslist)
    dict = {}
    for i in kmerslist:
        dict[i] = []
    for i in patt:
        dict[prefix(i)].append(suff(i))
    return dict

def readtocontig(kmers):
    tre = kmerstodeb(kmers)
    countso = trecount(tre)
    listcon = []
    for i in tre.keys():
        if countso[i] == [1, 1]:
            continue
        for j in tre[i]:
            contig = i
            w = j
            while True:
                contig += w[-1]
                w_degree = countso[w]
                if w_degree == [1, 1]:
                    w = tre[w][0]
                else:
                    break
            listcon.append(contig)
    return sorted(listcon)

def suff(string):
    return string[1:]


def prefix(string):
    return string[0:-1]

def trecount(tre):
    countso = {}
    for i in tre.keys():
        frneigh = tre[i]
        degrout = len(frneigh)
        if i in countso:
            countso[i][1] = degrout
        else:
            countso[i] = [0, degrout]
        for j in frneigh:
            if j in countso:
                countso[j][0] += 1
            else:
                countso[j] = [1, 0]
    return countso

if __name__ == "__main__":
    data = "".join(open('contig.txt')).split()
    print(*readtocontig(data[0:]))