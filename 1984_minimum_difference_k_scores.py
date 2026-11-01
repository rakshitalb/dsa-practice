class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()

        l = 0
        m = float('inf')

        for r in range(k - 1, len(nums)):
            d = nums[r] - nums[l]
            m = min(d, m)
            l += 1

        return m
