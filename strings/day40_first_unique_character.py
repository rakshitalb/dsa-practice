# Problem: First Unique Character in a String
# Day: 40
# Time Complexity: O(n)

def unique(s):

    d = {}

    # count frequency
    for ch in s:

        if ch in d:
            d[ch] += 1

        else:
            d[ch] = 1

    # find first unique character
    for i in range(len(s)):

        if d[s[i]] == 1:
            return i

    return -1


s = input("enter string: ")

print(unique(s))
