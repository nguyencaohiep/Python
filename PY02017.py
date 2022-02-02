t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    tmp = set(arr)
    for i in tmp:
        if(arr.count(i) % 2 == 1):
            print(i)
            break