n = list(map(int, input("Enter: ").split()))

s = []

for num in range(1, len(n) + 1):
    if num not in n:
        s.append(num)

print(s)
