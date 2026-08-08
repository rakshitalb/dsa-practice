n = list(map(int, input("Enter: ").split()))
ans = []

for i in n[:]:
    if i == 0:
        n.remove(i)
        ans.append(i)
    else:
        continue

print(n + ans)
