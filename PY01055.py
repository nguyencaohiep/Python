def check_ind(n):
    n = [int(i) for i in n]
    for i in range(0, len(n) - 2, 2):
        if n[i] != n[i + 2]:
            return False
    return True

t = int(input())

for i in range(t):
    n = input()
    if (len(n) % 2 != 0):
        if(n[0] != n[1]):
            if(check_ind(n)):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
