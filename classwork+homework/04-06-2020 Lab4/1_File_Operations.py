## Working with Files, and Intro do Objective Programming
#
# 1. Working with Files
#   There are three "fields" which are relevant to working with files.
#
#   I. Opening Files
#   II. Using those files (Read or Write ops)
#   III. Closing a file.
#
#   The basic structure looks something like this:
#   
#   NOTE: file = open(filename, operation_type)
#
#   Filename is obviously, the file name / path.
#   operation_type is what you want to do with the file.
#
#   "r" = READ only
#   "w" = WRITE only
#   "a" = WRITE to file, adding on to what is already there. Known as Append.
#   "r+" = READ and WRITE. The file must exist first!
#   "w+" = READ and WRITE. If the file doesn't exist, it is created!
#   "a+" = READ and WRITE. If the file doesn't exist it is created!
#
#   Not mentioned in the lesson, there are some other types as well.
#   
#   "x" = CREATES the specified file, returning an error if it exists.
#       NOTE: you can also specify how the file should be handled.
#   "t" = Text. Default Value.
#   "b" = BINARY. Binary mode (e.g, images)
#
#   So, if we had a file named "epic.txt," we'd open it this way:
#
#       open("epic.txt", "rt")
######################################################################
#
# Reading from File
#
#   You can use the following commands:
#
#       read([size]) - Reads what is on the file; you can specify how many characters you want to return as well.
#       readline(size) - you can return one line from the file this way; you can specify how many characters you want read from this line.
#       readlines() - Reads lines from the file.
#
#   NOTE: Example 1.
#
document = open("C:\\GitRepo\\data_visualization\\classwork+homework\\04-06-2020 Lab4\\Exc1_Ex1.txt","r")
# read 10 characters from the file
chars = document.read(10)

# read 1 line from the file
line = document.readline()

# read a paragraph from the file
verse = document.readlines()

# close file
document.close()

# This next part actually shows the results.
# Display 10 characters
print(chars)
print("\n")

# Display a line
print(line)
print("\n")

# Display an entire paragraph
print(verse)
print("\n")

input("Press Enter to Continue")

# Keep in mind that python "remembers" the last position of text read from. This is why we see only the last part of the file when displaing verse from readlines().

# After ending the program, python generally automatically closes the file either way.
#
#   We can WRITE to the file using: write(chain) - Writes data from the variable "chain."
#   We can also use this:           writelines(list) - this writes data from a list.
#
#   NOTE: Example 2 - 

import sys

print("Enter your College, field of study, year, and degree focus: ")
# reads data from the normal input
data = sys.stdin.readline()

# open a file
ColDoc = open("C:\\GitRepo\\data_visualization\\classwork+homework\\04-06-2020 Lab4\\data.txt", "w+")

# write to file
ColDoc.write(data)

# close the file
ColDoc.close()

# now, we create a list
listW = []
for x in range (1,5): #From 1 to 4
    listW += [x]

# open the file to write to
ColDoc = open("C:\\GitRepo\\data_visualization\\classwork+homework\\04-06-2020 Lab4\\data.txt", "a+") # This time, we append to the list.

# write to file
ColDoc.writelines(str(listW))

# and close the file.
ColDoc.close()
#
#   NOTE: Example 3
#
#   We can also open files to read and write to with the help of the command "with."
#   With this, we don't have to worry about closing the document at the end.
#   This for loop lets us display a file, line by line.
#
with open("data.txt","r") as MartyDoc:
    for line2 in MartyDoc:
        print(line2, end="")

input("\nPress ENTER to end.")
