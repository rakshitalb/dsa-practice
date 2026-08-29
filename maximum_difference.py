# Find the maximum difference between two elements
# where the larger element appears after the smaller element

n = list(map(int, input("enter : ").split()))

minimum = n[0]
maximum = -1

for i in range(1, len(n)):
    if n[i] - minimum > maximum:
        maximum = n[i] - minimum

    if n[i] < minimum:
        minimum = n[i]

print(maximum)
