```python
# LeetCode 977: Squares of a Sorted Array
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        l = 0
        r = len(nums) - 1
        ans = [0] * len(nums)
        p = len(nums) - 1

        while l <= r:
            if nums[l] > nums[r]:
                ans[p] = nums[l]
                l += 1
            else:
                ans[p] = nums[r]
                r -= 1
            p -= 1

        return ans
```
