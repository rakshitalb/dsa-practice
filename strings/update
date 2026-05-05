# Problem: Valid Anagram
# Day: 6
# Topic: Strings

def freq(s, t):
    d = {}
    r = {}

    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1

    for ch in t:
        if ch in r:
            r[ch] += 1
        else:
            r[ch] = 1

    return d == r


s = input("enter first string: ")
t = input("enter second string: ")

print(freq(s, t))
