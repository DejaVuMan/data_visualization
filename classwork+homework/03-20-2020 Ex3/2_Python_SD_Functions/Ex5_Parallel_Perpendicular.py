print("This program lets you enter in two linear equations, and will evaluate if they are Parallel or Perpendicular.")
print("Please enter the values for your first equation: ")
print("y=",end = " ")
m1 = input()
print("x+",end = " ")
b1 = input()
print("Enter the values for your second equation: ")
print("y=",end = " ")
m2 = input()
print("x+",end = " ")
b2 = input()

m1=float(m1)

m2=float(m2)

def perParall(p1,p2):
    if p1 == p2:
        print("Your linear functions are parallel!")
        return '||'
    elif p1*p2 == -1:
        print("Your linear functions are perpendicular!")
        return '+'
    else:
        print("Your functions have no direct correlation.")
        return 0

print(perParall(m1,m2))
