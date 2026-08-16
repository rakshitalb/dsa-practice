# Find missing and repeating numbers in an array

n = list(map(int, input("enter :").split()))

s = []
f = []

for i in range(len(n)):
    if n[i] not in s:
        s.append(n[i])
    else:
        f.append(n[i])

d = len(s) + 1
total = d * (d + 1) // 2

miss = total - sum(s)

f.append(miss)

print(f)
