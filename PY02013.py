while True:
    n = int(input())
    if n == 0:
        break
    else:
        if n == 1:
            print(1)
        else:
            cou = 1
            while(n != 1):
                if n % 2 == 0:
                    n /= 2
                else:
                    n = n * 3 + 1
                cou += 1
            print(cou)
