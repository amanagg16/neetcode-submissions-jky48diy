class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        def dfs(n, m):
            if n == 0 or m == 0:
                return 0
            
            if s1[n-1] == s2[m-1]:
                return 1 + dfs(n-1, m-1)
            else:
                return max(dfs(n-1, m), dfs(n, m-1))
        
        return dfs(len(s1), len(s2))