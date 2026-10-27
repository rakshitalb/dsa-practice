```python
# LeetCode 904: Fruit Into Baskets
# Pattern: Variable-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = {}
        l = 0
        m = 0

        for r in range(len(fruits)):
            count[fruits[r]] = count.get(fruits[r], 0) + 1

            while len(count) > 2:
                count[fruits[l]] -= 1

                if count[fruits[l]] == 0:
                    del count[fruits[l]]

                l += 1

            m = max(m, r - l + 1)

        return m
```
