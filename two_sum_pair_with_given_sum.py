# Check if two elements have the given sum

n = list(map(int, input("enter : ").split()))
t = int(input("enter t : "))

n.sort()

l = 0
r = len(n) - 1
flag = False

while l < r:
    if n[l] + n[r] == t:
        flag = True
        break
    elif n[l] + n[r] < t:
        l += 1
    else:
        r -= 1

print(flag)
