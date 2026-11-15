
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        count = {}
        m = 0

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

        for x in count:
            if x + 1 in count:
                m = max(m, count[x] + count[x + 1])

        return m
