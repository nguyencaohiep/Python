import math


def prime(n):
    n = sum([int(i) for i in n])
    if n < 2:
        return False
    else:
        if n > 3:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
    return True


def even_odd(n):
    n = [int(i) for i in n]
    for i in range(len(n)):
        if (i % 2 == 0) & (n[i] % 2 != 0):
            return False
        if (i % 2 != 0) & (n[i] % 2 == 0):
            return False
    return True


t = int(input())

for i in range(t):
    n = input()
    if (prime(n) == True & even_odd(n) == True):
        print("YES")
    else:
        print("NO")
