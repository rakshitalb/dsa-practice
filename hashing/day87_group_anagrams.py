n = list(map(str, input("Enter: ").split()))

d = {}

for word in n:
    key = "".join(sorted(word))

    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word)

print(list(d.values()))
