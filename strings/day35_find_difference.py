# Problem: Find the Difference
# Day: 35
# Time Complexity: O(n)

def diff(s, t):

    d = {}

    for ch in s:

        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    for ch in t:

        if ch not in d:
            return ch

        d[ch] -= 1

        if d[ch] < 0:
            return ch


s = input("enter s: ")

t = input("enter t: ")

print(diff(s, t))
