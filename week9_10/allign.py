def allignmentt(firstseq, secondseq, matt, nnum):
    numlenfirst= len(firstseq)
    numlensecond = len(secondseq)
    listnum = [[0] * (numlensecond + 1) for _ in range(numlenfirst + 1)]
    trcbc = [[0] * (numlensecond + 1) for _ in range(numlenfirst + 1)]
    for i in range(1, numlenfirst + 1):
        listnum[i][0] = - i * nnum
    for j in range(1, numlensecond + 1):
        listnum[0][j] = - j * nnum
    for i in range(1, numlenfirst + 1):
        for j in range(1, numlensecond + 1):
            score_list = [listnum[i - 1][j] - nnum, listnum[i][j - 1] - nnum, listnum[i - 1][j - 1] + matt[firstseq[i - 1], secondseq[j - 1]]]
            listnum[i][j] = max(score_list)
            trcbc[i][j] = score_list.index(listnum[i][j])
    insertind = lambda seq, i: seq[:i] + '-' + seq[i:]
    firstall, secondall = firstseq, secondseq
    a, b = numlenfirst, numlensecond
    returnmax = str(listnum[a][b])
    while a * b != 0:
        if trcbc[a][b] == 0:
            a -= 1
            secondall = insertind(secondall, b)
        elif trcbc[a][b] == 1:
            b -= 1
            firstall = insertind(firstall, a)
        else:
            a -= 1
            b -= 1
    for i in range(a):
        secondall = insertind(secondall, 0)
    for j in range(b):
        firstall = insertind(firstall, 0)
    return returnmax, firstall, secondall
if __name__ == '__main__':
    straf = 5
    with open('data.txt') as f:
        firstseq = f.readline().strip()
        secondseq = f.readline().strip()
    with open('help.txt') as f1:
        lines = [line.strip().split() for line in f1.readlines()]
        matt = {(i[0], i[1]): int(i[2]) for i in lines}
    answerr = '\n'.join(allignmentt(firstseq, secondseq, matt, straf))
    print(answerr)