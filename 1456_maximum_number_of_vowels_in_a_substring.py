
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        l = 0
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        m = count

        for r in range(k, len(s)):
            if s[r] in vowels:
                count += 1

            if s[l] in vowels:
                count -= 1

            l += 1
            m = max(m, count)

        return m
      
