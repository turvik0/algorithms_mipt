import itertools
from collections import Counter

def fr(st, k):
    key = []
    for i in range(len(st)):
        word = "".join(st[i: i + k])
        if len(word) == k:
            key.append(word)
    return Counter(key).most_common()

def clump_problem(st, k, L, t):
    key = []
    for i in range(len(st)):
        sts1 = st[i:i + L]
        if len(sts1) == L:
            key.append(fr(sts1, k))
    sample = list(itertools.chain(*key))
    print(*set([x[0] for x in sample if x[1] >= t]))

data = "".join(open('rosalind_ba1e.txt')).split()
clump_problem(data[0], int(data[1]), int(data[2]), int(data[3]))