#This program lists all numbers divisible by 5 from user input.

chosenNumb = input("Enter a list of numbers separated by spaces: ")

userList = chosenNumb.split()

print("user list is ",userList)

print("Calculating numbers divisible by 5...")

for x in userList:
    if int(x)%5 < 1:
        print(str(x) + " is divisible by 5.")   