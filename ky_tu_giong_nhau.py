def solve(n, x, y, z): # x, y, z : insert,delete,copy
    if n == 0:
        return 0
    if n == 1:
        return x
    dp = [0] * (n + 1) # dp[i] la tgian toi uu de có duoc chuoi o vi tri i

    dp[1] = x 

    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + x, dp[i // 2] + z)
        else:
            dp[i] = min(dp[i - 1 ] + x, dp[(i+1) // 2] + z + y)

    return dp[n]

t = int(input())

for i in range(t):
    n = int(input())
    x, y, z = [int(j) for j in input().split()]
    print(solve(n, x, y, z))
