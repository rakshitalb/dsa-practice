# Problem: Move Zeroes
# Day: 76

n = list(map(int, input("enter numbers: ").split()))

r = []
s = []

for i in range(len(n)):
    if n[i] == 0:
        s.append(n[i])
    else:
        r.append(n[i])

print(r + s)
