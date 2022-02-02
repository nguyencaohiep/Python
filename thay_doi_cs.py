t = int(input())

for i in range(t):
    p, q = [str(i) for i in input().split()]
    if (int(p) > int(q)):
        t = q
        q = p
        p = t
    x1 = input()
    x2 = input()
    m = x1.replace(q, p)
    n = x2.replace(q, p)
    print(int(m) + int(n), end = " ")
    m = x1.replace(p, q)
    n = x2.replace(p, q)
    print(int(m) + int(n))
