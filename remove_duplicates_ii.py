n = list(map(int, input("enter :").split()))

s = 0

for f in range(len(n)):

    if s < 2 or n[f] != n[s - 2]:
        n[s] = n[f]
        s += 1

print(n[:s])
