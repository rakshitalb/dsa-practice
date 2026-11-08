
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        m = float('inf')
        cs = 0

        for r in range(len(nums)):
            cs += nums[r]

            while cs >= target:
                m = min(r - l + 1, m)
                cs -= nums[l]
                l += 1

        if m == float('inf'):
            return 0

        return m
