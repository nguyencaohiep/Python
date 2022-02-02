def result(txt):
    a = [int(i) for i in txt]
    length = len(a)
    if (length == 1):
        return False
    if((a[0] == a[length - 2]) & (a[1] == a[length - 1])):
        return True
    else:
        return False

t = (int)(input())

for i in range(t):
    txt = input()
    if (result(txt) == True):
        print("YES")
    else:
        print("NO")
