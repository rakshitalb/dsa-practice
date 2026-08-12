n = list(input("enter ").lower())

l = 0
r = len(n) - 1
flag = True

while l < r:
    if n[l] == n[r]:
        l += 1
        r -= 1
    else:
        flag = False
        break

print(flag)
