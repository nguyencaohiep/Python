class Subject:
    def __init__(self, ma, ten, hinhThucThi):
        self.ma = ma
        self.ten = ten
        self.hinhThucThi = hinhThucThi
    
    def display(self):
        print(f"{self.ma} {self.ten} {self.hinhThucThi}")

        
n = int(input())
a = []
for i in range(n):
    a.append(Subject(input(), input(), input()))

a.sort(key = lambda x: x.ma)
for i in a:
    i.display()

