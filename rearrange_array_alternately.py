# Rearrange array in alternating max and min order

n = list(map(int, input("enter : ").split()))

n.sort()

ans = []

l = 0
r = len(n) - 1

while l <= r:
    ans.append(n[r])
    r -= 1

    if l <= r:
        ans.append(n[l])
        l += 1

print(ans)
