```python
# LeetCode 125: Valid Palindrome
# Pattern: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(ch.lower() for ch in s if ch.isalnum())

        l = 0
        r = len(s) - 1
        flag = True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                flag = False
                break

        return flag
```
