while True:
    arr = [0] * 4
    str = input()
    arr = [int(i) for i in str.split()]
    if(sum(arr) == 0):
        break
    else:
        step = 0
        while ((arr[0] != arr[1]) or (arr[1] != arr[2]) or (arr[2] != arr[3])):
            tmp = arr[0]
            for i in range(3):
                arr[i] = abs(arr[i] - arr[i + 1])
            arr[3] = abs(arr[3] - tmp)
            step += 1
        print(step)