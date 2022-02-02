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
    txt = input()
    tmp1, tmp2 = int(txt[0:3]), int(txt[(len(txt)-3):len(txt)])
    if(prime(tmp1) & prime(tmp2)):
        print("YES")
    else:
        print("NO")
