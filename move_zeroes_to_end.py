# Move all zeroes to the end of the array

n = list(map(int, input("enter : ").split()))

ans = []

for i in n:
    if i != 0:
        ans.append(i)

while len(ans) < len(n):
    ans.append(0)

print(ans)
