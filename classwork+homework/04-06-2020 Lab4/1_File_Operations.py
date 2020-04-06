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