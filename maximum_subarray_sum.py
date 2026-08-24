# Find the maximum sum of a contiguous subarray

n = list(map(int, input("enter : ").split()))

m = n[0]
s = 0

for i in n:
    s += i
    m = max(m, s)

    if s < 0:
        s = 0

print(m)
