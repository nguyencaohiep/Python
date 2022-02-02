import math

tmp = [int(i) for i in input().split()]
n = tmp[0]
m = tmp[1]
mat = []
res = []

for i in range(n):
    temp = input()
    mat.insert(i, temp)
    mat[i] = mat[i].split()
    for j in mat[i]:
        res.append(int(j))
max = max(res) - min(res)


if res.count(max) == 0:
    print("NOT FOUND")
else:
    print(max)
    for i in range(n):
        for j in range(m):
            if int(mat[i][j]) == max:
                print("Vi tri ", "[", i, "]", "[", j, "]",sep="")
