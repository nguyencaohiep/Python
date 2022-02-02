from itertools import combinations
n, m = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]
a = set(a)
b = []
for i in a:
    b.append(i)
b.sort()

comb = combinations(b, m)

for i in comb:
    print(*i)



