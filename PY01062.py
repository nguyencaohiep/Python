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
    txt = [int(i) for i in input()]
    cou = 0
    for i in txt:
        if prime(int(i)):
            cou += 1
    l = len(txt)
    if (prime(l) & ( cou > l - cou)):
        print("YES")
    else:
        print("NO")



