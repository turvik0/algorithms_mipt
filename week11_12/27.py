import numpy
def answerr(strng):
    checkk = 0
    for i in range(len(strng) - 1):
        if strng[i + 1] - strng[i] == 1:
            checkk += 1
    if strng[-1] == len(strng):
        checkk += 1
    if strng[0] == 1:
        checkk += 1
    return len(strng) + 1 - checkk

if __name__ == '__main__':
    with open('data.txt') as f:
        strng = f.readline().strip()
    strng = strng[1:-1].split()
    strng = [int(i) for i in strng]
    print(answerr(strng))