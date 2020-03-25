print("This Program will find the monotonous of a linear function in format: y = mx + b.")
m = input("Enter your value for m: ")
b = input("Enter your value for b: ")
m = int(m)
b = int(b)

def monotFunc(m):
    if m > 0:
        print("Your Function is growing positively.")
        return 1
    elif m < 0:
        print("Your Function is growing negatively.")
        return -1
    else:
        print("Your Function is constant!")
        return 0

print(monotFunc(m))

