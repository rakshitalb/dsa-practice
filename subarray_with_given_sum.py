# Find a continuous subarray with the given sum

n = list(map(int, input("enter : ").split()))
s = int(input("sum : "))

start = 0
total = 0

for end in range(len(n)):
    total += n[end]

    while total > s:
        total -= n[start]
        start += 1

    if total == s:
        print(start + 1, end + 1)
        break
else:
    print(-1)
