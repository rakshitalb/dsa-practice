n = list(map(int,input("enter :").split()))

s = int(input("enter :"))

i = 0
j = s
m = 0

while j < len(n):

    diff = abs(n[i] - n[j])

    if diff > m:
        m = diff

    i += 1
    j += 1

print(m)
