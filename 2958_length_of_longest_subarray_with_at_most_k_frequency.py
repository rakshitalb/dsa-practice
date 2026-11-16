
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        count = {}
        m = 0

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1

            m = max(m, r - l + 1)

        return m
