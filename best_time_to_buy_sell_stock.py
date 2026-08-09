# Best Time to Buy and Sell Stock

n = list(map(int, input("Enter: ").split()))

buy = n[0]
m = 0

for i in range(1, len(n)):
    p = n[i] - buy
    m = max(m, p)
    buy = min(buy, n[i])

print(m)
