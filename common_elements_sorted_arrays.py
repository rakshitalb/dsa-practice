n = list(map(int, input("enter : ").split()))

m = list(map(int, input("enter : ").split()))

i = 0
j = 0

ans = []

while i < len(n) and j < len(m):

    if n[i] == m[j]:
        ans.append(n[i])
        i += 1
        j += 1

    elif n[i] < m[j]:
        i += 1

    else:
        j += 1

print(ans)
