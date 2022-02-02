import math

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+ 1):
            if n % i == 0:
                return False
        return True

        
t = int(input())
while t > 0:
    a = int(input()[-4:])
    if prime(a): print("YES")
    else: print("NO")
    t -= 1