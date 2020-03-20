#To enter data, you can use Input commands.

#for example:

a = input("Here is where you would put a typical communication. i.e, Enter a number:\n")
print(a)

#We can also use the commands readline() and write(), which are in the sys module.

#for example:

import sys

print("Enter some text")
s = sys.stdin.readline() #Reads a line of text
print("Your entered text was: " + s)