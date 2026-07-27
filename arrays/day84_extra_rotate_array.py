n = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))

s = len(n) - k
print(s)

d = n[s:]
p = n[:s]

dd = d + p

print(dd)
