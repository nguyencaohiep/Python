import math

col = row = 20
arr = [[0] * col] * row

def prime(n):
    if n < 2:
        return False
    else:
        if n > 3:
            for i in range(2, int(math.sqrt(n) + 1)):
                if n % i == 0:
                    return False
    return True

m, n = [int(i) for i in input().split()] 
for i in range(m):
    a = input()
    arr[i] = [int(i) for i in a.split()]
    for j in range(n):
        if prime(arr[i][j]):
            arr[i][j] = 1
        else:
            arr[i][j] = 0
for i in range(m):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()
            