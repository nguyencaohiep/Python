import math


def prime(n):
    if n < 2:
        return False
    else:
        if n > 3:
            for i in range(2, int(math.sqrt(n) + 1)):
                if n % i == 0:
                    return False
    return True


n = int(input())
arr = [int(i) for i in input().split()]
uni = []
for i in arr:
    if prime(i):
        uni.append(i)
uni.sort()
ind = 0
for i in arr:
    if prime(i):
        print(uni[ind], end = " ")
        ind += 1
    else:
        print(i, end = " ")
print("")        
