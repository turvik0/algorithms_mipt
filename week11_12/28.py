import numpy
from collections import defaultdict
def dsttw(P, stry):
    bunchoflines = defaultdict(list)
    for j in P + stry:
        n = len(j)
        for i in range(n):
            bunchoflines[j[i]].append(-1 * j[(i + 1) % n])
            bunchoflines[-1 * j[(i + 1) % n]].append(j[i])
    tocheck = set(bunchoflines.keys())
    numss = 0
    while tocheck:
        numss += 1
        linee = {tocheck.pop()}
        while linee:
            nowrent = linee.pop()
            new = {i for i in bunchoflines[nowrent] if i in tocheck}
            linee |= new
            tocheck -= new
    return sum(map(len, P)) - numss


if __name__ == '__main__':
    with open('data.txt') as f:
        P, stry = [line.strip().lstrip('(').rstrip(')').split(')(') for line in f]
        P = [list(map(int, i.split())) for i in P]
        stry = [list(map(int, i.split())) for i in stry]
    answer = dsttw(P, stry)
    print(answer)