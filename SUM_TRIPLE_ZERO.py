from itertools import combinations
t = int(input())
for x in range(t):
    m = int(input())
    a = [int(i) for i in input().split()]
    comb = combinations(a, 3)
    c = 0
    for i in comb:
        if sum(i) == 0:
            c += 1
    print(c)
            
