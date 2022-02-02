t = int(input())
c = 0
l7 = 0
line = []

for i in range(t):
    tmp = [str(i) for i in input().split()]
    line.append(len(tmp))

res = []
for i in range(len(line)):
    if line[i] == 6:
        continue
    elif line[i] == 8:
        if i == len(line) - 1 or line[i + 1] ==7:
            res.append(1)
            c += 1
    else:
        l7 += 1
        if l7 == 4:
            res.append(2)
            c += 1
            l7 = 0
print(c)
print(*res, sep ='\n')

# cách 2

# t = int(input())
# b = []
# id = 0
# dem = 0
# for i in range(t):
#     a = input().split()
#     if len(a) == 7 :
#         dem += 1
#         id = 2
#         if dem == 4:
#             b.append(id)
#             dem=0
#     if (len(a) == 6 or len(a) == 8 and id != 1:
#         id =1
#         b.append(id)
# print(len(b))
# print(*b,sep = "\n")

