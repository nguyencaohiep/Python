n, m = [int(i) for i in input().split()]
a = []
b = []
for i in range(n):
    a.append([int(j) for j in input().split()])
    for v in a[i]:
        b.append(v)

lon = max(b)
nho = min(b)
dep = lon - nho

if b.count(dep) == 0:
    print("NOT FOUND")
else:
    print(dep)
    for i in range(n):
        for j in range(m):
            if a[i][j] == dep:
                print(f"Vi tri [{i}][{j}]")


