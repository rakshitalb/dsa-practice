# Find the missing and repeating number

n = list(map(int, input("enter : ").split()))

d = {}

for i in n:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

repeating = 0
missing = 0

for i in range(1, len(n) + 1):
    if i not in d:
        missing = i
    elif d[i] == 2:
        repeating = i

print("Repeating =", repeating)
print("Missing =", missing)
