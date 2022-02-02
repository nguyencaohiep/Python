n = int(input())
a = []
while True:
    try:
        tmp = [int(i) for i in input().split()]
        a += tmp
    except EOFError:
        break
    
odd = []
even = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd.sort()
even.sort()
c = 0
l = len(odd) - 1
for i in a:
    if i % 2 == 0:
        print(even[c], end = " ")
        c += 1
    else:
        print(odd[l], end = " ")
        l -= 1
print()


