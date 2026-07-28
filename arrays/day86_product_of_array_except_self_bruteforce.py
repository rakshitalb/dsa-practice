n = list(map(int, input("Enter: ").split()))

f = []

for i in range(len(n)):
    p = 1
    for j in range(len(n)):
        if i != j:
            p *= n[j]
    f.append(p)

print(f)
