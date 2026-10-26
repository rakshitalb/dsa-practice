```python
# LeetCode 1004: Max Consecutive Ones III
# Pattern: Variable-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = 0
        zeros = 0
        m = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            m = max(m, r - l + 1)

        return m
```
