a = list(map(int, input("enter first array: ").split()))
b = list(map(int, input("enter second array: ").split()))

i = 0
j = 0
ans = []

while i < len(a) and j < len(b):

    if a[i] == b[j]:
        ans.append(a[i])
        i += 1
        j += 1

    elif a[i] < b[j]:
        i += 1

    else:
        j += 1

print(ans)
