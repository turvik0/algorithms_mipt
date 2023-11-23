def countbal(adj_list):
    numbal = dict.fromkeys(adj_list.keys(), 0)
    for ij in adj_list.keys():
        for out in adj_list[ij]:
            numbal[ij] -= 1
            try:
                numbal[out] += 1
            except:
                numbal[out] = 1
    return numbal



def pattspelstr(patt, k):
    str = patt[0]
    for i in range(1, len(patt)):
        str += patt[i][-1]
    return str


def pairpref(pair):
    return (pair[0][:-1], pair[1][:-1])


def pairsuff(pair):
    return (pair[0][1:], pair[1][1:])

def patttogap(path, k, d):
    pattfir = [n for n, m in path]
    pattsec = [m for n, m in path]
    strsuff = pattspelstr(pattsec, k)
    strpref = pattspelstr(pattfir, k)
    for i in range((k + d + 1), len(strpref)):
        if strpref[i] != strsuff[i - k - d]:
            return "There is no string spelled by the gapped patterns"
    return strpref + strsuff[-k - d:]

def probleupath(dict):
    liststc = []
    numbal = countbal(dict)
    liststc.append([k for k, v in numbal.items() if v == -1][0])
    ret = []
    while liststc != []:
        univ = liststc[-1]
        try:
            w = dict[univ][0]
            liststc.append(w)
            dict[univ].remove(w)
        except:
            ret.append(liststc.pop())
    return ret[::-1]


def suff(string):
    return string[1:]


def prefix(string):
    return string[0:-1]

def pairtodeb(pairlist):
    pairlist = list(pairlist)
    ret = {}
    for i in pairlist:
        i = i.split('|')
        suff = pairsuff(i)
        prefix = pairpref(i)
        if prefix in ret.keys():
            ret[prefix].append(suff)
        else:
            ret[prefix] = [suff]
    return ret

if __name__ == "__main__":
    data = "".join(open('gapped.txt')).split()
    print(patttogap(probleupath(pairtodeb(data[2:])), int(data[0]),
                                            int(data[1])))