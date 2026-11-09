
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        l = 0
        cs = 0
        count = {}
        m = 0

        for r in range(len(nums)):
            cs += nums[r]
            count[nums[r]] = count.get(nums[r], 0) + 1

            while r - l + 1 > k:
                cs -= nums[l]
                count[nums[l]] -= 1

                if count[nums[l]] == 0:
                    del count[nums[l]]

                l += 1

            if r - l + 1 == k and len(count) == k:
                m = max(m, cs)

        return m
      
