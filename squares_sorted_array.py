n = list(map(int, input("enter: ").split()))

l = 0
r = len(n) - 1
ans = [0] * len(n)

i = len(n) - 1

while l <= r:

    if abs(n[l]) > abs(n[r]):
        ans[i] = n[l] ** 2
        l += 1
    else:
        ans[i] = n[r] ** 2
        r -= 1

    i -= 1

print(ans)
