class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_count = 0
        count = 0
        prefix_count = {0: 1}

        for num in nums:
            if num % 2 == 1:
                odd_count += 1

            needed = odd_count - k
            count += prefix_count.get(needed, 0)

            prefix_count[odd_count] = (
                prefix_count.get(odd_count, 0) + 1
            )

        return count
