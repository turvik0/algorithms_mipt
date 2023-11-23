import copy
def sortgrr(P):
    changess = []
    revdistt = 0
    for i in range(1, len(P) + 1):
        if P[i - 1] != i and P[i - 1] != -i:
            checkflag = 0
            if i in P:
                checkflag = P.index(i)
            elif -i in P:
                checkflag = P.index(-i)
            tem = P[i - 1:checkflag + 1]
            tem = [-k for k in tem]
            P[i - 1:checkflag + 1] = tem[::-1]
            changess.append(copy.copy(P))
            revdistt += 1
        if P[i - 1] == -i:
            P[i - 1] = i
            changess.append(copy.copy(P))
            revdistt += 1
    return revdistt, changess
if __name__ == '__main__':
    with open('data.txt') as f:
        P = f.readline().strip()
    P = P[1:-1].split()
    P = [int(i) for i in P]
    comm, changess = sortgrr(P)
    strng = ""
    file = open("output.txt", "w")
    for i in changess:
        additionalout = ['+' + str(chekk) if chekk > 0 else str(chekk) for chekk in i]
        file.write('(%s)' % ' '.join(additionalout) + "\n")
    file.close()