
from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_d = deque()
        max_d = deque()
        l = 0
        m = 0

        for r in range(len(nums)):
            while min_d and nums[r] < min_d[-1]:
                min_d.pop()
            min_d.append(nums[r])

            while max_d and nums[r] > max_d[-1]:
                max_d.pop()
            max_d.append(nums[r])

            while max_d[0] - min_d[0] > limit:
                if nums[l] == min_d[0]:
                    min_d.popleft()

                if nums[l] == max_d[0]:
                    max_d.popleft()

                l += 1

            m = max(m, r - l + 1)

        return m
