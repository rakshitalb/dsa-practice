# Problem: Length of Last Word
# Day: 29
# Time Complexity: O(n)

def lastword(s):

    w = s.split()

    return len(w[-1])


s = input("enter string: ")

print(lastword(s))
