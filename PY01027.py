def check1(txt):
    a = [int(i) for i in txt]
    for i in a:
        if ((i != 6) & (i != 8)):
            return False
    return True
def check2(txt):
    a = [int(i) for i in txt]
    for i in range(len(a)):
        if(a[0] == 8):
            return False
        if((a[i] == 8) & (a[i - 1] != 6) & (a[i - 1] !=8)):
            return False
        if( (i > 1) & (a[i] == 8) & (a[i - 1] == 8) & (a[i - 2] != 6)):
            return False
    return True            
txt = input()
if (check1(txt) == True):
    if(check2(txt) == True):
        print("YES")
    else:
        print("NO")
else:
    print("NO")

