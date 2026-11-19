
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        cost = 0
        m = 0

        for r in range(len(s)):
            cost += abs(ord(s[r]) - ord(t[r]))

            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            m = max(m, r - l + 1)

        return m
