t = int(input())

while t > 0:
    n = input()
    step = 0
    s = int(n)
    have = False
    if s % 7 == 0:
        print(s)
    else:
        while step < 1000:
            s = int(n) + int(n[::-1])
            if s % 7 == 0:
                print(s)
                have = True
                break
            n = str(s)
            step += 1

        if not have:
            print(-1)
    t -= 1