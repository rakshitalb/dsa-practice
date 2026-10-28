```python
# LeetCode 1052: Grumpy Bookstore Owner
# Pattern: Fixed-Size Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        c = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                c += customers[i]

        l = 0
        s = 0
        m = 0

        for r in range(len(customers)):
            if grumpy[r] != 0:
                s += customers[r]

            while r - l + 1 > minutes:
                if grumpy[l] != 0:
                    s -= customers[l]
                l += 1

            m = max(s, m)

        return m + c
```
