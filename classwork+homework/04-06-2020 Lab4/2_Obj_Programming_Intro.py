## INTRO to Object-Oriented Programming in Python
#
#   Important Terminology etc
#
#   Object-Oriented Programming requires designing a structure based on data & code.
# This structure is called a class & every object created on the basis of this
# class is an instance of an instance *** of a given class. 
#
#   The data associated with the object will be attributes (or properties), and the
# functions that perform something on the object are methods.
#
#   NOTE: Encapsulation
#       Also known as Hermitization. Basically, encapsulation works on the basis
#       that the class is defined in such a way so that it's methods only serve
#       the properties of the object, and no other outside function can modify
#       the properties of said object.
#       I.E, an object's variable can only be changed by an object's method.
#
#   NOTE: Inheritance
#       Inheritance allows us to define class that inherits all the methods and
#       properties from another class.
#       NOTE: a PARENT class is the class being inherited from, aka BASE class.
#       NOTE: a CHILD class is the class that inherits from another class,
#       aka DERIVED class.
#
#   Defining a class is rather simple.
#       EXAMPLE:
#       class ClassName[(BaseClass1, BaseClass2, BaseClass3)]:
#           instruction1
#           instruction2
#           ...
#           instructionN
#
#       EXAMPLE 4:
#       class FirstClass:
#           """"Example of a Class"""
#
#       object = FirstClass()
#       print(object)
#
#   In the Above ^^^ example, we declare a class, and then set Object to be it,
#   and then print object, thus printing  the location of FirstClass.
#
#       EXAMPLE 5:
#
#       class FirstClass:
#           """Example of a class"""
#           attribute = 12345
#
#       object = FirstClass()
#       print(object)
#       print(object.attribute)
#
#       Similar to the 5th example, but here we can print the location in FirstClass,
#       or just part of it.
#
#       EXAMPLE 6 - Method:
#
#       class FirstClass:
#           """Example of a Class"""
#           attribute = 12345
#
#           def first_method(self):
#               return "This is an example of a Method"
#
#       object = FirstClass()
#       print(object)
#       print(object.attribute)
#       print(object.first_method())  
# 
#       EXAMPLE 7 - Adding attributes to a class
#      
#       class FirstClass:
#           """Example of a Class"""
#           attribute = 12345
#
#           def first_method(self):
#               return "This is an example of a Method"
#       
#       object = FirstClass()
#       print(object)
#
#       # here we print the attribute
#       print(object.attribute)
#
#       # and here, we're adding an attribute to an existing class
#       object.text = "Don't you know you're beautiful"
#       print(object.text)
#
#       # however, it will not exist in a new instance of class!
#       new_object = FirstClass()
#       print(new_object.text)  # <- Will not work!
#
######################
#
#   NOTE: CONSTRUCTORS
#       Constructors are special functions which create objects.
#   If we don't define our own, Python makes one up basically.
#   In python, a constructor doesn't creat an instance for a class,
#   but gives a value to an object.
#   Most often used to INITIALIZE to data members.
#
#   Syntax of constructor declaration:
#
#       def __init__(self):
#           #body of the constructor
#
#   EXAMPLE 8:
#
class Shaper:
    #define the constructor
    def __init__(self, x, y):
        #declare attributes
        #self points to variables declared by the class itself
        self.x=x
        self.y=y
        self.definition = "Here is a class for general shapes"

    def vals_rectangle(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def add_description(self, text):
        self.definition = text

    def scale(self, factor):
        self.x = self.x * factor
        self.y = self.y * factor

#Create the object

square = Shaper(10,30)

# here, we check how the method works which returns the values
print(square.vals_rectangle())
print(square.perimeter())

# here, we check how the methods which don't return values work
square.add_description("Square")
print(square.definition)

square.scale(0.5)
print(square.x)
print(square.y)