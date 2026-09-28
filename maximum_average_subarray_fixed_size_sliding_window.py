class Solution(object):

    def findMaxAverage(self, nums, k):

        w = sum(nums[:k])
        m = w

        for r in range(k, len(nums)):

            w = w - nums[r-k] + nums[r]

            if w > m:
                m = w

        return m / k
