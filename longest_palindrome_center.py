n = input("enter :")

ans = ""
max_len = 0

for i in range(len(n)):

    # Odd length
    l = i
    r = i

    while l >= 0 and r < len(n) and n[l] == n[r]:

        length = r - l + 1

        if length > max_len:
            ans = n[l:r+1]
            max_len = length

        l -= 1
        r += 1

    # Even length
    l = i
    r = i + 1

    while l >= 0 and r < len(n) and n[l] == n[r]:

        length = r - l + 1

        if length > max_len:
            ans = n[l:r+1]
            max_len = length

        l -= 1
        r += 1

print(ans)
