class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        for r in range(k, len(s)):
            if s[r] in vowels:
                count += 1

            if s[r - k] in vowels:
                count -= 1

            ans = max(ans, count)

        return ans
