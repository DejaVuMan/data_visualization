# Create a class, which defines an arithmetic series. Values should be stored as an attribute. The class should have these methods:
#
#   show_data: shows elements on screen
#   insert_elements: gets concrete values from the user
#   insert_parameters: Gets the first value and difference from the user, and the number of string elements to be generated.
#   count_sum: Gets the total sum of all elements.
#   count elements: tells the user how many elements there are if the first value and difference is given.

class ASeries(object):
    def __init__(self, firstVal, diff, amount, sum,elems):
        self.fV = firstVal
        self.diff = diff
        self.amount = amount
        self.sum = sum
        self.elems = elems

    def show_data(self):
        print(f"First Value: {self.fV}")
        print(f"Difference Between Elements: {self.diff}")
        print(f"Amount of Elements: {self.amount}")
    
    def insert_parameters(self):
        self.fV = input("Please Enter your first value: ")
        self.fV=int(self.fV)
        self.diff = input("What is the difference between each value in your series?: ")
        self.diff=int(self.diff)
        self.amount = input("How many values are in your series?: ")
        self.amount=int(self.amount)
    
    def count_sum(self):
        self.sum = (self.amount * (2 * self.fV  + (self.amount - 1) * self.diff)) / 2
        print(f"Your Sum is: {self.sum}")

    def count_elems(self):
        Elem_C = self.amount
        print(f"There are " + str(Elem_C) + " elements in your series.")




Series = ASeries(0, 0, 0, 0, 0)
Series.insert_parameters()
Series.show_data()
Series.count_sum()
Series.count_elems()