```python
# LeetCode 15: 3Sum - Brute Force
# Pattern: Three Nested Loops
# Time Complexity: O(n^3) (excluding duplicate checking)
# Space Complexity: O(k) for storing results

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    cs = nums[i] + nums[j] + nums[k]

                    if cs == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])

                        if triplet not in ans:
                            ans.append(triplet)

        return ans
```
