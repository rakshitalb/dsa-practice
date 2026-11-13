
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_size = n - k

        if window_size == 0:
            return total

        current_sum = sum(cardPoints[:window_size])
        min_sum = current_sum

        for r in range(window_size, n):
            current_sum += cardPoints[r]
            current_sum -= cardPoints[r - window_size]
            min_sum = min(min_sum, current_sum)

        return total - min_sum
