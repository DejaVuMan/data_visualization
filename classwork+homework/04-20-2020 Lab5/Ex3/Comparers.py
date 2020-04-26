class Square:

    def __init__(self, x):
        self.x = x
        self.y = x

    def __repr__(self):
        return "Square({})".format(self.x)

    def __str__(self):
        return 'The length of the new side length is {self.x} units'.format(self=self)
    
    def __add__(self, other):
        return self.x + self.y
    
    def __lt__(self, other):
        return self.x < other

    def __gt__(self, other):
        return self.x > other 

    def __le__(self, other):
        return self.x <= other

    def __ge__(self, other):
        return self.x >= other   

sq1 = Square(5)
sq2 = Square(10)
print(sq1) #Display results of initial Length
print(sq1+sq1) #Double the length of itself basically
#__lt__(a,b) is a < b
#__le__(a,b) is a <= b
#__eq__(a,b) is a==b
#__ne__(a,b) is a!=b
#__ge__(a,b) is a >= b
#__gt__(a,b) is a > b
print(sq1<sq2) # Check if sq1 less than sq2
print(sq1>sq2)
print(sq1<=sq2) # Check if sq1 less than or equal to sq2
print(sq1>=sq2)