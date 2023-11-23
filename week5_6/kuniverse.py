import itertools
def compossuff(k, text, uniq=False):
    kmers = []
    for i in range(len(text)+1-k):
        kmers.append(text[i:i+k-1])
    if uniq:
        return sorted(list(kmers))
    else:
        return sorted(kmers)

def probleucirc(dict):
    liststc = []
    vertrand = sorted(dict.keys())[0]
    liststc.append(vertrand)
    returnlist = []
    while liststc != []:
        univ = liststc[-1]
        try:
            w = dict[univ][0]
            liststc.append(w)
            dict[univ].remove(w)
        except:
            returnlist.append(liststc.pop())
    return returnlist[::-1]
def kuniverse(k):
    circle = probleucirc(kmertodebgraph(stringbin(k)))
    circle = circle[:-(k-1)]
    gen = circle[0][:-1]
    for i in circle:
        gen += i[-1]
    return gen

def kmertodebgraph(patt):
    kmers = list()
    for i in patt:
        kmers = kmers+compossuff(len(i), i, uniq=True)
    kmers = set(kmers)
    dict = {}
    for i in kmers:
        dict[i] = []
    for i in patt:
        dict[prefix(i)].append(suff(i))
    return dict

def suff(string):
    return string[1:]


def prefix(string):
    return string[0:-1]

def stringbin(k):
    universe = ["0", "1"]
    kmers = ["".join(el) for el in itertools.product(universe, repeat=k)]
    return sorted(kmers)

if __name__ == "__main__":
    data = "".join(open('kuniverse.txt')).split()
    print(data)
    print(kuniverse(int(data[0])))