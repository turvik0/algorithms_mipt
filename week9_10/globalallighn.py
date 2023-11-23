def multiple_lcs(strings):
    l1, l2, l3 = len(strings[0]), len(strings[1]), len(strings[2])
    score = [[[0 for _ in range(l3 + 1)] for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            for k in range(1, l3 + 1):
                if strings[0][i - 1] == strings[1][j - 1] and strings[0][i - 1] == strings[2][k - 1]:
                    score[i][j][k] = score[i - 1][j - 1][k - 1] + 1
                else:
                    score[i][j][k] = max(score[i - 1][j][k], score[i][j - 1][k], score[i][j][k - 1])

    alignments = ["", "", ""]
    i, j, k = l1, l2, l3
    while i > 0 or j > 0 or k > 0:
        if i > 0 and score[i][j][k] == score[i - 1][j][k]:
            alignments[0] += strings[0][i - 1]
            alignments[1] += '-'
            alignments[2] += '-'
            i -= 1
        elif j > 0 and score[i][j][k] == score[i][j - 1][k]:
            alignments[0] += '-'
            alignments[1] += strings[1][j - 1]
            alignments[2] += '-'
            j -= 1
        elif k > 0 and score[i][j][k] == score[i][j][k - 1]:
            alignments[0] += '-'
            alignments[1] += '-'
            alignments[2] += strings[2][k - 1]
            k -= 1
        else:
            alignments[0] += strings[0][i - 1]
            alignments[1] += strings[1][j - 1]
            alignments[2] += strings[2][k - 1]
            i -= 1
            j -= 1
            k -= 1

    alignments = [alignment[::-1] for alignment in alignments]
    return score[l1][l2][l3], alignments

if __name__ == '__main__':
    with open('data.txt') as f:
        firstseq = f.readline().strip()
        secondseq = f.readline().strip()
        thirdseq = f.readline().strip()
    strings = [firstseq, secondseq, thirdseq]
    score, alignment = multiple_lcs(strings)
    print(score)
    for a in alignment:
        print(a)
    