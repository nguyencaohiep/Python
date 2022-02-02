def solve(s):
    if len(s) == 0: return 
    s = " ".join(s.split())

    print(s.capitalize().strip())

s = ""
while True:
    try:
        s += input().lower()+""
    except EOFError: break
s = s.replace("!", ".")
s = s.replace("?", ".")
for i in s.split("."):
    solve(i)
