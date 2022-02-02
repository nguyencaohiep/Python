import re
while True:
    try:
        s = input().strip()
        s = re.sub("\s+", " ", s)
        s = s.capitalize()
        if s[-1] != "." and s[-1] != "?" and s[-1] != "!": 
            s += "."
        if s[-2] == " ": 
            print(s[:-2]+s[-1])
        else: 
            print(s) 

    except EOFError: break