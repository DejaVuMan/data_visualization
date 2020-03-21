# This program gets a number from the user and adds all of the digits in it together into one.

listNums=input("Enter a mutli-digit number: ")
res=[int(x) for x in str(listNums)]
print("The sum of all digits is: ")

length = len(res)
i=0
totalSum=0
while i < length:
    totalSum = totalSum + int(listNums[i])
    i+=1

print(str(totalSum))

input('Press ENTER to exit')