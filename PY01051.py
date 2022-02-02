def check(n):
    string  = str(n)
    if n < 11:
        return False
    else:
        if string != str(n)[::-1]:
            return False
    return True

t = int(input())

for i in range(t):
    n = sum([int(i) for i in input()])
    if(check(n)):
        print("YES")
    else:
        print("NO")


