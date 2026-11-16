
class Solution:
    def compress(self, chars: list[str]) -> int:
        l = 0
        r = 0

        while r < len(chars):
            ch = chars[r]
            count = 0

            while r < len(chars) and chars[r] == ch:
                count += 1
                r += 1

            chars[l] = ch
            l += 1

            if count > 1:
                for digit in str(count):
                    chars[l] = digit
                    l += 1

        return l
