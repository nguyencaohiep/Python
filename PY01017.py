t = (int)(input())
for i in range(t):
    txt = input()
    result = ""
    ind = 0
    length = 0 
    for i in range(len(txt)):
        if (txt[i] != txt[i + 1]):
            length = i + 1 - ind
            ind = i + 1 
            result += (str)(length) + txt[i]
    result += (str)(len(txt) - ind) + txt[len(txt) - 1]
    print(result)
                
