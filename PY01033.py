import math

a, b = [int(i) for i in input().split()]
for i in range(a, b - 1):
    for j in range(i + 1, b):
        for t in range(j + 1, b + 1):
            if(math.gcd(i,j) == 1) & (math.gcd(j,t) == 1) & (math.gcd(i,t) == 1):
                print(f"({i}, {j}, {t})",)
