n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
check = False
for i in range(n - 1):
    if (arr[i] + 1) != arr[i + 1]:
        check = True
        print(arr[i] + 1)
        break
if check == False:
    print(arr[n - 1] + 1)

