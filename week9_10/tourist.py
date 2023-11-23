def tourist(n, m, falsee, truee):
    listnum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): listnum[i][0] = listnum[i - 1][0] + falsee[i - 1][0]
    for j in range(1, m + 1): listnum[0][j] = listnum[0][j - 1] + truee[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            listnum[i][j] = max(listnum[i - 1][j] + falsee[i - 1][j], listnum[i][j - 1] + truee[i][j - 1])
    return listnum[n][m]

if __name__ == "__main__":
    with open('data.txt') as f:
        line = f.readline().strip().split()
        n = int(line[0])
        m = int(line[1])
        truee = []
        falsee = []
        for i in range(n):
            line = f.readline().strip().split()
            falsee.append([int(i) for i in line])
        f.readline()
        for i in range(n + 1):
            line = f.readline().strip().split()
            truee.append([int(i) for i in line])
    print(tourist(n, m, falsee, truee))