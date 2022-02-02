t = int(input())

def check(n):
    for i in range(len(n) - 1):
        if (n[i] == n[i+1]):
            return False
    return True

while t > 0:
    txt = input()
    a = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(txt)):
        a[int(txt[i])] = 1
    if(sum(a) > 2):
        print("NO")
    else:
        if check(txt):
            print("YES")
        else:
            print("NO")
    t -= 1