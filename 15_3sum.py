```python
# LeetCode 15: 3Sum
# Pattern: Sorting + Two Pointers
# Time Complexity: O(n^2)
# Space Complexity: O(1) auxiliary space, excluding sorting and output

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                cs = nums[i] + nums[l] + nums[r]

                if cs == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif cs < 0:
                    l += 1

                else:
                    r -= 1

        return ans
```
