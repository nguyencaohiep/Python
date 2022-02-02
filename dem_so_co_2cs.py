txt = input()
if len(txt) % 2 != 0:
    txt = txt[:len(txt) - 1]
a = []
b = []
for i in range(0, len(txt), 2):
    s = txt[i:i+2]
    a.append(s)
    if s not in b:
        b.append(s)
for t in b:
    print(f"{t} {a.count(t)}")

