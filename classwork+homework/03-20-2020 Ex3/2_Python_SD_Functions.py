#   In Python, we can define our own functions. We can treat them as subprograms, or functions within MATLab.
#
#   NOTE: Example Structure.
#
#   def funtion_name(position_arg, arg_default=value, *arg_4, ** arg_5):
#       instructions
#       return value
######################
#   Function Definition:
#       
#   def defaultArg(name, msg = "Hello!"):
#
#   Function Call:
#
#   defaultArg(name)
######################
#   NOTE: Required Arg Function:
#
#   def requiredArg(str,num):
#
#   Function Call:
#
#   requiredArg("Hello",12)
######################
#
#   NOTE: Lets not forget about Keyword Arguments!
#
#   Keyword Arguments are relevant for Python Function calls. The keywords mentioned during the function call along with their correspondent values.
# These keywords are then mapped with the func args so the function can easily identify the corresponding values even if the order is not maintained
# during the function call. Below is the correct syntax for such a KA function.
#
#   Function Definition: 
#
#   def keywordArg(name, role):
#
#   Function Call:
#
#   keywordArg(name = "Alan", role = "CEO of Bad Decisions and Stupid Mistakes")
#   NOTE: The above can have reversed order - (role, name), etc.
######################
#
#   NOTE: Finally, there are also VARIABLE number of argument functions!
# 
#   These are most useful when you're not sure of how many arguements will be provided.
# 
#   Function Definition:
#   
#  def varlengthArgs(*varargs):
#
#   Function Call:
#
#   varlengthArgs(30,40,50,60)
######################
#
#   So BASICALLY, this is how you write your own function:
#   Step 1. Declare the Function with the keyword "def" followed by the function name.
#   Step 2. Write the arguements inside the opening and closing parenthesis of the function, and end the declaration with a colon.
#   Step 3. Add the program statements to be executed.  Step 4. End the function with/without a return statement.
#
#   def userDefFunction(arg1, arg2, arg3,...):
#       program statement1
#       program statement2
#       program statement3
#       ...
#       return;
#
#   Lets see an example of a Default Argument.
#
def defArgFunc( empname, emprole = "Manager" ):   
   print ("Emp Name: ", empname)
   print ("Emp Role: ", emprole)
   return
print("Using default value")
defArgFunc(empname="Nick")
print("************************")
print("Overwriting default value")
defArgFunc(empname="Tom",emprole = "CEO")
#
#   And here's an example of a Variable Length Arguement.
#
def varLenArgFunc(*varvallist ):   
   print ("The Output is: ")
   for varval in varvallist:
      print (varval)
   return
print("Calling with single value")
varLenArgFunc(55)
print("Calling with multiple values")
varLenArgFunc(50,60,70,80)
#
print("#####################")
#
#   Now, let's do a complicated example with Quadratic Functions!
#
import math

def quadEquation(a, b, c):
    delta = b**2 - 4*a*c
    if  (delta<0):
        print("No roots exist!")
        return -999
    elif (delta == 0):
        print("One root point exists.")
        x = (-b) / (2*a)
        return x
    else:
        print("Your Equation has 2 root points: ")
        x1= (-b - math.sqrt(delta)) / (2*a)
        x2= (-b + math.sqrt(delta)) / (2*a)
        return x1, x2
print(quadEquation(6,1,3))
print(quadEquation(1,2,1))
print(quadEquation(1,4,1))