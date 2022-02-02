n = int(input())
a = []
for i in range(n):
    txt = [int(i) for i in input().split()]
    a.append(txt)

t1 = t2  = 0
for j in range(n):
    for i in range(n):
        if j < (n - i - 1):
            t1 += a[i][j]
        elif (n - i - 1) < j:
            t2 += a[i][j]

t1 = abs(t1 - t2)

k = int(input())
if(t1 <= k):
    print("YES")
else:
    print("NO")

print(t1)


# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9