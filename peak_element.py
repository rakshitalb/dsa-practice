n = list(map(int, input("enter :").split()))

for i in range(len(n)):
    left = n[i-1] if i > 0 else float("-inf")
    right = n[i+1] if i < len(n)-1 else float("-inf")

    if left < n[i] > right:
        print(i)
        break
