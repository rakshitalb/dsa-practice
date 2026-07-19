arr = input("Enter words: ").split()

d = {}

for word in arr:
    key = "".join(sorted(word))

    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word)

print(list(d.values()))
