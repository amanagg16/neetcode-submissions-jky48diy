class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
       
        n = len(s)

        if n == 0:
            return ""

        res = ""

        def expand(l, r):

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            # loop breaks AFTER crossing palindrome boundary
            return s[l + 1:r]

        for i in range(n):

            # odd length palindrome
            odd = expand(i, i)

            # even length palindrome
            even = expand(i, i + 1)

            if len(odd) > len(res):
                res = odd

            if len(even) > len(res):
                res = even

        return res
