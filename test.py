t = int(input())

for i in range(t):
    n, m, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    x, y, z = 0, 0, 0
    check = False
    while x < n and y < m and z < k:
        if a[x] == b[y] and b[y] == c[z]:
            print(a[x], end=" ")
            check = True
            x += 1
            y += 1
            z += 1
        elif a[x] > b[y]:
            y += 1
        elif b[y] > c[z]:
            z += 1
        else:
            x += 1
    if not check:
        print("NO")
    print()
