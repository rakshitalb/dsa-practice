n = list(map(int, input("enter :").split()))
s = int(input("enter :"))

i = 0
j = s

flag = False

while j < len(n):

    if n[i] == n[j]:
        flag = True
        break

    i += 1
    j += 1

print(flag)
