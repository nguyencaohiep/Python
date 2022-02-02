class Tram:
    def __init__(self, ma, ten, tgian, luongMua):
        self.ma = ma
        self.ten = ten
        self.tgian = tgian
        self.luongMua = luongMua

    def getTen(self):
        return self.ten

    def solve(self):
        res = self.luongMua / self.tgian
        res = "{:.2f}".format(res)
        print(f"{self.ma} {self.ten} {res}")

t = int(input())
name = []
dic = {}
for i in range(t):
    ten = input()
    if ten not in name:
        name.append(ten)
        ma = "T{:02d}".format(i + 1)
        tmp = input().split(":") + input().split(":")
        tgian = (int(tmp[2]) * 60 + int(tmp[3]) - (int(tmp[0]) * 60 + int(tmp[1]))) / 60
        luongMua = int(input())
        tram = Tram(ma, ten, tgian, luongMua)
        dic[ten] = tram
    else:
        tram = dic[ten]
        tmp = input().split(":") + input().split(":")
        time = (int(tmp[2]) * 60 + int(tmp[3]) - (int(tmp[0]) * 60 + int(tmp[1]))) / 60
        lm = int(input())
        tram.tgian += time
        tram.luongMua += lm
for i in name:
    for j in dic:
        if i == j:
            dic[j].solve()

