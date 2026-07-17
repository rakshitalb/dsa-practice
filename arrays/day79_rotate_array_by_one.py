# Problem: Valid Anagram
# Day: 79

s = input("enter first string: ")
t = input("enter second string: ")

if sorted(s) == sorted(t):
    print(True)
else:
    print(False)
