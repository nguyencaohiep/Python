# s = [int(i) for i in input().split()]
# for i in range(len(s)):
#     s[i] = s[i] ** 2
# s.sort(reverse = True)
# print(s)

s1 = [1,2,3,4,3,2,1]
tmp = []
for i in s1:
    if i not in tmp:
        tmp.append(i)
print(len(tmp))    