n = list(map(int, input("enter :").split()))
k = int(input("enter :"))

n.sort()

diff = n[-1] - n[0]

for i in range(1, len(n)):
    if n[i] - k < 0:
        continue

    low = min(n[0] + k, n[i] - k)
    high = max(n[i - 1] + k, n[-1] - k)

    diff = min(diff, high - low)

print(diff)
