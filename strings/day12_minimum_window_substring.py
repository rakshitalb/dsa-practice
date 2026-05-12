# Problem: Minimum Window Substring
# Day: 12
# Approach: Sliding Window
# Time Complexity: O(n)

def window(s, t):

    if t == "":
        return ""

    countT = {}
    window = {}

    # frequency of t
    for ch in t:
        countT[ch] = countT.get(ch, 0) + 1

    have = 0
    need = len(countT)

    res = [-1, -1]
    reslen = float("inf")

    l = 0

    for r in range(len(s)):

        c = s[r]
        window[c] = window.get(c, 0) + 1

        # valid character
        if c in countT and window[c] == countT[c]:
            have += 1

        # valid window
        while have == need:

            # update result
            if (r - l + 1) < reslen:
                res = [l, r]
                reslen = r - l + 1

            # shrink window
            window[s[l]] -= 1

            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1

            l += 1

    l, r = res

    return s[l:r+1] if reslen != float("inf") else ""


s = input("enter string s: ")

t = input("enter string t: ")

print(window(s, t))
