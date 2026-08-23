# Find the intersection of two arrays

a = list(map(int, input("enter first array : ").split()))
b = list(map(int, input("enter second array : ").split()))

ans = []

for i in a:
    if i in b:
        ans.append(i)
        b.remove(i)

print(ans)
