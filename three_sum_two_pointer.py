n = list(map(int, input("enter : ").split()))

n.sort()
ans = []

for i in range(len(n) - 2):

    if i > 0 and n[i] == n[i - 1]:
        continue

    l = i + 1
    r = len(n) - 1

    while l < r:

        s = n[i] + n[l] + n[r]

        if s == 0:
            ans.append([n[i], n[l], n[r]])

            while l < r and n[l] == n[l + 1]:
                l += 1

            while l < r and n[r] == n[r - 1]:
                r -= 1

            l += 1
            r -= 1

        elif s < 0:
            l += 1

        else:
            r -= 1

print(ans)
