# Find the missing number in an array

n = list(map(int, input("enter : ").split()))

total = len(n) * (len(n) + 1) // 2
missing = total - sum(n)

print(missing)
