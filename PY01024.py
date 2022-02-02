import math


def check(arr):
    for i in range(len(arr) - 1):
        if(abs(arr[i] - arr[i+1]) != 2):
            return False
    return True

t = int(input())

for i in range(t):
    arr = [int(i) for i in input()]
    if(sum(arr) % 10 ==0):
        if(check(arr)):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

