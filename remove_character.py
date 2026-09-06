n = list(input("enter :"))

r = input("enter :")

s = 0

for f in range(len(n)):

    if n[f] != r:
        n[s] = n[f]
        s += 1

print("".join(n[:s]))
