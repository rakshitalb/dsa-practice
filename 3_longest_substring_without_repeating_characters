```python
# LeetCode 3: Longest Substring Without Repeating Characters
# Pattern: Variable-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(min(n, character set size))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = {}
        m = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while count[s[r]] > 1:
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]

                l += 1

            m = max(m, r - l + 1)

        return m
```
