import math
class HocSinh:
    def __init__(self, ma, ten, diemTB):
        self.ma = ma
        self.ten = ten
        self.diemTB = diemTB

    def display(self):
        xepLoai = ""
        diem = float("{:.1f}".format(round(self.diemTB, 1)))
        if diem >= 9:
            xepLoai = "XUAT SAC" 
        elif diem >= 8:
            xepLoai = "GIOI"
        elif diem >= 7:
            xepLoai = "KHA"
        elif diem >= 5:
            xepLoai = "TB"
        else:
            xepLoai = "YEU"
        print(f"{self.ma} {self.ten} {diem} {xepLoai}")

t = int(input())
hs = []
for i in range(t):
    ma = "HS{:02d}".format(i + 1)
    ten = input()
    diem = [float(i) for i in input().split()]
    tmp = (sum(diem) + diem[0] + diem[1]) / 10 / 1.2
    hs.append(HocSinh(ma, ten, tmp))

res = sorted(hs, key = lambda x: x.diemTB, reverse = True)

for k in res:
    k.display()
    
