n = list(map(int, input("Enter: ").split()))

s = min(n)
m = n.index(s)

print(m)

mm = max(n[m:])

print(mm)

b = mm - s

print(b)
