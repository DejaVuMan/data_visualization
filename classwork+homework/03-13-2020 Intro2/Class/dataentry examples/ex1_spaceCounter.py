#This program waits for the user to input a sentence and counts the amounts of spaces in the sentence.
#uses the sys library for Input commands.
import sys

print("Please Enter a sentence: ")
x= input() #This command reads a line of user entered text.

count = 0

for i in x:
    if(i.isspace()):
        count=count+1
    
print("The number of blank spaces in the sentence:\n" + x + " epic is: ",count)

