filepath = ("C:\\GitRepo\\data_visualization\\classwork+homework\\04-06-2020 Lab4\\1_File_Operations\\Ex3_WriteTo_ReadFrom\\Ex3Test.txt")

document = open(filepath,"w+")
x = input("What would you like to write to this file?: ")

document.write(x)
document.close()

print("The program will now read back to you what you wrote:\n")

with open(filepath,"r") as Doc:
    for line in Doc:
        print(line, end="")

input("\nPress ENTER to end.")