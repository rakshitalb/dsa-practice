# Find the equilibrium index

n = list(map(int, input("enter : ").split()))

total = sum(n)
left = 0

for i in range(len(n)):
    right = total - left - n[i]

    if left == right:
        print(i)
        break

    left += n[i]
else:
    print(-1)
