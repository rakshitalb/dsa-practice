n = list(map(int, input("Enter: ").split()))

r = n[0]
rr = 0

for i in range(1, len(n)):
    if n[i] < r:
        r = n[i]
    else:
        rr = max(rr, n[i] - r)

print(rr)
