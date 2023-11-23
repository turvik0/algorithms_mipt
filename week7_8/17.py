def peptnumm(m):
    numm = 0
    for i in amkisl:
        if (m - dictamm[i]) in dctmss.keys():
            numm += dctmss[(m - dictamm[i])]
        elif m - dictamm[i] < 0:
            break
        elif m - dictamm[i] > 0:
            numm += peptnumm(m - dictamm[i])
        elif m - dictamm[i] == 0:
            numm += 1
            return numm
    dctmss[m] = numm
    return numm


if __name__ == '__main__':
    m = int("".join(open('pept.txt')))
    dictamm = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, \
                  'N': 114, 'D': 115, 'K': 128, 'E': 129, 'M': 131, \
                  'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    dctmss = {}
    amkisl = list(dictamm.keys())
    ans_num = peptnumm(m)
    amkisl_mass = list(dictamm.values())
    print(ans_num)