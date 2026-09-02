n = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Target: "))

l = 0
r = len(n) - 1

while l < r:
    s = n[l] + n[r]

    if s == target:
        print(l, r)
        break
    elif s < target:
        l += 1
    else:
        r -= 1
else:
    print(-1)
