class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dfs(i):
            if i > n:
                return 0
            
            if i == n:
                return 1

            ways = 0
            if s[i] != "0":
                ways += dfs(i+1)
            
            if s[i] != "0" and i+1 < n and ((s[i] == "1" and s[i+1] in ["0", "1", "2", "3", "4","5", "6", "7", "8", "9"]) or (s[i] == "2" and s[i+1] in ["0", "1", "2", "3", "4","5", "6"])):
                ways += dfs(i+2)
        
            return ways
        
        return dfs(0)