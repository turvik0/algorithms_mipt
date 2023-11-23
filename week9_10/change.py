import numpy as np
import sys
def resoutput(M, inpp):
    currentone = ""
    realssum = []
    for j in range(len(inpp)):
        if(inpp[j] == ","):
            realssum.append(int(currentone))
            currentone = ""
        else:
            currentone += inpp[j]
    realssum.append(int(currentone))
    res = numcoiins(M, realssum)
    print(res)
def numcoiins(M, sumcoin):
    allnum = np.zeros(M)
    for i in sumcoin:
        if (i <= M):
            allnum[i - 1] = 1
    for m in range(1, M + 1):
        nummminimum = sys.maxsize
        if (m not in sumcoin):
            for i in sumcoin:
                if (m - i >= 0):
                    if (allnum[m - i - 1] + 1 < nummminimum):
                        nummminimum = allnum[m - i - 1] + 1
            allnum[m - 1] = nummminimum
    result = allnum[M - 1]
    return int(result)
if __name__ == '__main__':
    data = "".join(open('data.txt')).split()
    M = int(data[0])
    sumcoin = data[1]
    resoutput(M, sumcoin)