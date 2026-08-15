n = list(map(int, input("enter : ").split()))

c = 1
m = 1

for i in range(1, len(n)):
    if n[i - 1] == n[i]:
        c += 1
    else:
        c = 1

    m = max(m, c)

print(m)
