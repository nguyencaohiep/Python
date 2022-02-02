t = int(input())

for i in range(t):
    tmp = input().split()
    res = ""
    i = 0
    while len(res) < 100 and i < len(tmp):
        res += tmp[i] + " "
        i += 1
    res = res.strip()
    if len(res) > 100:
        index = len(res) - 1
        while res[index] != " ":
            index -= 1
        res = res[0:index]
        print(res)
    else:
        print(res)

# cách 2
# n = int(input())
# for i in range(n):
#     s = input()
#     if len(s) <=100:
#         print(s)
#     else:
#         tmp = 0
#         for i in range(100,-1,-1):
#             if s[i]==' ':
#                 tmp = i
#                 break
#         print(s[0:tmp+1])
