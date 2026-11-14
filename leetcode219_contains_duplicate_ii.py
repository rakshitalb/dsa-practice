
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l = 0
        ans = {}

        for r in range(len(nums)):
            if nums[r] in ans:
                if abs(ans[nums[r]] - r) <= k:
                    return True

            ans[nums[r]] = r

        return False
