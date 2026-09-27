class Solution(object):

    def longestPalindrome(self, s):

        ans = ""

        for i in range(len(s)):

            # Odd length palindrome
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:

                cu = s[l:r + 1]

                if len(cu) > len(ans):
                    ans = cu

                l -= 1
                r += 1

            # Even length palindrome
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:

                cu = s[l:r + 1]

                if len(cu) > len(ans):
                    ans = cu

                l -= 1
                r += 1

        return ans
