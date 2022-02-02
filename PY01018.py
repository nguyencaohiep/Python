P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    str = input().split()
    k = int(str[0])
    if (k == 0):
        break
    else:
        txt = list(str[1])
        for i in range(len(txt)):
            ind = P.find(txt[i]) + k
            txt[i] = P[ind]
        txt = "".join(txt) 
        txt = txt[::-1]           
        print(txt)