t = int(input())

for i in range(t):
    n = int(input())
    a = set([int(i) for i in input().split()])
    a = list(a)
    a.sort()
    print(a[-1] - a[0] + 1 - len(a))