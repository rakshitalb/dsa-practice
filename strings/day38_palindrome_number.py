# Problem: Palindrome Number
# Day: 38
# Time Complexity: O(n)

def palindrome(x):

    s = str(x)

    return s == s[::-1]


x = int(input("enter number: "))

print(palindrome(x))
