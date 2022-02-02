n = int(input())
arr = [[0] * n] * n
for i in range(n):
    arr[i] = [int(i) for i in input().split()]
res = [0] * n
if n == 2:
    res[1] = int(arr[0][1] / 2)
    res[0] = int(arr[0][1]) - res[1]
    for i in res:
        print(i, end = " ")
else:
    res[n-1] = (int)((arr[n - 3][n - 1] - arr[n - 3]
                    [n - 2] + arr[n - 2][n - 1]) / 2)
    for i in range(n - 1):
        res[i] = arr[i][n - 1] - res[n - 1]
    for i in res:
        print(i, end=" ")
