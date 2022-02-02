n = int(input())
for j in range(n):
    n, t= [int(i) for i in input().split()]
    if t == 1:
        if n >= 20:
            print("Bao Binh")
        else:
            print("Ma Ket")
    elif t == 2:
        if n >= 19:
            print("Song Ngu")
        else:
            print("Bao Binh")
    elif t == 3:
        if n >= 21:
            print("Bach Duong")
        else:
            print("Song Ngu")
    elif t == 4:
        if n >= 20:
            print("Kim Nguu")
        else:
            print("Bach Duong")
    elif t == 5:
        if n >= 21:
            print("Song Tu")
        else:print("Kim Nguu")
    elif t == 6:
        if n >= 21:
            print("Cu Giai")
        else :
            print("Song Tu")
    elif t == 7:
        if n >= 23:
            print("Su Tu")
        else:
            print("Cu Giai")
    elif t == 8:
        if n >= 23:
            print("Xu Nu")
        else:print("Su Tu")

    elif t ==9:
        if n >= 23:
            print("Thien Binh")
        else:print("Xu Nu")
    elif t == 10:
        if n >= 23:
            print("Thien Yet")
        else:
            print("Thien Binh")
    elif t == 11:
        if n >= 23:
            print("Nhan Ma")
        else:
            print("Thien Yet")
    elif t == 12:
        if n >= 22:
            print("Ma Ket")
        else:print("Nhan Ma")