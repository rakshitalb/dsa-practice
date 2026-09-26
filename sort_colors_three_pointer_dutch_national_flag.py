class Solution(object):

    def sortColors(self, nums):

        r = []
        w = []
        b = []

        for i in range(len(nums)):

            if nums[i] == 0:
                r.append(nums[i])

            elif nums[i] == 1:
                w.append(nums[i])

            else:
                b.append(nums[i])

        nums[:] = r + w + b
