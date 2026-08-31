n = list(map(str, input("enter : ")))

ans = ""

for i in range(len(n)):

    # Odd length palindrome
    l = i
    r = i

    while l >= 0 and r < len(n) and n[l] == n[r]:
        current = ''.join(n[l:r+1])

        if len(current) > len(ans):
            ans = current

        l -= 1
        r += 1

    # Even length palindrome
    l = i
    r = i + 1

    while l >= 0 and r < len(n) and n[l] == n[r]:
        current = ''.join(n[l:r+1])

        if len(current) > len(ans):
            ans = current

        l -= 1
        r += 1

print(ans)
