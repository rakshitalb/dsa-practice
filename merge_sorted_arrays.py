a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

p1 = 0
p2 = 0

ans = []

while p1 < len(a) and p2 < len(b):

    if a[p1] < b[p2]:
        ans.append(a[p1])
        p1 += 1
    else:
        ans.append(b[p2])
        p2 += 1

while p1 < len(a):
    ans.append(a[p1])
    p1 += 1

while p2 < len(b):
    ans.append(b[p2])
    p2 += 1

print(ans)
