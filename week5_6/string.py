def getnumbalance(adj_list):
    numbalance = dict.fromkeys(adj_list.keys(), 0)
    for node in adj_list.keys():
        for out in adj_list[node]:
            numbalance[node] -= 1
            try:
                numbalance[out] += 1
            except:
                numbalance[out] = 1
    return numbalance

def recprobl(patt):
    return problgenp(problgeupath(kmertodebgr(patt)))

def problgenp(kmers, flag=True):
    gen = ''
    for i in kmers:
        gen += i[0]
    if flag:
        gen += i[1:]
    return gen

def problgeupath(dict):
    liststc=[]
    numbalance = getnumbalance(dict)
    liststc.append([k for k, v in numbalance.items() if v==-1][0])
    returnlistpath = []
    while liststc != []:
        u_v = liststc[-1]
        try:
            w = dict[u_v][0]
            liststc.append(w)
            dict[u_v].remove(w)
        except:
            returnlistpath.append(liststc.pop())
    return returnlistpath[::-1]

def kmertodebgr(patt):
    kmers = list()
    for i in patt:
        kmers = kmers + compossuff(len(i), i, uniq=True)
    kmers = set(kmers)
    returndict = {}
    for j in kmers:
        returndict[j] = []
    for i in patt:
        returndict[prefix(i)].append(suff(i))
    return returndict

def compossuff(k, text, uniq=False):
    kmers = []
    for i in range(len(text)+1-k):
        kmers.append(text[i:i+k-1])
    if uniq:
        return sorted(list(kmers))
    else:
        return sorted(kmers)

def prefix(string):
    return string[0:-1]

def suff(string):
    return string[1:]


if __name__ == "__main__":
    data = "".join(open('string.txt')).split()
    print(recprobl(data[1:]))