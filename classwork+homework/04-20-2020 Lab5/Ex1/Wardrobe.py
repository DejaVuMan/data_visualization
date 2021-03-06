class Material:
    def __init__(self, type, length, width):
        self.type = type
        self.length = length
        self.width = width
    
    def printData(self):
        print("Material type: " + self.type + ". LxW = " + self.length + "x" + self.width +" in.")

x = Material("Cotton", "38", "8")
x.printData()

class Clothes(Material):
    def __init__(self, size, color, gender):
        self.size = size
        self.color = color
        self.gender = gender

    def showData(self):
        print("Clothes size: " + self.size + ". Color: " + self.color + ". Gender: " + self.gender)

class Sweater(Clothes):
    def __init__(self, SWtype):
        self.SwType = SWtype

    def showSweater(self):
        print("Sweater type: " + self.SwType)

y = Clothes("M", "Fuscia", "Unisex")
y.showData()