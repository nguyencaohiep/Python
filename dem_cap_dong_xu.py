n = int(input())

a = [[0]*101]*101

for i in range(n):
    a[i] = input()
# print(a[1][3])
CountPairCoin = 0
for i in range(n):
    Coin = 0
    for j in range(len(a[i])):
        if a[i][j] == 'C':
            Coin += 1
    CountPairCoin += Coin*(Coin - 1) // 2

for i in range(n):
    Coin = 0
    for j in range(len(a[i])):
        if a[j][i] == 'C':
            Coin += 1
    CountPairCoin += Coin*(Coin - 1) // 2

print(CountPairCoin)