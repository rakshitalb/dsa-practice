class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l = 0
        count = {}
        d = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            if r - l + 1 > 3:
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]

                l += 1

            if len(count) == 3:
                d += 1

        return d
