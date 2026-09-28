class Solution(object):

    def numOfSubarrays(self, arr, k, threshold):

        w = sum(arr[:k])

        if w / k >= threshold:
            c = 1
        else:
            c = 0

        for r in range(k, len(arr)):

            w = w - arr[r-k] + arr[r]

            if w / k >= threshold:
                c += 1

        return c
