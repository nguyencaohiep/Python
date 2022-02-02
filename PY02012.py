n = (int)(input())
arr = []
while(len(arr) < n):
    tmp = [int(i) for i in input().split()]
    arr += tmp
ind = [0] * n#nếu vị trí đó là số chẵn thì ind là 0, lẻ thì ind là 1
even = []
odd = []
for i in range(n):
    if( arr[i] % 2 == 0):
        even.append(arr[i])
        ind[i] = 0
    else:
        odd.append(arr[i])
        ind[i] = 1
even.sort()# sắp xếp tăng dần
odd.sort()
odd = odd[::-1]#đảo ngược mảng số lẻ
i, j = 0, 0
for t in range(n):
    if(ind[t] == 0):
        print(even[i], end = " ")
        i += 1
    else:
        print(odd[j], end = " ")
        j += 1





    

