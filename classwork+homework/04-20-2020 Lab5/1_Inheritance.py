# Inheritance
#
#   Python Inheritance allows us to define a class that inherits all the methods
# and properties from another class.
#
#   PARENT Class is the class being inherited from, also called BASE class.
#
#   CHILD Class is the class that inherits from another class, also called
# DERIVED Class.
#
#   You can add new methods and attributes with a child class.
#
#  NOTE: First, you must create a Parent Class.
#       Any class can be a parent class, so the syntax is the same as any other class
#
#   EXAMPLE
#       Create a class named Person, with firstname and lastname properties,
#   and a printname method.

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method

x = Person("John", "Doe") # Initializes Person, x goes to it with John and Doe
x.printname()

# CREATE A CHILD CLASS
#
#   To create a class that inherits the functionality from another class, send the
# PARENT Class as a paremeter when creating the child class:
#
#   EXAMPLE
#       Create a class named Student, which will inherit the properties and
#   methods from the Person class.

#class Student(Person):
#    pass # Use the pass keyword when you do not want to add any other properties or methods

#   Now the student class has the same properties and methods as the Person class.
#
#   EXAMPLE
#       Use the Student class to create an object, and then execute the printname method.

# x = Student("Barack","Obama")
# x.printname()
#
#   Add the __init__() Function
#
#   So far we have created a child class that inherits the properties and methods
# from its parent.
#
#   We want to add the __init__() function to the child class(instead of the pass kw).
#
#   NOTE: The __init__() function is called auto every time the class is used to make a new object.
#
#   EXAMPLE
#       Add the __init__() function to the Student class

#class Student(Person):
#    def __init__(self, fname, lname):
         #add properties etc

#   When you add the __init__() function, the cild class no longer inherits the parents one.
# It OVERRIDES the inheritance of the parents __init__() function.
#
#   To keep the inheritance of the parent's __init__() function, add a call to
# the parent's __init__() function.
#
#   EXAMPLE

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

#   Now that we have successfully added the __init__() function, and kept the
# inheritance of the parent class, we are ready to add functionality in the __init__() function.
#
#       Use the super() Function
#
#   Python also has a super() function that will make the child class inherit all
# the methods and properties from its parent.
#
#   EXAMPLE

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)
#
#   By using the super() function, you don't have to use the name of the parent
# element, it will automatically inherit the methods and properties from its parent.
#
#   Add Properties
# For EXAMPLE: we can add graduationyear to the Student class:
#
#         self.graduationyear = 2019
#
#   In this example, 2019 is declared, but we can make it a variable like so:
#
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Al", "Gore", 2023)
x.welcome()