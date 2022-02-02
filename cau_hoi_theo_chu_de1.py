test = int(input())
count = -1
res =""
ok = False
for t in range(test):
    s = input()
    count += 1
    if s[-1:] != "?" and len(s) > 0 and ok == False:
        ok = True
        print(s.strip()+": ",sep="",end="")
    if len(s) == 0 or t == test-1:
        ok = False
        if t == test-1:
            print(count)
        else:
             print(count-1)
        count = -1