a = [0] * 93
a[1] = 1
a[2] = 1
for i in range(3, 93):
    a[i] = a[i - 1] + a[i - 2]
t = (int)(input())
while t > 0:
    tmp = [(int)(i) for i in input().split()]
    b = tmp[0]
    c = tmp[1]
    for i in range(b, c + 1):
        print(a[i]," ")
    print("")
    t -= 1        
