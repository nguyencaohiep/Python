a = (int)(input())

for i in range(a):
    s = input()
    arr = [int(i) for i in s]
    for i in range(len(arr) - 1):
        result = True
        if(arr[i] > arr[i + 1]):
            result = False
            break
    if result == False:
        print("NO")
    else:
        print("YES")
