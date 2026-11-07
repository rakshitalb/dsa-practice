
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        cs = sum(nums[:k])
        m = cs

        for r in range(k, len(nums)):
            cs += nums[r]

            while r - l + 1 > k:
                cs -= nums[l]
                l += 1

            m = max(cs, m)

        return m / k
      
