# Problem: Longest Palindromic Substring
# Day: 24
# Time Complexity: O(n^2)

def longsubpalidromarray(s):

    m = ""

    for i in range(len(s)):

        # odd palindrome
        l = i
        r = i

        while l >= 0 and r < len(s) and s[l] == s[r]:

            if len(s[l:r+1]) > len(m):

                m = s[l:r+1]

            l -= 1
            r += 1

        # even palindrome
        l = i
        r = i + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:

            if len(s[l:r+1]) > len(m):

                m = s[l:r+1]

            l -= 1
            r += 1

    return m


s = input("enter string: ")

print(longsubpalidromarray(s))
