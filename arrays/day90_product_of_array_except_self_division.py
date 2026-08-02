n = list(map(int, input("Enter: ").split()))

p = 1
for i in n:
    p *= i

s = []
for i in n:
    s.append(p // i)

print(s)
