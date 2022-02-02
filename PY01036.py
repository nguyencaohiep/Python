t = int(input())

for i in range(t):
    n = int(input())
    i = 1
    if n % 2 == 0:
        i = 2
    su = 0
    for j in range(i, (n + 1), 2):
        su += 1/j
    su = str(round(su, 6))
    ind = su.find('.')
    for t in range(6 - len(su[(ind+1):])):
        su += "0"
    print(su)        
