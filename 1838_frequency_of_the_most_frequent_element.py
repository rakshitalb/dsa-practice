
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()

        l = 0
        m = 0
        o = 0

        for r in range(len(nums)):
            o += nums[r]

            while nums[r] * (r - l + 1) - o > k:
                o -= nums[l]
                l += 1

            m = max(m, r - l + 1)

        return m
