class Gamer:
    def __init__(self, ma, ten, tgian):
        self.ma = ma
        self.ten = ten
        self.tgian = tgian

    def solve(self):
        gio  = self.tgian // 60
        phut = self.tgian % 60 
        print(f"{self.ma}  {self.ten} {gio} gio {phut} phut")

t = int(input())        
a = []
for i in range(t):
    ma = input()
    ten = input()
    tgianvao = input().split(":")
    tgianra = input().split(":")
    tgian = int(tgianra[0]) * 60 + int(tgianra[1]) - (int(tgianvao[0]) * 60 + int(tgianvao[1]))
    gamer  = Gamer(ma, ten, tgian)
    a.append(gamer)

a.sort(key = lambda x: x.tgian, reverse=True)
for i in a:
    i.solve()
        
