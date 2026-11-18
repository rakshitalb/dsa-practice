
class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        s = 0
        ans = 0

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                s += 1
                l += 1
                ans = max(ans, s)

            elif s > 0:
                power += tokens[r]
                s -= 1
                r -= 1

            else:
                break

        return ans
