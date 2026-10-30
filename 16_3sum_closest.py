
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                cs = nums[i] + nums[l] + nums[r]

                if abs(target - cs) < abs(target - ans):
                    ans = cs

                if cs < target:
                    l += 1
                elif cs > target:
                    r -= 1
                else:
                    return cs

        return ans
