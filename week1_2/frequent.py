def compl(i):
    return {'A':'T','C':'G','G':'C','T':'A'}[i]
def rcompl(j):
    return ''.join([compl(j[i]) for i in range(len(j)-1, -1,-1)])
def dist(st1, st2):
    numbers = 0
    for s1, s2 in zip(st1, st2):
        if s1 != s2:
            numbers += 1
    return numbers

def relat(sample, d):
    if d == 0:
        return sample
    if len(sample) == 1:
        return ["A", "C", "G", "T"]
    close= []
    suff = relat(sample[1:], d)
    for i in suff:
        if dist(sample[1:], i) < d:
            for x in ["A", "C", "G", "T"]:
                close.append(x + i)
        else:
            close.append(sample[0] + i)
    return close

def findfr(st, k, d):
    result = []
    keys = []
    neighborhood = set()
    for i in range(len(st) - k + 1):
        keys.append(st[i: i + k])
    for i in range(len(st) - k + 1):
        keys.append(rcompl(st[i: i + k]))
    for i in keys:
        neighborhood.update(set(relat(i, d)))
    m = 0
    for i in neighborhood:
        frti = 0
        for j in keys:
            if dist(i, j) <= d:
                frti += 1
        if m < frti:
            m = frti
            result = [i]
        elif m == frti:
            result.append(i)
    return result

data = "".join(open('rosalind_ba1j.txt')).split()
print(*findfr(data[0], int(data[1]), int(data[2])))