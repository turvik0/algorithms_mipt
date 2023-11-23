def cyclospectrr(pept):
    specmbright = [0]
    masspreif = [0]
    for i in range(len(pept)):
        masspreif.append(masspreif[i]+pept[i])
    for i in range(len(masspreif) - 1):
        for j in range(i + 1, len(masspreif)):
            specmbright.append(masspreif[j]-masspreif[i])
            if i > 0 and j < len(masspreif)-1:
                specmbright.append(masspreif[-1] - (masspreif[j] - masspreif[i]))
    return sorted(specmbright)


def gttpelemnw(dctconvo, m):
    convolution = [(key, val) for key, val in dctconvo.items()]
    convoright = sorted(convolution, key=lambda entry: entry[1], reverse=True)
    rtimm_pos = m-1
    for rtimm_pos in range(m - 1, len(convoright) - 1):
        if convoright[rtimm_pos][1] > convoright[rtimm_pos + 1][1]:
            break
    return [i[0] for i in convoright[:rtimm_pos + 1]]


def expepetss(pepts, amino_acid_mass_list):
    pptdsnw = []
    for pept in pepts:
        for mass in amino_acid_mass_list:
            new_pept = list(pept)
            new_pept.append(mass)
            pptdsnw.append(new_pept)
    return pptdsnw


def mssparr(spectrr):
    return spectrr[-1]


def make_numscc(pept, spectrr):
    ls = cyclospectrr(pept)
    cs = spectrr.copy()
    numscc = 0
    for c in ls:
        if c in cs:
            numscc += 1
            cs.remove(c)
    return numscc

def secsycllconn(m, n, spectrr):
    spectrr = sorted(spectrr)
    dctconvo = gtpktspectrl(spectrr)
    topamnasidmss = gttpelemnw(dctconvo, m)
    return sesclde(spectrr, n, topamnasidmss)

def gtpktspectrl(spectrr):
    dctconvo = {}
    spectrr = sorted(spectrr)
    for i in range(len(spectrr) - 1):
        for j in range(i, len(spectrr)):
            mass = spectrr[j] - spectrr[i]
            if mass < 57 or mass > 200:
                continue
            if mass in dctconvo:
                dctconvo[mass] += 1
            else:
                dctconvo[mass] = 1
    return dctconvo

def rtimm(leaderboard, spectrr, N):
    numsccs = []
    if len(leaderboard) < N:
        returntoback = leaderboard
    else:
        for pep in leaderboard:
            numsccs.append(linearnumscc(pep, spectrr))
        numsccs.sort(reverse=True)
        numscc_min = numsccs[N - 1]
        peptkval = []
        for i, pep in enumerate(leaderboard):
            if linearnumscc(pep, spectrr) >= numscc_min:
                peptkval.append(i)
        returntoback = []
        for k in peptkval:
            returntoback.append(leaderboard[k])
    return returntoback


def sesclde(spectrr, n, amino_acid_mass_list):
    piptleadnumscc = 0
    piptlead = ''
    leaderboard = [[]]
    while leaderboard:
        leaderboard = expepetss(leaderboard, amino_acid_mass_list)
        loop = list(leaderboard)
        for pept in loop:
            mass = sum(pept)
            massneighb = mssparr(spectrr)
            if mass == massneighb:
                numscc = make_numscc(pept, spectrr)
                if numscc > piptleadnumscc:
                    piptlead = pept
                    piptleadnumscc = numscc
            elif mass > massneighb:
                leaderboard.remove(pept)
        leaderboard = rtimm(leaderboard, spectrr, n)
    return piptlead

def linearnumscc(pept, spectrr):
    ls = spectrrlin(pept)
    cs = spectrr.copy()
    numscc = 0
    for c in ls:
        if c in cs:
            numscc += 1
            cs.remove(c)
    return numscc

def spectrrlin(pept):
    linialspctrrr = []
    masspreif = [0 for i in range(len(pept) + 1)]
    for i in range(len(pept)):
        masspreif[i + 1] = masspreif[i] + pept[i]
    for i in range(len(pept)):
        for j in range(i + 1, len(pept) + 1):
            linialspctrrr.append(masspreif[j] - masspreif[i])
    linialspctrrr.append(0)
    linialspctrrr = sorted(linialspctrrr)
    return linialspctrrr

if __name__ == '__main__':
    with open('pept.txt') as f:
        m = int(f.readline())
        n = int(f.readline())
        spectrr = list(map(int, f.readline().split()))
    print('-'.join([str(i) for i in secsycllconn(m, n, spectrr)]))