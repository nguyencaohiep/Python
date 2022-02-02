t = (int)(input())

for i in range(t):
    n = (int)(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = [int(i) for i in input().split()]
    b.sort()
    result = True
    for i in range(n):
        if(a[i] > b[i]):
            result = False
            break
    if(result):
        print("YES")
    else:
        print("NO")
        
    