n = list(map(str, input("enter")))

d = {}
c = 1

for i in range(1, len(n)):
    if n[i] == n[i-1]:
        c += 1
    else:
        c = 1

    if n[i] not in d:
        d[n[i]] = c
    else:
        d[n[i]] = max(d[n[i]], c)

val = max(d.values())

for key, value in d.items():
    if value == val:
        print(key)
