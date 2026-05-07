e = list(map(int, input("enter numbers: ").split()))
d = {}
for num in e:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

# find max frequency
m = max(d.values())

# print elements with max frequency
for key, value in d.items():
    if value == m:
        print(key)
