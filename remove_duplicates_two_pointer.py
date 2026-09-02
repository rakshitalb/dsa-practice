n = list(map(int, input("Enter sorted array: ").split()))

slow = 0

for fast in range(1, len(n)):
    if n[fast] != n[slow]:
        slow += 1
        n[slow] = n[fast]

print(n[:slow + 1])
