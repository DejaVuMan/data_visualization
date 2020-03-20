#   A little different from Definite Iteration.
#
#   Basically, Indefinite Iteration, the number of times the loop is
# executed isn't specified explicity in advance!
# It continues going as long as some condition is met.
#
#   A While loop will look like this:
#
#       while <expr>:
#           <statement(s)>
#
#       while condition:
#           instruction
#       [else:
#               other_instruction]
#
#   FOR EXAMPLE:
#
#   The program below keeps displaying a random number until
# it gets 5.
#
import random #This library has lottery functions

random.seed() #Initialize generator

z = random.randint(1,15) #Gets the first number.

while(z != 5):
    print(str(z))
    z = random.randint(1,15)
else:
    print("I have recieved the number 5; End of Program.")