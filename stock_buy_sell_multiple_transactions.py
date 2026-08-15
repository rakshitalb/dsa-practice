n = list(map(int, input("enter : ").split()))

profit = 0

for i in range(1, len(n)):
    if n[i] > n[i - 1]:
        profit += n[i] - n[i - 1]

print(profit)
