# Problem: Second Largest Element
# Day: 75

n = list(map(int, input("enter numbers: ").split()))

n = list(set(n))
n = sorted(n)

if len(n) < 2:
    print("No second largest element")
else:
    print(n[-2])
