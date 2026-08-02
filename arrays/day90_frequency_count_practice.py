n = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))

d = {}

for num in n:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
    if k > 0:
        print(key)
        k -= 1
