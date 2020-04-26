class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Construct a Point."""
        self.x = x
        self.y = y
    
    def update(self, n):
        self.counter.append(n)

p1 = Point(0,0)
p2 = Point(1,1)
p3 = Point(3,9)
p4 = Point(6,9)
p5 = Point(4,20)

print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
p1.update(1)
print(p1.counter)
p1.update(2)
print(p2.counter)
p3.update(3)
print(p3.counter)
p4.update(4)
print(p4.counter)
p4.update(5)
print(p5.counter)