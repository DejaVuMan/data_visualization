# Functions

def changeme():
    global list
    list = [2, 3, 4]
    print("Internal Function: ", list)
    return

changeme()
print(list)
##############################
def sum(a,b):
    return 2*a+b

print(sum(a=3,b=6))

def sumsub(a,b,c=0,d=0): #Basically, if D isn't defined, then it has a value of 0.
    return a-b + c-d
print(sumsub(12, 4,2,4)) 

#def average(first, *values):
#    return (first + sum(values)) / (1+ len(values))
#
#print(average(2,3,4,6))

def f(**kwargs):
    print(kwargs)
f(pl="Polish", en="English") #Basically treated as a dictionary)
########################
import math

a=0
b=math.sin(2*math.pi)
print(b)

#-2.449293598

print(math.isclose(a,b,rel_tol=1e-09,abs_tol=1e-09))

## True
