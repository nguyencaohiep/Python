# Read a string:
# s = input()
# Print a value:
# print(s)
n = int(input())
a = []
b = []
for i in range(n):
    txt = input().split()
    for j in txt:
        a.append(j)
        if(j not in b):
            b.append(j)
res = " "
cou = 0
b.sort()
for i in b:
    if(a.count(i) > cou):
        cou = a.count(i)
        res = i
print(res)        
