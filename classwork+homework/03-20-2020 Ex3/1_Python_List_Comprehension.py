#   List Comprehensions are generally used to create a collection of some sorts
# (i.e., a list, a dictionary, a set) on the basis of a one-line definition.
# You can generally always give the definition with the help of a loop.
#
#   Sometimes, it is enough to provide the definition of a mathematical
# set in Python.
#
#   This is how it could look:
#
#       Instead of writing inside of a loop -
#
#       listA = []
#       for element in range:
#           if certain_variable_for(element):
#               listA.append("Something has occurred with: " + element)
#
#       We can write ALL of this in one line!
#
#       listA = ["Something has occurred with: " + element for element in range
#       if certain_variable_for(element)].
###################################################
#   NOTE: For Example -
#   We have a predefined set:
#   A={x^2:x e <0,9>}
#
#   B={1,3,9,27,...,3^5}
#
#   C={x:x e A and x is a odd number}
#
#   NOTE: In python, we can write ALL of this as:
#
A=[x**2 for x in range(10)] # 0,1,2,3,4,5,6,7,8,9

B=[3**i for i in range(6)] # 0,1,2,3,4,5,6

C=[x for x in A if x %2 !=0] # Looks at uneven values in A and uses those. so, it would be 1,3,5,7,9

print(A)
print(B)
print(C)
####################################################
#
#   NOTE: For Example - We want to get even numbers from a given set.
#
#       Version with a Loop
#
#       numbers = [1,2,3,4,5,6,7,8,9,10]
#       listB = []
#       for i in numbers:
#           if i % 2 == 0:
#               listB.append(i)
#       
#       print("List of even numbers obtained from intial list: ")
#       print(listB)
#
#   NOTE: Version with Python List Comprehension    
#
numbers = [1,2,3,4,5,6,7,8,9,10]
listB = []
listB = [z for z in numbers if  z % 2 == 0]
print(listB)
####################################################
#   Nested Loops
#
#   NOTE: Instead of writing this - 
#   
#       listC = []
#       for i in [1, 2, 3]:
#           for j in [4, 5, 6]:
#               if i != j:
#                   listC.append((i,j))
#       print(listC)
# 
#   You can Write THIS instead -
#  
listC = [(i,j) for i in [1, 2, 3] for j in [4, 5, 6]]
print(listC)
####################################################
#
#   NOTE: This can also be applied to dictionaries where we replace keys with their values.
#
abbrev = {"LOL" : "Laugh Out Loud",
          "USA" : "United States of America",
          "DC" : "Doge Charger"}
reverse = {value: key for key, value in abbrev.items()}
print("Original values: ")
print(abbrev)
print("Reversed values: ")
print(reverse)
