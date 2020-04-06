# This program will read the previous file and list it to the console.

with open("C:\\GitRepo\\data_visualization\\classwork+homework\\04-06-2020 Lab4\\1_File_Operations\\Ex1_DivBy4_WriteToFile\\NumsDivisibleBy4.txt","r") as MartyDoc:
    for line2 in MartyDoc:
        print(line2, end="")

input("\nPress ENTER to end.")