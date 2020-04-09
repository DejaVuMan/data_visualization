# This program creates the class ForGroceries, which contains:
# product_name, amount, unitMeasure, price
# and also methods:
#   constructor - which gives values
#   show_price() - list info on price in console
#   hm_product() - info on how much of a given item there is, i.e:
#       quantity+unit_measurements - ex: 1 item, 3lbs, etc.
#   hm_cost() - counts how much an amount of product costs, i.e:
#       3lbs of potatoes, and the price is $1.50 per pound, so the function returns
#       1.50*3 = 4.50.

class Grocer(object):
    def __init__(self, item, amount, measurement, ind_Price):
        self.item = item
        self.amount = amount
        self.measurement = measurement
        self.indP = ind_Price

    def show_product(self):
        print(f"Product Name: {self.item}")
        print(f"Amount: {self.amount}")
        print(f"Unit of Measurement: {self.measurement}")
        print(f"Individual Price: ${self.indP}")

    def hm_product(self):
        print(f"The amount of your product is: {self.amount} {self.measurement}")
    
    def hm_cost(self):
        cost = self.amount * self.indP
        print(f"The cost of this item is: ${cost}")

Pineapples = Grocer("Pineapple", 6, "lbs", 2.99)
Pineapples.show_product()
Pineapples.hm_product()
Pineapples.hm_cost()

print("\nPineapples can make many things taste better...")
input("Press ENTER to Continue.")
