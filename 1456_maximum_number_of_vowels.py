class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        m = 0
        c = 0
        ans = ['a', 'e', 'i', 'o', 'u']

        for r in range(len(s)):
            if s[r] in ans:
                c += 1

            if r - l + 1 > k:
                if s[l] in ans:
                    c -= 1
                l += 1

            if r - l + 1 == k:
                m = max(c, m)

        return m
