t = int(input())
for i in range(t):
    txt = input()
    result = True
    for i in range(len(txt)):
        tmp = int(txt[i])
        if((tmp != 4) & (tmp != 7)):
            result = False
            break
    if(result):
        print("YES")
    else:
        print("NO")