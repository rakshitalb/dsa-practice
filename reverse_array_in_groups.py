n = list(map(int, input("enter :").split()))
k = int(input("enter k :"))
ans = []
s = []

for i in range(len(n)):
    s.append(n[i])
    if len(s) == k:
        s = s[::-1]
        ans.extend(s)
        s.clear()

if len(s) != 0:
    s = s[::-1]
    ans.extend(s)

print(ans)
