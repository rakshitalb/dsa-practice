# Problem: Maximum Subarray
# Day: 73 Extra

n = list(map(int, input("enter numbers: ").split()))

cs = n[0]
m = n[0]

for i in range(1, len(n)):
    cs = max(n[i], cs + n[i])
    m = max(m, cs)

print(m)
