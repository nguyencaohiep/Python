t = (int)(input())
for i in range(t):
    n = (int)(input())
    txt = input()
    arr = [int(i) for i in txt.split()]
    arr.sort()
    cou = 0
    ind = 0
    tmp = 0
    # 2 2 3 3 3 4 4 4 4 4 
    for i in range(n - 1):
        if (arr[i] != arr[i + 1]):
            if ((i + 1 - tmp) > cou):
                cou = i + 1 - tmp
                ind = i 
            tmp = i + 1
    if (n - tmp > cou):
        cou = n - tmp
        ind = n - 1
    if cou > (int)( n / 2):
        print(arr[ind])
    else: 
        print("NO")

   