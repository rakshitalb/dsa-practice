# Problem: Reverse Vowels of a String
# Day: 47
# Time Complexity: O(n)
# Space Complexity: O(n)

vowels = ['a', 'e', 'i', 'o', 'u']

s = input("enter string: ")

chars = list(s)

v = []

for ch in chars:
    if ch.lower() in vowels:
        v.append(ch)

v.reverse()

j = 0

for i in range(len(chars)):
    if chars[i].lower() in vowels:
        chars[i] = v[j]
        j += 1

print("".join(chars))
