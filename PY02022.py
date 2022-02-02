import math
def prime(n):
    if n < 2:
        return False
    else:
        if n > 3:
            for i in range(2, (int)(math.sqrt(n) + 1)):
                if (n % i == 0):
                    return False
    return True

n = (int)(input())
arr = 0 * n
pri = []
txt = input()
arr = [int(i) for i in txt.split()]
for i in arr:
    if (prime(i) & (i not in pri)):
        pri.append(i)
for i in pri:
    cou = 0
    for j in arr:
        if i == j:
            cou += 1
    print(i, end = " ")
    print(cou)



