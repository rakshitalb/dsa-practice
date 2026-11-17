
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        ans = 0

        for r in range(len(nums) - 1, 1, -1):
            l = 0
            rr = r - 1

            while l < rr:
                if nums[l] + nums[rr] > nums[r]:
                    ans += rr - l
                    rr -= 1
                else:
                    l += 1

        return ans
