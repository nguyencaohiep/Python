n = (int)(input())
arr = 0 * n
txt = input()
arr = [int(i) for i in txt.split()]
cou = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if  (arr[i] > arr[j]):
            cou += 1
print(cou)
