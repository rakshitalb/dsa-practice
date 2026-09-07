n = list(map(int, input("enter: ").split()))

s = 0

for f in range(len(n)):

    if n[f] < 0:
        n[s], n[f] = n[f], n[s]
        s += 1

print(n)
