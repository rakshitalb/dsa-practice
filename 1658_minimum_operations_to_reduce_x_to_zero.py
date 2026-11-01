class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        l = 0
        cs = 0
        m = -1

        for r in range(len(nums)):
            cs += nums[r]

            while cs > target and l <= r:
                cs -= nums[l]
                l += 1

            if cs == target:
                m = max(m, r - l + 1)

        if m == -1:
            return -1

        return len(nums) - m
