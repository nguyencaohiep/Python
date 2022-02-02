class ThiSinh:
    def __init__(self, ma, hoTen, diemThi, danToc, khuVuc):
        self.ma = ma
        self.hoTen = hoTen
        self.diemThi = diemThi
        self.danToc = danToc
        self.khuVuc = khuVuc
        self.tongDiem = self.tinhDiem()

    def tinhDiem(self):
        diem = 0
        kv = self.khuVuc
        if kv == '1':
            diem += 1.5
        elif kv == '2':
            diem += 1
        else:
            diem += 0
        dt = self.danToc
        if dt != "Kinh":
            diem += 1.5
        return diem + self.diemThi

    def solve(self):
        diem = float("{:1f}".format(self.tongDiem))
        res = ""
        if diem < 20.5:
            res = "Truot"
        else:
            res = "Do"
        print(f"{self.ma} {self.hoTen} {diem} {res}")

t = int(input())
arr = []
for i in range(t):
    ten = input().lower().title().split()
    res = " ".join(ten)
    res.strip() 
    ma = "TS{:02d}".format(i + 1)
    arr.append(ThiSinh(ma, res, float(input()), input(), input()))

arr.sort(key = lambda x: -x.tongDiem)
for i in arr:
    i.solve()
