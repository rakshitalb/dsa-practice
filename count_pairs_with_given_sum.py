# Count pairs with a given sum

n = list(map(int, input("enter : ").split()))
k = int(input("sum : "))

count = 0

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == k:
            count += 1

print(count)
