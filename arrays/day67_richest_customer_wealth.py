# Problem: Richest Customer Wealth
# Day: 67

def richest_wealth(accounts):

    maximum = 0

    for row in accounts:

        total = sum(row)

        if total > maximum:

            maximum = total

    return maximum


n = int(input("enter number of customers: "))

accounts = []

for i in range(n):

    accounts.append(list(map(int, input().split())))

print(richest_wealth(accounts))
