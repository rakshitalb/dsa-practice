# Problem: Valid Anagram
# Day: 41
# Time Complexity: O(n log n)

def anagram(s, t):

    return sorted(s) == sorted(t)


s = input("enter first string: ")
t = input("enter second string: ")

print(anagram(s, t))
