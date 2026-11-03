class Solution:
    def reverseVowels(self, s: str) -> str:
        ans = "aeiouAEIOU"
        l = 0
        r = len(s) - 1
        k = list(s)

        while l < r:
            if k[l] in ans and k[r] in ans:
                k[l], k[r] = k[r], k[l]
                l += 1
                r -= 1
            elif k[l] not in ans:
                l += 1
            elif k[r] not in ans:
                r -= 1

        return "".join(k)
