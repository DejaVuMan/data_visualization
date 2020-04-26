class Square():

    def __init__(self, x):
        self.x = x
        self.y = x

#    def __add__(self, y):
#       return self.x + self.y

    def __str__(self):
        #return 'This square has a side length of {} units'.format(self.x)
        return 'The length of the new side length is {} units'.format(self.x.__add__(self.y))
    

sq = Square(5)
print(sq)