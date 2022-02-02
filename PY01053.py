t = int(input())

for i in range(t):
    txt = [int(i) for i in input()]
    if(sum(txt) % 3 == 0):
        print("YES")
    else:
        print("NO")
