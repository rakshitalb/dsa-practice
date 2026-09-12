n = list(map(int, input("enter : ").split()))
m = list(map(int, input("enter : ").split()))

i = 0
j = 0
ans = []

while i < len(n) and j < len(m):

    if n[i] < m[j]:
        if not ans or ans[-1] != n[i]:
            ans.append(n[i])
        i += 1

    elif n[i] > m[j]:
        if not ans or ans[-1] != m[j]:
            ans.append(m[j])
        j += 1

    else:
        if not ans or ans[-1] != n[i]:
            ans.append(n[i])
        i += 1
        j += 1

while i < len(n):
    if not ans or ans[-1] != n[i]:
        ans.append(n[i])
    i += 1

while j < len(m):
    if not ans or ans[-1] != m[j]:
        ans.append(m[j])
    j += 1

print(ans)
