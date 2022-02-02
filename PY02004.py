n = int(input())
arr = input().split()
cou = 0
for i in range(n - 1):
    if(arr[i] != arr[i+1]):
        cou += 1
print(cou)        
