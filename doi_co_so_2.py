t = int(input())

line = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def convert(n, m):
    res = ""
    while n > 0:
        t = n % m
        res += str(line[t])
        n //= m 
    return res[::-1]

for i in range(t):
    b = int(input())
    txt = input()
    if b == 2:
        print(txt)
    else:
        txt = int(txt,2)
        print(convert(txt, b))

    
