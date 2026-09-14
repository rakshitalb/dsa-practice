n = sorted(list(map(int, input("enter :").split())))
m = sorted(list(map(int, input("enter :").split())))

i = 0
j = 0
c = 0
ans = []

while i < len(n) and j < len(m):

    if n[i] == m[j]:
        ans.append(n[i])
        c += 1
        i += 1
        j += 1

    elif n[i] < m[j]:
        i += 1

    else:
        j += 1

print(c)
print(ans)
