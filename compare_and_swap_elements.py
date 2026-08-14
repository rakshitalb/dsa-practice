a = list(map(int, input("enter :").split()))
b = list(map(int, input("enter :").split()))

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] < b[j]:
            continue
        else:
            temp = a[i]
            a[i] = b[j]
            b[j] = temp

print(a)
b.sort()
print(b)
