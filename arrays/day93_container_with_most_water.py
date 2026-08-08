n = list(map(int,input("enter :").split()))
l = 0
r = len(n) - 1
m = 0

while l < r:
    d = r - l
    h = min(n[r],n[l])
    w = d * h
    m = max(m,w)

    if n[l] < n[r]:
        l += 1
    else:
        r -= 1

print(m)
