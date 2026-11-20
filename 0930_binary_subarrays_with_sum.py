
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(k):
            if k < 0:
                return 0

            l = 0
            cs = 0
            c = 0

            for r in range(len(nums)):
                cs += nums[r]

                while cs > k:
                    cs -= nums[l]
                    l += 1

                c += r - l + 1

            return c

        return atMost(goal) - atMost(goal - 1)
