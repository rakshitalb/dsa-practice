n = list(map(int, input("enter :").split()))

d = int(input("enter :"))

s = 1

for f in range(len(n) - 1, -1, -1):
    if s == d:
        print(n[f])
        break
    s += 1
