print('Good evening gamers!!!')
print('Very Epic!!!?!')

def main():
    pass

#Comments start with Hashtags!
name = "Doge Charger"
print(name)
print(type(name))
print(type(5))
print(type(5.7))
print(type(True))
print(type(None))
print(name[2])
#name[2] = "G" #You are unable to mutate this type to a different type!
name = "Alan Szuszkiewicz"
name=name.lower() #This is called a chain
#print(name.lower())
print(name)
age = 18
#print(name + " jest z Stanow Zjednoczonych i ma "+ age +"lat.")
# ^ incorrect inseration of int into string
#print(name + " jest z Stanow Zjednoczonych i ma " + age.__str__() + " lat.")
# You could also use str(age). This isn't the most efficient method, though.

print("{} jest z Stanow Zjednoczonych i ma {} lat.".format(name,age))
#This is the better method - easy to use, less text to type.
#print("{0} jest z Stanow Zjednoczonych i ma {1} lat.".format(name,age))
#This method also works!
#print(f"{name} jest z Stanow Zjednoczonych i ma {age} lat.")
#f-string is generally regarded as the best method - from 3.6 onward.
#=====================================================================================
number = 6.75645801237190378
print(f"{number:.2f}")
#pyformat.info

#number types
number = 5
numberF = 5.5
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1//2)#Division without the remainder.
print(3**2)#Raising numbers to a power.
print(1%2)#Modulo

text = "110"
numberFromText = int(text,8)
print(numberFromText)
import math
pi = 3.15
from math import pow, sqrt, pi #Imports every type from math
import math as m
m.pow()
print(m.pi)