import math
def gcd(a, b):
    if(b == 0):
        return a 
    return gcd(b,a % b)
    

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    k = 0
    for j in range(1, n):
        if(gcd(j, n) == 1):
            k += 1
    if(prime(k)):
        print("YES")
    else:
        print("NO")
