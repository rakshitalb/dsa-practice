class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        l = 0
        cs = sum(arr[:k])
        c = 0

        if cs >= k * threshold:
            c += 1

        for r in range(k, len(arr)):
            cs += arr[r]

            while r - l + 1 > k:
                cs -= arr[l]
                l += 1

            if cs >= k * threshold:
                c += 1

        return c
