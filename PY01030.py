import math
n, k = input().split()
k = int(k)
ind = 0
if len(n) == k:
    ind = int(n)
else:
    ind = pow(10, (k)) 
cou = 0
for i in range(pow(10, (k - 1)), ind):
    if(math.gcd(int(n), i) == 1):
        print(i, end=" ")
        cou += 1
    if cou == 10:
        cou = 0
        print("")
