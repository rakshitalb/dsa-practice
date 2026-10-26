```python
# LeetCode 1493: Longest Subarray of 1's After Deleting One Element
# Pattern: Variable-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l = 0
        zeros = 0
        m = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            m = max(m, r - l)

        return m
```
