t = int(input())

for i in range(t):
    arr = [int(i) for i in input()]
    res = 1
    for i in arr:
        if (i != 0) & (i != 1):
            res *= i
    print(res)