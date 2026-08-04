n = list(map(int, input("Enter: ").split()))

d = {}

for num in n:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

for key, value in d.items():
    if value > len(n) // 2:
        print(key)
        break
