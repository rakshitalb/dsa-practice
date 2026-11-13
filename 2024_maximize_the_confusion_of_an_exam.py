
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {}
        l = 0
        m = 0

        for r in range(len(answerKey)):
            count[answerKey[r]] = count.get(answerKey[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[answerKey[l]] -= 1

                if count[answerKey[l]] == 0:
                    del count[answerKey[l]]

                l += 1

            m = max(m, r - l + 1)

        return m
