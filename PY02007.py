cou = 0
arr = []
while cou < 10:
    txt = [int(i) for i in input().split()]
    for i in txt:
        if (i % 42) not in arr:
            arr.append(i % 42)
        cou += 1
print(len(arr))
