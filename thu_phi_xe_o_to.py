def solve(loai, huong):
    if huong == "IN":
        if loai == "Xe_con5":
            return 10000
        elif loai == "Xe_con7":
            return 15000
        elif loai == "Xe_tai2":
            return 20000
        elif loai == "Xe_khach29":
            return 50000
        else:
            return 70000
    return  0

res = {}

t = int(input())

for i in range(t):
    data = input().split(" ")
    if data[-1] in res:
        res[data[-1]] += solve(data[1] + data[2], data[3])
    else:
        res[data[-1]] = solve(data[1] + data[2], data[3])

for i in res:
    print(f"{i}: {res[i]}")

