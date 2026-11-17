
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        w = 0
        m = float('inf')

        for r in range(len(blocks)):
            if blocks[r] == "W":
                w += 1

            while r - l + 1 > k:
                if blocks[l] == "W":
                    w -= 1
                l += 1

            if r - l + 1 == k:
                m = min(m, w)

        return m
