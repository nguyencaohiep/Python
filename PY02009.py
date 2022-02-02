t = int(input())

for i in range(t):
    n = int(input())
    arr = [0] * 1001
    tmp = []
    for i in range(n):
        t1 = int(input())
        tmp.append(t)
        arr[t1] += 1
    print(arr.index(max(arr)))