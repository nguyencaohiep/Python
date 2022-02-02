import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        t1 = self.x - p2.x
        t2 = self.y - p2.y
        return math.sqrt(t1*t1+t2*t2)
        

t = int(input())

while t > 0:
    data = [float(i) for i in input().split(" ")]
    p1 = Point(data[0], data[1])
    p2 = Point(data[2], data[3])
    p3 = Point(data[4], data[5])
    d1 = p1.distance(p2) 
    d2 = p1.distance(p3) 
    d3 = p3.distance(p2) 

    if (d1 + d2 <= d3) or (d1 + d3 <= d2) or (d2 + d3 <= d1) or (d1 == 0) or (d2 == 0) or (d3 == 0):
        print("INVALID")
    else:
        print("{:.3f}".format(d1 + d2 + d3))
    t -= 1