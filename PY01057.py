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

def check(n):
    for i in range(len(n)):
        if (prime(i) == True):
            if prime(n[i]) == False:
                return False
        if(prime(i) == False):
            if prime(n[i]) == True:
                return False
    return True


t = int(input())
for i in range(t):
    n = [int(i) for i in input()]
    if(check(n)):
        print("YES")
    else:
        print("NO")

