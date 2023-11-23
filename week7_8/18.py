def spectrrcycle(pept, tablaminac):
    prefix_mass = [0 for i in range(len(pept) + 1)]
    for i in range(len(pept)):
        prefix_mass[i + 1] = prefix_mass[i] + tablaminac[pept[i]]
    peptMass = prefix_mass[len(pept)]
    cycl_spectrr = []
    for i in range(len(pept)):
        for j in range(i + 1, len(pept) + 1):
            cycl_spectrr.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(pept):
                cycl_spectrr.append(peptMass - (prefix_mass[j] - prefix_mass[i]))
    cycl_spectrr.append(0)
    cycl_spectrr = sorted(cycl_spectrr)
    return cycl_spectrr

def secsycll(spectrr):
    peptsfinn = []
    peptstosee = ['']
    while peptstosee:
        minus = []
        peptstosee = expepetss(peptstosee)
        for i in range(len(peptstosee)):
            pept = peptstosee[i]
            if massppt(pept) == max(spectrr):
                if spectrrcycle(pept, tablaminac) == spectrr:
                    peptsfinn.append(pept)
                    minus.append(pept)
            elif not consistent(pept, spectrr):
                minus.append(pept)
        for i in range(len(minus)):
            peptstosee.remove(minus[i])
    pptfinmass = []
    for pept in peptsfinn:
        peeptmass = []
        for i in range(len(pept)):
            peeptmass.append(tablaminac[pept[i]])
        pptfinmass.append('-'.join(str(i) for i in peeptmass))
    return ' '.join(str(i) for i in pptfinmass)


def expepetss(pepts):
    peptsnew = []
    for i in pepts:
        for key in tablaminac:
            peptsnew.append(i + key)
    return peptsnew

def consistent(pept, spectrr):
    linialspctrrr = spectrrlin(pept)
    for s in linialspctrrr:
        if linialspctrrr.count(s) > spectrr.count(s):
            return False
    return True

def spectrrlin(pept):
    prefix_mass = [0 for i in range(len(pept) + 1)]
    for i in range(len(pept)):
        prefix_mass[i + 1] = prefix_mass[i] + tablaminac[pept[i]]
    linialspctrrr = []
    for i in range(len(pept)):
        for j in range(i + 1, len(pept) + 1):
            linialspctrrr.append(prefix_mass[j] - prefix_mass[i])
    linialspctrrr.append(0)
    linialspctrrr = sorted(linialspctrrr)
    return linialspctrrr

def massppt(pept):
    mass = 0
    for i in range(len(pept)):
        mass += tablaminac[pept[i]]
    return mass

if __name__ == '__main__':
    spectrr = list(map(int, open('pept.txt').readline().split()))
    tablaminac = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113,
                             'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156,
                             'Y': 163, 'W': 186}
    amino = list(tablaminac.keys())
    amino_mass = list(tablaminac.values())
    print(*set(list(secsycll(spectrr).split())))