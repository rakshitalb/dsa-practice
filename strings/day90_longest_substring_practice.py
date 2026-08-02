s = list(input("Enter: "))

d = []
m = 0

for i in range(len(s)):
    while s[i] in d:
        d.pop(0)

    d.append(s[i])
    m = max(m, len(d))

print(m)
