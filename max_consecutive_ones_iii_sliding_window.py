class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        zeros = 0
        mn = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            mn = max(mn, r - l + 1)

        return mn
