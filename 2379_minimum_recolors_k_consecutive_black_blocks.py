class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        count = {}
        m = float('inf')

        for r in range(len(blocks)):
            count[blocks[r]] = count.get(blocks[r], 0) + 1

            while r - l + 1 > k:
                count[blocks[l]] -= 1

                if count[blocks[l]] == 0:
                    del count[blocks[l]]

                l += 1

            if r - l + 1 == k:
                o = k - count.get('B', 0)
                m = min(o, m)

        return m
