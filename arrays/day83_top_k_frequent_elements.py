n = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))

d = {}

for num in n:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

s = sorted(d.items(), key=lambda x: x[1], reverse=True)

ans = []

for i in range(k):
    ans.append(s[i][0])

print(ans)
