class nhanVien:
    def __init__(self, ma, hoTen, diemLT, diemTH):
        self.ma = ma 
        self.hoTen = hoTen
        self.diem = (diemLT + diemTH) / 2
    
    def display(self):
        d = self.diem
        res = ""
        if d < 5:
            res = "TRUOT"
        elif d < 8:
            res = "CAN NHAC"
        elif d < 9.5:
            res = "DAT"
        else:
            res = "XUAT SAC"
        diem = "%.2f"%(d)
        print(f"{self.ma} {self.hoTen} {diem} {res}")

        
def xuLiDiem(n):
    tmp = float(n)
    res = ""
    if tmp > 10:
        res = n[0:1] + "." + n[1:]
    else:
        res = n
    return res


t = int(input())
nv = []
for i in range(t):
    ten = input()
    diemLT = float(xuLiDiem(input()))
    diemTH = float(xuLiDiem(input()))
    ma = "TS{:02d}".format(i + 1)
    nv.append(nhanVien(ma, ten, diemLT, diemTH))

nv.sort(key = lambda x: -x.diem)

for i in nv:
    i.display()