class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def count_palindromic_substrings(l ,r):
            count = 0
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count


        count = 0
        for i in range(0, n):
            
            count += count_palindromic_substrings(i, i)
            count += count_palindromic_substrings(i-1, i)
        
        return count