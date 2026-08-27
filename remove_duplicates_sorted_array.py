# Remove duplicates from a sorted array

n = list(map(int, input("enter : ").split()))

ans = []

for i in n:
    if i not in ans:
        ans.append(i)

print(ans)
