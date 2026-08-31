# Find the maximum amount of water between two lines

n = list(map(int, input("enter : ").split()))

l = 0
r = len(n) - 1
m = 0

while l < r:
    area = (r - l) * min(n[l], n[r])
    m = max(m, area)

    if n[l] < n[r]:
        l += 1
    else:
        r -= 1

print(m)
