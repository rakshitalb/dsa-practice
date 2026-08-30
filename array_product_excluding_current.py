n = list(map(int, input("enter : ").split()))

ans = []
t = 1
z = 0

for i in range(len(n)):
    if n[i] != 0:
        t *= n[i]
    else:
        z += 1

for i in range(len(n)):
    if n[i] != 0:
        if z == 0:
            ans.append(t // n[i])
        else:
            ans.append(0)
    else:
        if z == 1:
            ans.append(t)
        else:
            ans.append(0)

print(ans)
