a, k, n = [int(i) for i in input().split()]
have = False
b = k - a % k
while(a + b <= n):
    print(b, end=" ")
    b += k
    have = True
if not have:
    print(-1)
