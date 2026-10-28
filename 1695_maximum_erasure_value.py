```python
# LeetCode 1695: Maximum Erasure Value
# Pattern: Variable-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        l = 0
        m = 0
        cs = 0
        count = {}

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

            while count[nums[r]] > 1:
                cs -= nums[l]
                count[nums[l]] -= 1

                if count[nums[l]] == 0:
                    del count[nums[l]]

                l += 1

            cs += nums[r]
            m = max(cs, m)

        return m
```
