n = list(map(int, input("enter : ").split()))

res = n[0]
m = n[0]

for i in range(1, len(n)):
    m = max(m + n[i], n[i])
    res = max(m, res)

print(res)
