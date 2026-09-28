class Solution(object):

    def minSubArrayLen(self, target, nums):

        l = 0
        c = 0
        ml = float('inf')
        ll = 0

        for r in range(len(nums)):

            c += nums[r]
            ll += 1

            while c >= target:

                ml = min(ll, ml)

                c -= nums[l]
                ll -= 1
                l += 1

        if ml == float('inf'):
            return 0

        return ml
