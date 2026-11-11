
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        need = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1

        l = 0
        window = {}
        ans = []

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if r - l + 1 > len(p):
                left_char = s[l]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                l += 1

            if window == need:
                ans.append(l)

        return ans
      
