s = list(map(str,input("enter ").split()))
l = 0
r = len(s) - 1

while l <= r:
    temp = s[l]
    s[l] = s[r]
    s[r] = temp
    l += 1
    r -= 1

print(s)
