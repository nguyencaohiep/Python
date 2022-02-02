class Customer:
    def __init__(self, ma, ten, chiSoCu, chiSoMoi):
        self.ma = ma
        self.ten = ten
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi
    
    def tinhTien(self):
        luongNuoc = self.chiSoMoi - self.chiSoCu
        if luongNuoc <= 50:
            return (luongNuoc * 100)*(1 + 2 / 100)
        elif luongNuoc >= 51 and luongNuoc <= 100:
            return (50 * 100 + (luongNuoc - 50) * 150)*(1 + 3 / 100)
        return (50 * 250 + (luongNuoc - 100 ) * 200)*(1 + 5 / 100)
        

    def display(self):
        print(f"{self.ma} {self.ten} {round(self.tinhTien())}")

t = int(input())
arr = []
for i in range(t):
    ma = "KH{:02d}".format(i+1)
    arr.append(Customer(ma, input(), int(input()), int(input())))

arr.sort(key = lambda x : -x.tinhTien())
for i in arr:
    i.display()


