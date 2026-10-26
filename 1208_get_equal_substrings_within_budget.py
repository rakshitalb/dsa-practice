```python
# LeetCode 1208: Get Equal Substrings Within Budget
# Pattern: Variable-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        cost = 0
        ans = 0

        for r in range(len(s)):
            cost += abs(ord(s[r]) - ord(t[r]))

            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            ans = max(ans, r - l + 1)

        return ans
```
