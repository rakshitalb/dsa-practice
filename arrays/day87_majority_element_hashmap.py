n = list(map(int, input("Enter: ").split()))

s = {}

for i in range(len(n)):
    if n[i] not in s:
        s[n[i]] = 1
    else:
        s[n[i]] += 1

for key, value in s.items():
    if value > len(n) // 2:
        print(key)
