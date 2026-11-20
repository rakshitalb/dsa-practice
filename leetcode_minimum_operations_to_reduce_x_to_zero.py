
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target = total - x

        l = 0
        m = -1
        s = 0

        for r in range(len(nums)):
            s += nums[r]

            while s > target and l <= r:
                s -= nums[l]
                l += 1

            if s == target:
                m = max(m, r - l + 1)

        if m == -1:
            return -1

        return len(nums) - m
