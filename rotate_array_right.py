# Rotate an array to the right by k positions

n = list(map(int, input("enter : ").split()))
k = int(input("k : "))

k = k % len(n)

n = n[-k:] + n[:-k]

print(n)
