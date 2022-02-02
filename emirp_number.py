def prime(n):
    if n < 2: 
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

t = int(input())

while t > 0:
    n = int(input())
    a = [0]*n
    for i in range(13,n,2):
        if a[i] == 0:
            if int(str(i)[::-1]) < n:
                if prime(i) and prime(int(str(i)[::-1])) and str(i) != str(i)[::-1]:
                    a[i] = a[int(str(i)[::-1])] = 1
                    print(f"{i} {str(i)[::-1]}",end = " ")
    print()
    t -= 1

