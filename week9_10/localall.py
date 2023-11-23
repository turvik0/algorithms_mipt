def localallighn(firstseq, secondseq, matt, straf):
	numlenfirst, numlensecond = len(firstseq), len(secondseq)
	s = [[0 for i in range(numlensecond + 1)] for j in range(numlenfirst + 1)]
	trcbc = [[0 for i in range(numlensecond + 1)] for j in range(numlenfirst + 1)]
	nummaxx = -1
	maxfirst, maxsecond = 0, 0
	for i in range(1, numlenfirst +1):
		for j in range(1, numlensecond+1):
			listnumm = [s[i-1][j] - straf, s[i][j-1] - straf, s[i-1][j-1] + matt[firstseq[i-1], secondseq[j-1]], 0]
			s[i][j] = max(listnumm)
			trcbc[i][j] = listnumm.index(s[i][j])
			if s[i][j] > nummaxx:
				nummaxx = s[i][j]
				maxfirst, maxsecond = i, j
	insertind = lambda seq, i: seq[:i] + '-' + seq[i:]
	a, b = maxfirst, maxsecond
	firstall, secondall = firstseq[:a], secondseq[:b]
	while trcbc[a][b] != 3 and a * b != 0:
		if trcbc[a][b] == 0:
			a -= 1
			secondall = insertind(secondall, b)
		elif trcbc[a][b] == 2:
			a -= 1
			b -= 1
		elif trcbc[a][b] == 1:
			b -= 1
			firstall = insertind(firstall, a)
	firstall = firstall[a:]
	secondall = secondall[b:]
	return str(nummaxx), firstall, secondall

if __name__ == '__main__':
	straf = 5
	with open('data.txt') as f:
		firstseq = f.readline().strip()
		secondseq = f.readline().strip()
	with open('newhelp.txt') as f1:
		lines = [line.strip().split() for line in f1.readlines()]
		matt = {(i[0], i[1]): int(i[2]) for i in lines}
	answerr = '\n'.join(localallighn(firstseq, secondseq, matt, straf))
	print(answerr)