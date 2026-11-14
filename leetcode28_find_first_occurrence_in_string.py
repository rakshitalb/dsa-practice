
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        l = 0
        k = len(needle)

        for r in range(len(haystack)):
            while r - l + 1 > k:
                l += 1

            if r - l + 1 == k:
                if haystack[l:r+1] == needle:
                    return l

        return -1
