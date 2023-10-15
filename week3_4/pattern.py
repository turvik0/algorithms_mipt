def pattern(patt, dna):
    n = len(patt)
    leng = 0
    for word in dna:
        lenham = float("inf")
        #==
        for i in range(len(word) - n + 1):
            if lenham > dist_ham(patt, word[i:i + n]):
                lenham = dist_ham(patt, word[i:i + n])
        leng = leng + lenham
    return leng


def dist_ham(str1, str2):
    num = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            num += 1
    return num
#==
if __name__ == "__main__":
    data = "".join(open('pattern.txt')).split()
    leng = pattern(data[0], data[1:])
    print(leng)