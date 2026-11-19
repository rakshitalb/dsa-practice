
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()

        l = 0
        m = 0

        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1

            m = max(m, r - l + 1)

        return m
