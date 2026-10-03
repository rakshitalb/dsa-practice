class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        count_p = {}
        count_s = {}

        for ch in p:
            count_p[ch] = count_p.get(ch, 0) + 1

        k = len(p)
        ans = []

        for i in range(k):
            count_s[s[i]] = count_s.get(s[i], 0) + 1

        if count_p == count_s:
            ans.append(0)

        for r in range(k, len(s)):
            count_s[s[r]] = count_s.get(s[r], 0) + 1

            left = s[r - k]
            count_s[left] -= 1

            if count_s[left] == 0:
                del count_s[left]

            if count_p == count_s:
                ans.append(r - k + 1)

        return ans
