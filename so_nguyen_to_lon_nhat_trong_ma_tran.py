a = [0]*100
a[0] = a[1] = 1
prime = []
for i in range(2, 100):
    if(a[i] == 0):
        prime.append(i)
        for j in range(i*2, 100,i):
            a[j] = 1
m,n = [int(i) for i in input().split()]
arr = [[0]*n]*m
maxValue = 1
for i in range(m):
    tmp = [int(j) for j in input().split()]
    arr[i] = tmp
    for t in arr[i]:
        if t in prime and t > maxValue:
            maxValue = t
if maxValue == 1:
    print("NOT FOUND")          
else:
    print(maxValue)  
    for i in range(m):
        for j in range(n):
            if arr[i][j] == maxValue:
                print(f"Vi tri [{i}][{j}]")


