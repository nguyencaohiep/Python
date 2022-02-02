t = int(input())

def check(t):
    for i in range(len(t)):
        if int(t[i]) % 2 != 0:
            return False
    return True
            
while t > 0:
    n = int(input())
    for i in range(22,n,22):
        tmp = str(i)
        if(len(tmp) % 2 == 0):
            if(tmp == tmp[::-1]):
                if(check(tmp)):
                    print(i, end = " ")
    print("")
    t -= 1