# Find elements occurring more than n/3 times

n = list(map(int, input("enter :").split()))
d = {}

for i in range(len(n)):
    if n[i] not in d:
        d[n[i]] = 1
    else:
        d[n[i]] += 1

ans = []
m = len(n) // 3

for key, value in d.items():
    if value > m:
        ans.append(key)

ans.sort()
print(ans)
