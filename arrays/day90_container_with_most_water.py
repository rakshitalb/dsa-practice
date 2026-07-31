n = list(map(int, input("Enter: ").split()))

m = 0
l = 0
r = len(n) - 1

while l < r:
    h = min(n[l], n[r])
    d = r - l
    area = h * d

    m = max(m, area)

    if n[l] < n[r]:
        l += 1
    else:
        r -= 1

print(m)
