t = int(input())
for i in range(t):
    n , x, m = [float(i) for i in input().split()]
    cou = 0
    while n < m:
        n = n + n * x / 100
        cou += 1
    print(cou)