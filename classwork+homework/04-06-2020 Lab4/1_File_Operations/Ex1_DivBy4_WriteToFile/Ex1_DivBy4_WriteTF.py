# This file will list out all numbers divisible by 4 and list them to a document.

ListDivis = open("C:\\GitRepo\\data_visualization\\classwork+homework\\04-06-2020 Lab4\\1_File_Operations\\Ex1_DivBy4_WriteToFile\\NumsDivisibleBy4.txt","w+")
a = 1
b = 21
listDiv = []
for x in range (a,b): #From a1 to b21
    if x % 4 == 0:
        listDiv += [x]

ListDivis.writelines(str(listDiv))

ListDivis.close()