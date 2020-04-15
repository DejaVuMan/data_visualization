"""
# Compare two strings 
# If character in position I is the same for both
# counter goes up by one

from collections import Counter

def common(str1,str2):
    # into counter dict
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    #insert 
    commonDict = dict1 & dict2

    if len(commonDict) == 0:
        print -1
        return

    #common
    commonChars = list(commonDict.elements())

    x = len("".join(commonChars))

    print(x)

if __name__ == "__main__":
    str1 = "Helllllllo!"
    str2 = "GoodHellllllllo!"
    common(str1,str2)
"""
string1 = 'Hellooooooooooooooooooooooooooooooooo!'
string2 = 'Helloooooooooo!'
s1 = set(string1)
s2 = set(string2)
common_char = s1 & s2 
x = len(common_char)

print(x)