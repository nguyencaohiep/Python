t = int(input())

for i in range(t):
    txt = [str(i) for i in input()]
    txt.sort()
    su = 0
    res = ""
    for i in txt:
        if i.isnumeric():
            su += int(i)
        else:
            res += i
    res += str(su)
    print(str(res))