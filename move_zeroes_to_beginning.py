n = list(map(int, input("enter: ").split()))

slow = 0

for fast in range(len(n) - 1, -1, -1):

    if n[fast] == 0:
        n[slow], n[fast] = n[fast], n[slow]
        slow += 1

print(n)
