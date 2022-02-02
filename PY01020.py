t = (int)(input())

for i in range(t):
    n = input()
    if (n[len(n) - 1] != '6') or (n[len(n) - 2] != '8'):
        print("NO")
    else:
        print("YES")

