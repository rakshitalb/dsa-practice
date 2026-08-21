# Find the majority element in an array

n = list(map(int, input("enter : ").split()))

for i in n:
    if n.count(i) > len(n) // 2:
        print(i)
        break
