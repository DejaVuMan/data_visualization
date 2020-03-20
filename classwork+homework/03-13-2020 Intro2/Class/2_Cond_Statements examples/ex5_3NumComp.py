# This program waits for you to input 3 numbers ('a','b','c') and checks if 'a' is between 0 to 10, and if a>b or b>c.
numA = input("Enter your first number: ")
numB = input("Enter your second number: ")
numC = input("Enter your third number: ")

if int(numA)>=0 and int(numA)<10 and (int(numA)>int(numB) or int(numB)>int(numC)):
    print("All three numbers meet the requirements!")
else:
    print("One or more of your entered numbers did not match the requirements.")
    