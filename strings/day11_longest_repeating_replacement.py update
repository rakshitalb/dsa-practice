# Problem: Longest Repeating Character Replacement
# Day: 11
# Approach: Sliding Window
# Time Complexity: O(n)

def replace(s, k):

    d = {}

    l = 0
    m = 0
    maxf = 0

    for r in range(len(s)):

        # frequency count
        if s[r] in d:
            d[s[r]] += 1
        else:
            d[s[r]] = 1

        # maximum frequency
        maxf = max(maxf, d[s[r]])

        # invalid window
        while (r - l + 1) - maxf > k:
            d[s[l]] -= 1
            l += 1

        # maximum length
        m = max(m, r - l + 1)

    return m


s = input("enter string: ")

k = int(input("enter k: "))

print(replace(s, k))
