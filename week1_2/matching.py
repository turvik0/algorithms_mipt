def pos(sample, st, er):
    pos = []
    k = len(sample)
    for i in range(len(st)):
        key = "".join(st[i: i + k])
        if func(key, sample, er) == 1:
            pos.append(i)
    print(*pos)
def func(str, sample, er):
    if (len(str) != len(sample)):
        return 0
    numbers = 0
    for i in range(len(str)):
        if (str[i] != sample[i]):
            numbers += 1
        if numbers > er:
            return 0
    return 1
data ="".join(open('rosalind_ba1h.txt')).split()
pos(data[0], data[1], int(data[2]))