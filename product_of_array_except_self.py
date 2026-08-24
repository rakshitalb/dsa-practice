# Find the product of all elements except the current element

n = list(map(int, input("enter : ").split()))

ans = []

for i in range(len(n)):
    p = 1

    for j in range(len(n)):
        if i != j:
            p *= n[j]

    ans.append(p)

print(ans)
