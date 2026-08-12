n = input("enter :")
l = 0
r = len(n) - 1
ans = ""

while l < len(n):
    window = n[l:r+1]

    if window == window[::-1]:
        if ans == "" or len(window) > len(ans):
            ans = window
        l += 1
        r = len(n) - 1
    else:
        r -= 1

print(ans)
