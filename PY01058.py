import math
def prime(n):
    if n < 2:
        return False
    else:
        if n > 3:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
    return True
t = int(input())

for i in range(t):
    n = input()
    n = int(n[(len(n) - 4):len(n)])
    if prime(n):
        print("YES")
    else:
        print("NO")
    
