n = list(map(int, input("Enter: ").split()))

zero = 0
one = 0
two = 0

for i in n:
    if i == 0:
        zero += 1
    elif i == 1:
        one += 1
    else:
        two += 1

index = 0

while zero > 0:
    n[index] = 0
    index += 1
    zero -= 1

while one > 0:
    n[index] = 1
    index += 1
    one -= 1

while two > 0:
    n[index] = 2
    index += 1
    two -= 1

print(n)
