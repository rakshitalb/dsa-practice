n = list(map(int,input("enter :").split()))

m = len(n)
total = m * (m + 1) // 2

for i in n:
    total -= i

print(total)
