# Problem: Best Time to Buy and Sell Stock
# Day: 2

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

# User input
prices = list(map(int, input("Enter prices (space separated): ").split()))

result = maxProfit(prices)

print("Maximum Profit:", result)
