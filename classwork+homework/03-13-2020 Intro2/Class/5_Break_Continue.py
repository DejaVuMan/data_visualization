#   Break and Continue are operations typically reserved for loops.
#
#   Break: Forces the loop to halt and continues to code outside of the loop.
#
#   Continue: Ends current part of loop and continues to the next part.
#
#   EXAMPLE:
#
#       User Provides a number
#   Program looks through a predetermined list of numbers, and if theres a match,
#   we let the user know, and end the loop.
# 
listO = [1, 5, 3, 2, 6, 7, 8, 9, 10]
print("Please enter a number - the program will check if it exists in the list: ")
#   
number=input()
counter = 0
while counter < 10:
#   if we find a match, we end the loop.
    if int(number) == listO[counter]:
        print("Your Number: " + number + " - exists in position: " + str(counter))
        break
    else:
        counter += 1