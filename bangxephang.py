class SinhVien:
    def __init__(self, hoTen, soBaiLamDung, soSub):
        self.hoTen = hoTen
        self.soBaiLamDung = soBaiLamDung
        self.soSub = soSub

    def display(self):
        print(f"{self.hoTen} {self.soBaiLamDung} {self.soSub}")

t = int(input())
sv = []
for i in range(t):
    ten = input() 
    a = [int(i) for i in input().split()]
    sv.append(SinhVien(ten, a[0], a[1]))

sv.sort(key = lambda x: (-x.soBaiLamDung, x.soSub, x.hoTen))
for i in sv:
    i.display()



