arr = list(map(int, input("enter :").split()))

p = []
n = []

for num in arr:
    if num >= 0:
        p.append(num)
    else:
        n.append(num)

pi = 0
ni = 0
i = 0

while pi < len(p) and ni < len(n):
    if i % 2 == 0:
        arr[i] = p[pi]
        pi += 1
    else:
        arr[i] = n[ni]
        ni += 1
    i += 1

while pi < len(p):
    arr[i] = p[pi]
    pi += 1
    i += 1

while ni < len(n):
    arr[i] = n[ni]
    ni += 1
    i += 1

print(arr)
