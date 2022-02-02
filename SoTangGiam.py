t = int(input())

def check(n):
    index = 0
    for i in range(len(n)  - 1):
        if int(n[i]) > int(n[i+1]):
            index = i
            break
        if int(n[i]) == int(n[i+1]):
            return False
    for i in range(index, len(n) - 1):
        if int(n[i]) <= int(n[i + 1]):
            return False
    return True

while t > 0:
    txt = input()
    if len(txt) > 3:
        if check(txt):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    t -= 1