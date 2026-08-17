# Find the element that occurs most frequently in an array

n = list(map(int, input("enter :").split()))
d = {}

for i in range(len(n)):
    if n[i] not in d:
        d[n[i]] = 1
    else:
        d[n[i]] += 1

val = max(d.values())

for key, value in d.items():
    if value == val:
        print(key)
