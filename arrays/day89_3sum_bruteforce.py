n = list(map(int, input("Enter: ").split()))

r = []

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        for k in range(j + 1, len(n)):
            if n[i] + n[j] + n[k] == 0:
                r.append(tuple(sorted((n[i], n[j], n[k]))))

print(sorted(set(r)))
