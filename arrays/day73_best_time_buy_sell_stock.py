# Problem: Best Time to Buy and Sell Stock
# Day: 73

n = list(map(int, input("enter numbers: ").split()))

m = n[0]
profit = 0

for i in range(1, len(n)):

    if n[i] - m > profit:
        profit = n[i] - m

    if n[i] < m:
        m = n[i]

print(profit)
