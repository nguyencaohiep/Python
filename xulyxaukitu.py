# s1 = input().lower().split()
# s2 = input().lower().split()

# hop = list(set(s1 + s2))

# hop.sort()
# s1 = list(set(s1))
# s1.sort()
# print(*hop)

# for i in s1:
#     if i in s2:
#         print(i, end = " ")

s1 = input().lower().split()
s2 = input().lower().split()
hop = set(s1+s2)
hop1 = []
for i in hop:
    hop1.append(i)
hop1.sort()
giao = []
for i in s1:
    if i in s2:
        giao.append(i)
giao.sort()
for i in hop1:
    print(i,end=" ")
print()
for i in giao:
    print(i,end=" ")
print()
