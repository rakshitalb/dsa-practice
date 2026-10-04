class Solution(object):
    def maximumSubarraySum(self, nums, k):
        count = {}
        window_sum = 0
        ans = 0

        for i in range(k):
            window_sum += nums[i]
            count[nums[i]] = count.get(nums[i], 0) + 1

        if len(count) == k:
            ans = window_sum

        for r in range(k, len(nums)):
            window_sum += nums[r]
            count[nums[r]] = count.get(nums[r], 0) + 1

            left = nums[r - k]
            window_sum -= left
            count[left] -= 1

            if count[left] == 0:
                del count[left]

            if len(count) == k:
                ans = max(ans, window_sum)

        return ans
