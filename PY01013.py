import math
def gcd(a, b):
    while (a != 0) & (b != 0):
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def prime(n):
    if n < 2:
        return False
    else:
        if n > 3:
            for i in range(2, int(math.sqrt(n) + 1)):
                if n % i == 0:
                    return False
    return True

t = int(input())
for i in range(t):
    a, b = [int(i) for i in input().split()]
    tmp = gcd(a, b)
    result = 0
    while tmp > 0:
        result += tmp % 10
        tmp = tmp // 10
    if(prime(result)):
        print("YES")
    else:
        print("NO")

