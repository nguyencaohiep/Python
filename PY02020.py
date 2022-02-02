n = int(input())
arr = [float(i) for i in input().split()]
arr.sort()
tmp1 = arr[0]
tmp2 = arr[len(arr) - 1]
tmp = []
for i in arr:
    if (i != tmp1) & (i != tmp2):
        tmp.append(i)
res = round((sum(tmp) / len(tmp)), 2)
res = str(res)
cnt = 0
for x in range(len(res)):
    if x > res.index('.'):
        cnt += 1
res += '0' * (2 - cnt)
print(res)
