s = list(map(str, input("Enter: ").split()))

d = {}

for word in s:
    ch = "".join(sorted(word))
    if ch not in d:
        d[ch] = [word]
    else:
        d[ch].append(word)

print(list(d.values()))
