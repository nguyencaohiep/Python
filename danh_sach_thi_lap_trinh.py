class Team:
    def __init__(self, ma, ten, tenTruong):
        self.ma = ma
        self.ten = ten
        self.tenTruong = tenTruong
    def display(self):
        print(f"{self.ten} {self.tenTruong}")

class HocSinh:
    def __init__(self, ma, ten, maTeam):
        self.ma = ma
        self.ten = ten
        self.maTeam = maTeam

    def display(self):
        print(f"{self.ma} {self.ten}", end = " ")


t = int(input())
team = {}
for i in range(t):
    ma = "Team{:02d}".format(i + 1)
    team[ma] = Team(ma, input(), input())

hs = {}
t = int(input())
for i in range(t):
    ma = "C{:03}".format(i + 1)
    hs[ma] = HocSinh(ma, input(), input())

hs = sorted(hs.items(), key = lambda x : x[1].ten)

for k, v in hs:
    v.display()
    team[v.maTeam].display()

        
        