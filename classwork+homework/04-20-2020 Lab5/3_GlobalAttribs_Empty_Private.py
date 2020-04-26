#   Returning to the beginning of the introduction for OOP, 
# we should remind ourselves about the possibility of creating
# attributes which are shared by all instances of a given class.
#
#   NOTE:
#       EXAMPLE
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

print(p1.counter)
print(p2.counter)
p1.update(1)
print(p1.counter)
print(p2.counter)