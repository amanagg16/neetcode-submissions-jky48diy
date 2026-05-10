class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        def dfs(n, m):
            if n == 0 or m == 0:
                return 0
            
            if s1[n-1] == s2[m-1]:
                return 1 + dfs(n-1, m-1)
            else:
                return max(dfs(n-1, m), dfs(n, m-1))

        def dfs1(n, m):
            if n == 0 or m == 0:
                return 0
            
            if (n,m) in memo:
                return memo[(n,m)]
            
            if s1[n-1] == s2[m-1]:
                memo[(n,m)] = 1 + dfs1(n-1, m-1)
            else:
                memo[(n,m)] = max(dfs1(n-1, m), dfs1(n, m-1))
            
            return memo[(n,m)]
        
        memo = {}
        return dfs1(len(s1), len(s2))