n = list(map(int, input("enter : ").split()))
ans = []

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] < n[j]:
            ans.append([n[i], n[j]])

print(ans)
