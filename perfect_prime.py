
def check2(n):
    s = 0
    for i in range(len(n)):
        if not prime(int(n[i])):
            return False
        s += int(n[i])
    if prime(s):
        return True
    return False

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

t = int(input())

while t > 0:
    n = int(input())
    
    if prime(n):
        if prime(int(str(n)[::-1])):
            if check2(str(n)):
                print("Yes")
            else: 
                print("No")
        else:
            print("No")
    else: print("No")
    t -= 1