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

    

sq = Square(5)
print(sq)
print(sq+sq)
