```python
# LeetCode 643: Maximum Average Subarray I
# Pattern: Fixed-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        ca = sum(nums[:k])
        a = ca / k
        ma = a

        for r in range(k, len(nums)):
            ca -= nums[l]
            ca += nums[r]
            l += 1
            a = ca / k
            ma = max(a, ma)

        return ma
```
