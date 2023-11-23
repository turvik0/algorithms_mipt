import numpy as np
def tofndit(g, i, j, k, l):
    remained = ((i, j), (j, i), (k, l), (l, k))
    rghi = [t for t in g if t not in remained]
    rghi.append((i, k))
    rghi.append((j, l))
    return rghi

def numsqfr(s):
    fs = []
    for i in s:
        latesd = permlst(i)
        fs.append(latesd)
    return fs

def edjclr(gnmm):
    g = []
    for p in gnmm:
        s = roundupp(p)
        for j in range(len(s) // 2):
            firsts = 1 + 2 * j
            seconds = (2 + 2 * j) % len(s)
            e = (s[firsts], s[seconds])
            g.append(e)
    return g


def roundupp(p):
    itemds = []
    for i in p:
        if i > 0:
            itemds.append(2 * i - 1)
            itemds.append(2 * i)
        else:
            itemds.append(-2 * i)
            itemds.append(-2 * i - 1)
    return itemds

def twogrems(gnmm, i, j, k, l):
    g = edjclr(gnmm)
    g = tofndit(g, i, j, k, l)
    gnmm = gengrr(g)
    return gnmm

def permlst(p):
    ps = []
    for i in p:
        if i > 0:
            ps.append('+' + str(i))
        elif i == 0:
            ps.append('0')
        elif i < 0:
            ps.append(str(i))
    return '(' + ' '.join(ps) + ')'

def gengrr(g):
    gnmm = []
    seend = []
    adj = np.zeros(len(g) * 2, dtype=np.int)
    for t in g:
        adj[t[0] - 1] = t[1] - 1
        adj[t[1] - 1] = t[0] - 1

    for t in g:
        whstre = t[0]
        if whstre in seend:
            continue
        seend.append(whstre)
        if whstre % 2 == 0:
            closing = whstre - 1
        else:
            closing = whstre + 1
        p = []
        i = 0
        while True:
            if whstre % 2 == 0:
                p.append(whstre // 2)
            else:
                p.append(-(whstre + 1) // 2)
            dest = adj[whstre - 1] + 1
            i = i + 1
            if (i > 100):

                return
            seend.append(dest)
            if dest == closing:
                gnmm.append(p)
                break
            if (dest % 2 == 0):
                whstre = dest - 1
            else:
                whstre = dest + 1
            assert whstre > 0
            seend.append(whstre)
    return gnmm

if __name__ == '__main__':
    with open('data.txt') as f:
        gnmm = [list(map(int, f.readline().strip()[1:-1].split(' ')))]
        [i, j, k, l] = list(map(int, f.readline().strip().split(', ')))
    gnmm = twogrems(gnmm, i, j, k, l)
    print(''.join(numsqfr(gnmm)))