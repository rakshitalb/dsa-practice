l1 = list(map(int, input("enter :").split()))
l2 = list(map(int, input("enter :").split()))

l1.reverse()
l2.reverse()

r = ""
s = ""

for i in l1:
    r += str(i)

for i in l2:
    s += str(i)

d = int(r) + int(s)

d = str(d)
d = d[::-1]

print(list(map(int, d)))
