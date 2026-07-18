# Problem: First Non-Repeating Character
# Day: 80

s = input("enter string: ")

d = {}

for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1

found = False

for ch in s:
    if d[ch] == 1:
        print(ch)
        found = True
        break

if found == False:
    print("No non-repeating character")
