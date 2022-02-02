t = int(input())

for k in range(t):
    txt = [int(i) for i in input()]
    su = 0
    mul = 1
    i = 1
    while i < len(txt):
        su += txt[i]
        i += 2 
    j = 0
    have = False
    while j < len(txt):
        if txt[j] != 0:
            if txt[j] == 1:
                have = True
            mul *= txt[j]
        j += 2
    if ((have == False) & (mul == 1)):
        mul = 0
    print(mul, su)
    

