# This program writes the absolute value out of whatever entered number you have.

number=input("Please enter a number. This program will give you its absolute value: ")

number = int(number)

if number < 0:
    print("The absolute value of " + str(number))
    number = number*-1
    print(" is: " + str(number))
elif number >= 0:
    print("The absolute value of " + str(number) + " is: " + str(number))