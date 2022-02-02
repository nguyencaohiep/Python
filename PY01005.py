n = input()
cou = 0
for i in range(len(n)):
    if((int(n[i]) == 4) or ( int(n[i]) == 7)):
        cou += 1
if((cou == 4) or (cou == 7)):
    print("YES")
else:
    print("NO")
