# This program takes all the user inputted numbers and puts them on a list.
# It uses the "while" Indefinite Loop.

listNums=input("Enter a series of numbers separated by spaces: ")

userNums = listNums.split()

print("User list is:")

length = len(userNums)
i=0

while i <length:
    print(userNums[i])
    i+=1