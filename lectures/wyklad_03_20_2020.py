list1 = [1,2,3,4]
list2=list1
list1[2]='a'
print(list1)
# Remember everything is referential!
# So, redefining value is done via reference as well.

print(list2)

# You can also call on a specific value in that array
print(list2[3])
# [1 2 a 4]
#  0 1 2 3

# list1.Append('5') would add the value as the final alue in the array.
# list1.Extend([4,5,6]) adds all of these values to the array and extends it.

listTest= [1,'a','b',True]
print(listTest)
listTest.remove(True)
print(listTest)

#List Comprehensions \/ \/ \/
squares = []
for x in range(5):
    squares.append(x ** 2)

print (squares)

#############################

squares = [x**2 for x in range(5)]
print(squares)

#############################

#tuple objects

sLtuple = 123, 'abc', True
print(sLtuple[2])

#############################

#Constructing sets

letters= {'one','two','one','three','eight'}
print(letters)

##############################

#'dictionary'?

dictionary={'back':4098,'jack':4138,'do':'it'}
dictionary["again"]= "wheels keep turnin"
print(dictionary)
