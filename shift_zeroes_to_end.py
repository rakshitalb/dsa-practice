n = list(map(int, input("enter: ").split()))

s = 0
z = 0
ans = []

for f in range(len(n)):

    if n[f] != 0:
        n[s] = n[f]
        s += 1
    else:
        z += 1

ans = [0] * z

print(n[:s] + ans)
