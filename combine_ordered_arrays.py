n = list(map(int, input("enter : ").split()))
val = list(map(int, input("enter : ").split()))

i = 0
j = 0

ans = []

while i < len(n) and j < len(val):

    if n[i] < val[j]:
        ans.append(n[i])
        i += 1
    else:
        ans.append(val[j])
        j += 1

while i < len(n):
    ans.append(n[i])
    i += 1

while j < len(val):
    ans.append(val[j])
    j += 1

print(ans)
