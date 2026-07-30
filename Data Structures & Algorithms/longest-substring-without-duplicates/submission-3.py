class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, 0
        res = 0
        m = {}
        while r < n:
            if s[r] in m:
                
                if m[s[r]] >=l:
                    l = m[s[r]] + 1
                    
                
            m[s[r]] = r
            res = max(res, r-l+1)
            r += 1
            
            
        return res