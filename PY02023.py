def sum2(n):
    n = str(n)
    arr = [int(i) for i in n]
    return sum(arr)


t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    s = []
    for i in arr:
        tmp = sum2(i)
        if tmp not in s:
            s.append(tmp)
    s.sort()
    res = []
    for i in range(len(s)):
        for j in arr:
            if s[i] == sum2(j):
                res.append(j)
    for i in res:
        print(i, end= " ")                   
    print("")
    
