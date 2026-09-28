class Solution(object):

    def lengthOfLongestSubstring(self, s):

        l = 0
        ans = []
        cl = 0
        m = 0

        for r in range(len(s)):

            while s[r] in ans:
                ans.remove(s[l])
                l += 1
                cl -= 1

            ans.append(s[r])
            cl += 1

            m = max(m, cl)

        return m
