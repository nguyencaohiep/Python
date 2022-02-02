t = int(input())

while t > 0:
    n = int(input())
    print("1", end = " ")
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            print(f" * {i}^{count}", end = " ")
    if n > 1:
        print("* " + str(n) + "^1")
    print()
    t -= 1
