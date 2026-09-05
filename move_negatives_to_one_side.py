n = list(map(int, input("enter :").split()))

s = 0
ans = []

for f in range(len(n)):

    if n[f] < 0:
        n[s] = n[f]
        s += 1
    else:
        ans.append(n[f])

print(n[:s] + ans)
