class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
       
        largest = 0
        res = ""
        for i in range(n):
            # odd
            l, r = i-1, i+1
            odd_count = 1
            odd_palindrome_candidate = ""
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
                odd_count += 2
                odd_palindrome_candidate = s[l+1:r]
            
            # even
            l, r = i-1, i
            even_count = 0
            even_palindrome_candidate = ""
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
                even_count += 2
                even_palindrome_candidate = s[l+1:r]

            if odd_count > largest:
                largest = odd_count
                res = odd_palindrome_candidate
            if even_count > largest:
                largest = even_count
                res = even_palindrome_candidate

        return res
