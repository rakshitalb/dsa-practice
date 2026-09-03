n = list(map(int, input("enter: ").split()))

val = int(input("enter :"))

s = 0

for f in range(len(n)):

    if n[f] != val:
        n[s] = n[f]
        s += 1

print(n[:s])
