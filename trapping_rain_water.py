# Calculate the amount of rainwater trapped between bars

n = list(map(int, input("enter : ").split()))

water = 0

for i in range(1, len(n) - 1):
    left = max(n[:i])
    right = max(n[i + 1:])

    h = min(left, right) - n[i]

    if h > 0:
        water += h

print(water)
