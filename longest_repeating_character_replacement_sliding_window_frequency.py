class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        count = {}
        max_freq = 0
        ans = 0

        for r in range(len(s)):
            # Count the current character
            count[s[r]] = count.get(s[r], 0) + 1

            # Find the highest frequency
            max_freq = max(max_freq, count[s[r]])

            # Number of characters that need to be replaced
            changes = (r - l + 1) - max_freq

            # If changes are more than k, shrink the window
            while changes > k:
                count[s[l]] -= 1
                l += 1
                changes = (r - l + 1) - max_freq

            # Store the longest valid window
            ans = max(ans, r - l + 1)

        return ans
