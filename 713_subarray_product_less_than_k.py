
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        l = 0
        cs = 1
        c = 0

        for r in range(len(nums)):
            cs *= nums[r]

            while cs >= k:
                cs //= nums[l]
                l += 1

            c += r - l + 1

        return c
