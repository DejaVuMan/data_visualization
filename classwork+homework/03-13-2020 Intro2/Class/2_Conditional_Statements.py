# Variable instructions look like so: 
#   if condition_1:
#       instruction_1
#   [elif condition_2:
#       instruction_2:
#   ...
#   elif condition_n:
#       instruction_n:
#   else:
#       other_instruction]

# For Example:

# We want to get a number from the user. Maybe his credit card number.
# We want to see if that number is positive or negative.

number=input("Please enter a number:")

# 'number' is a type of a string here. We need to change it to a int.

number = int(number)

if number > 0:
    print("The number entered is positive.")
elif number < 0:
    print("The number entered is negative.")
else:
    print("The number you entered is equal to zero.")

# Another Example:
# This part will check which of two entered numbers is larger.

num1 = input("Enter your first Number: ")
num2 = input("Enter your second Number: ")

# As before, we need to convert the string types ('num1' & 'num2') to int types.
num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(str(num1) + " is greater than " + str(num2))
elif num1 < num2:
    print(str(num2) + " is greater than " + str(num1))
else:
    print("Both numbers are the same!")

