#This program squares all numbers that the user inputs.

chosenNumb = input("Enter a list of numbers separated by spaces: ")

userList = chosenNumb.split()

print("user list is ",userList)

print("Calculating the square of selected numbers...")

for x in userList:
    print(str(x), end = '')
    x= int(x)**2
    print(" to the power of 2 is: " + str(x))