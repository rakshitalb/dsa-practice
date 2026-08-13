n = list(map(int, input("enter :").split()))
s = []

while len(n) != 0:
    f = min(n)
    s.append(f)
    n.remove(f)

print(s)
