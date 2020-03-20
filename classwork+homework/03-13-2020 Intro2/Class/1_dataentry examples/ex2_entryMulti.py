# This program uses readline() to get from the user two numbers to multiply and prints the result out with write().
import sys
print('Enter your first number to multiply.')
s = sys.stdin.readline() # Holds the first user input in 's'.
print('Enter your second number to multiply.')
s2 = sys.stdin.readline() # Holds the second user input in 's2'.

ans = int(s)*int(s2) # Makes 'ans' be the result of multiplying s and s2 together. uses int() to convert entry from string to number.
epic=str(ans) # Makes 'epic' be the result of 'ans,' but must be converted to string to be displayed by write().
sys.stdout.write(epic)

# NOTE: there is probably a better way to do this...