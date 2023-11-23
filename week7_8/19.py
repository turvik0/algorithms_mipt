def mssparr(spectrr):
    return spectrr[-1]


def massppt(pept):
    mass = 0
    for i in range(len(pept)):
        mass += tablaminac[pept[i]]
    return mass

def sesclde(spectrr, n):
    nmsaccpept = 0
    piptlead = ''
    leaderboard = ['']
    while leaderboard:
        leaderboard = expepetss(leaderboard)
        loop = list(leaderboard)
        for pept in loop:
            mass = massppt(pept)
            massneighb = mssparr(spectrr)
            if mass == massneighb:
                numscc = numlinsc(pept, spectrr)
                if numscc > nmsaccpept:
                    piptlead = pept
                    nmsaccpept = numscc
            elif mass > massneighb:
                leaderboard.remove(pept)
        leaderboard = rtimm(leaderboard, spectrr, n)
    return piptlead

def spectrrlin(pept):
    masspreif = [0 for i in range(len(pept) + 1)]
    for i in range(len(pept)):
        masspreif[i + 1] = masspreif[i] + tablaminac[pept[i]]
    linialspctrrr = []
    for i in range(len(pept)):
        for j in range(i + 1, len(pept) + 1):
            linialspctrrr.append(masspreif[j] - masspreif[i])
    linialspctrrr.append(0)
    linialspctrrr = sorted(linialspctrrr)
    return linialspctrrr


def numlinsc(pept, spectrr):
    ls = spectrrlin(pept)
    cs = spectrr.copy()
    numscc = 0
    for c in ls:
        if c in cs:
            numscc += 1
            cs.remove(c)
    return numscc

def expepetss(pepts):
    pptdsnw = []
    for i in pepts:
        for key in tablaminac:
            pptdsnw.append(i + key)
    return pptdsnw

def rtimm(leaderboard, spectrr, N):
    numsccs = []
    if len(leaderboard) < N:
        returntoback = leaderboard
    else:
        for pep in leaderboard:
            numsccs.append(numlinsc(pep, spectrr))
        numsccs.sort(reverse=True)
        numscc_min = numsccs[N - 1]
        peptkval = []
        for i, pep in enumerate(leaderboard):
            if numlinsc(pep, spectrr) >= numscc_min:
                peptkval.append(i)
        returntoback = []
        for k in peptkval:
            returntoback.append(leaderboard[k])
    return returntoback

if __name__ == '__main__':
    tablaminac = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113,
                             'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156,
                             'Y': 163, 'W': 186}
    with open('pept.txt') as f:
        n = int(f.readline())
        spectrr = list(map(int, f.readline().split()))
    piptlead = sesclde(spectrr, n)
    mssleadppti = []
    for i in piptlead:
        mssleadppti.append(tablaminac[i])
    print('-'.join([str(i) for i in mssleadppti]))