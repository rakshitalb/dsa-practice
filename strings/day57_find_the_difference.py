# Problem: Find the Difference
# Day: 57

def find_difference(s, t):

    s = sorted(s)
    t = sorted(t)

    for i in range(len(s)):

        if s[i] != t[i]:
            return t[i]

    return t[-1]


s = input("enter first: ")
t = input("enter second: ")

print(find_difference(s, t))
