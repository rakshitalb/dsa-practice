n = list(map(int, input().split()))
k = int(input())

k = k % len(n)

print(n[-k:] + n[:-k])
