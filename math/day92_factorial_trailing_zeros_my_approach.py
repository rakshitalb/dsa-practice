n = int(input("Enter: "))

p = 1
while n != 0:
    p *= n
    n -= 1

print(p)

s = list(str(p))
c = 0

for num in s[::-1]:
    if num == '0':
        c += 1
    else:
        break

print(c)
