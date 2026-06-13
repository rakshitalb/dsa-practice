# Problem: Valid Palindrome
# Day: 46
# Time Complexity: O(n)

def palindrome(s):

    t = ""

    for ch in s:

        if ch.isalnum():
            t += ch.lower()

    return t == t[::-1]


s = input("enter string: ")

print(palindrome(s))
