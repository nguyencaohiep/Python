in_put = input()
n, m = [int(i) for i in in_put.split()]
a = input()
arr_a = [int(i) for i in a.split()]
b = input()
arr_b = [int(i) for i in b.split()]
arr_a.sort()
arr_b.sort()
uni_a = []
uni_b = []
for i in arr_a:
    if i not in uni_a:
        uni_a.append(i)
for i in arr_b:
    if i not in uni_b:
        uni_b.append(i)
for i in uni_a:
    if i in uni_b:
        print(i, end = " ")
print()
for i in uni_a:
    if i not in uni_b:
        print(i, end = " ")
print()        
for i in uni_b:
    if i not in uni_a:
        print(i, end = " ")
print()        