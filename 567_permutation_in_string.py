
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}

        for ch in s1:
            need[ch] = need.get(ch, 0) + 1

        l = 0
        window = {}

        for r in range(len(s2)):
            ch = s2[r]
            window[ch] = window.get(ch, 0) + 1

            if r - l + 1 > len(s1):
                lch = s2[l]
                window[lch] -= 1

                if window[lch] == 0:
                    del window[lch]

                l += 1

            if window == need:
                return True

        return False
