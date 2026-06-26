# Problem: Check if All Characters Have Equal Number of Occurrences
# Day: 56

def equal_occurrences(s):

    d = {}

    for ch in s:

        if ch in d:
            d[ch] += 1

        else:
            d[ch] = 1

    freq = list(d.values())

    for i in range(1, len(freq)):

        if freq[i] != freq[0]:
            return False

    return True


s = input("enter string: ")

print(equal_occurrences(s))
