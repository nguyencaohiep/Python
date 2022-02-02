txt = [str(i) for i in input()]# convert input from text to list
lower = 0
upper = 0
for i in range(len(txt)):
    if(txt[i].isupper()):
        upper += 1
    else:
        lower += 1
txt = "".join([str(i) for i in txt])# convert list to str
if(upper > lower):
    print(txt.upper())
else:
    print(txt.lower())
