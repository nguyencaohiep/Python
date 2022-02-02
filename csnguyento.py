import math
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

while t > 0:
    txt = input()
    t1 = t2 = 0
    if(prime(len(txt))):
        for i in range(len(txt)):
            if(prime(int(txt[i]))):
                t1 += 1
            else:
                t2 += 1
        if t1 > t2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t -= 1