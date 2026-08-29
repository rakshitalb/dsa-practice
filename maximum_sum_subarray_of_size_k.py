# Find the maximum sum of a subarray of size k

n = list(map(int, input("enter : ").split()))
k = int(input("k : "))

s = sum(n[:k])
m = s

for i in range(k, len(n)):
    s = s - n[i - k] + n[i]
    m = max(m, s)

print(m)
