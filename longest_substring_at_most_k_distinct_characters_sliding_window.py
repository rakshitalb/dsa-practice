class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        l = 0
        count = {}
        ans = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while len(count) > k:
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]

                l += 1

            ans = max(ans, r - l + 1)

        return ans
