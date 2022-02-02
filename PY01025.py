txt = input()
i = len(txt) - 1
res = ""
count = 0
while i >= 0:
    count += 1
    res = txt[i] + res
    if i == 0:
        break
    if count == 3:
        res = "," + res
        count = 0
    i -= 1
print(res)    
