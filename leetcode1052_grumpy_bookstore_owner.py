
class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        l = 0
        c = 0

        for r in range(len(grumpy)):
            if grumpy[r] == 0:
                c += customers[r]

        m = 0
        s = []
        ss = 0

        for r in range(len(grumpy)):
            s.append(r)
            ss += customers[r]

            while len(s) > minutes:
                s.pop(0)
                ss -= customers[l]
                l += 1

            if len(s) == minutes:
                temp = ss

                for i in s:
                    if grumpy[i] == 0:
                        temp -= customers[i]

                m = max(m, temp)

        return c + m
