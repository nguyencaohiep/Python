import math
n = (int)(input())
arr = [[0] * n] * n
if ( n == 1):
    print(0)
else:
    col = [0] * n
    row = [0] * n
    for i in range(n):
        txt = input()
        for j in range(len(txt)):
            if (txt[j] == 'C'):
                row[i] += 1
                col[j] += 1
    result = 0
    for i in range(n):
        if (col[i] >= 2):
            result += math.comb(col[i],2)# math.comb(n,k) tính tổ hợp chập k của n
    for i in range(n):
        if (row[i] >= 2):
            result += math.comb(row[i],2)
    print(result)
