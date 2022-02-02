from itertools import permutations

s = [''.join(o) for o in permutations(input())]

for i in s:
    print(i)