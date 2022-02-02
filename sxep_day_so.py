t = int(input())

while t > 0:
    t -= 1
    q, n = [int(i) for i in input().split()]

    a = [int(i) for i in input().split()]
    m = max(a)
    ind = a.index(m)
    a.insert(ind, n)

    b = [0] * len(a)
    c = []
    d = []
    for i in range(len(a)):
        if a[i] < 0:
            b[i] = -1
            c.append(a[i])
        else:
            b[i] = 0
            d.append(a[i])
    ind1 = ind2 = 0
    b.sort()
    for i in b:
        if i < 0:
            print(c[ind1], end = " ")
            ind1 += 1
        else:
            print(d[ind2], end = " ")
            ind2 += 1
    print()







