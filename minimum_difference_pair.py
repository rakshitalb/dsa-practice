n = list(map(int, input("enter :").split()))
m = list(map(int, input("enter :").split()))

i = 0
j = 0

mm = float("inf")
ans = ()

while i < len(n) and j < len(m):

    diff = abs(n[i] - m[j])

    if diff < mm:
        mm = diff
        ans = (n[i], m[j])

    if n[i] < m[j]:
        i += 1
    else:
        j += 1

print(mm)
print(ans)
