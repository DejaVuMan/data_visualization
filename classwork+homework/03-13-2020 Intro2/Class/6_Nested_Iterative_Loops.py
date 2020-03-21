# Basically, We can put one Loop inside of the other. This is called "nesting" (zagnieżdżaniem).
#
# EXAMPLE:
#   
#   We want to print this on our screen.
#
#   H   H
#   H   H
#   HHHHH
#   H   H
#   H   H
#
#   How the code looks:
#
import sys

for i in [1, 2, 3, 4, 5]: #This is Horizontal
    for j in [1, 2, 3, 4, 5]:
        #check which line of H you are in vertically
        if i == 3:
            sys.stdout.write('H')
        # if not then we write H on the edges
        else:
            #check if 'j' is on the list, which means the edges
            if j in [1, 5]:
                sys.stdout.write('H')
                #if not, then we write spaces.
            else:
                sys.stdout.write(' ')
    sys.stdout.write('\n')