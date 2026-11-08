
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        cs = 0
        m = float('inf')

        for r in range(len(nums)):
            cs += nums[r]

            while cs >= target:
                m = min(m, r - l + 1)
                cs -= nums[l]
                l += 1

        if m == float('inf'):
            return 0

        return m
      
