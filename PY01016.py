t = (int)(input())
for i in range(t):
    txt = input()
    result = ""
    for i in range(1,len(txt),2):
        for j in range((int)(txt[i])):
            result += txt[i - 1]
    print(result)