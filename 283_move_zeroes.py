# LeetCode 283: Move Zeroes
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1

        while l < len(nums):
            nums[l] = 0
            l += 1
