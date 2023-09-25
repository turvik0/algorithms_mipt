data = open('rosalind_ba1f.txt', 'r')
skew = []
st = data.read()
pos = 0
for i in st:
    if i == 'C':
        pos += -1
    elif i =='G':
        pos += 1
    skew.append(pos)
endst = []
min = min(skew)
for i in range(len(skew)):
    if skew[i] == min:
        endst.append(i+1)
print(*endst)