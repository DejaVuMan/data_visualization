#   Definite Iteration Loops, also commonly referred to as "For" Loops because "For" is they keyword used to introduce them.
# Generally, there are very few flavors of Definite Iteration; this section will cover "for" loops.
#
#   A numeric loop will look like this:
#   for NUMBER in SEQUENCE:
#       instruction
#   [else: 
#       other_instruction]
#
#   for i = 1 to 100
#       <loop body>
#
#       The sequence part can be a chain, list, or Tuple (Krotka). From the beginning of the counting sequence begings the iterational loop and its 
#   instructions to carry out. the 'i' value is assigned the first value in the sequence, then it is assigned the next value, and so on. 
#
#       To create a sequence, we can use this function:
#           range([start, stop, increment])
#
#   FOR EXAMPLE: say that we want to count all numbers in a range from 1 to 5.
#
for x in range (1, 6, 1):
    print(str(x) + " ")
#
#   Alternatively, lets say that we have a list and want to use it as a sequence and to display its values.
#
listT = [3, 4, 2, 1, 6]

for x in listT:
    print(str(x) + " ")
#
#   We can also do the above, but add a message when there are no elements left in the list.

listT = [3, 4, 2, 1, 6]

for x in listT:
    print(str(x) + " ")
else:
    print("No more numbers to display.")
