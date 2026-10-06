class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        ans = 0
        m = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            # Maximum frequency in the current window
            m = max(m, count[s[r]])

            # Number of characters that need replacement
            while (r - l + 1) - m > k:
                count[s[l]] -= 1
                l += 1

            # Current valid window length
            ans = max(ans, r - l + 1)

        return ans
