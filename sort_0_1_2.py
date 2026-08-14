n = list(map(int,input("enter :").split()))
zero = []
one = []
two = []

for i in range(len(n)):
    if n[i] == 0:
        zero.append(n[i])
    elif n[i] == 1:
        one.append(n[i])
    else:
        two.append(n[i])

print(zero + one + two)
