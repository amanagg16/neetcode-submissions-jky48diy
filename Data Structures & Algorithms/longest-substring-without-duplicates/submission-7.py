class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        n = len(s)
        l = r = 0
        m = {}

        res = 1

        while r < n:
            if s[r] in m:
                old_l = l
                l = 1 + m[s[r]]
                till = m[s[r]]
                for i in range(old_l, till+1):
                    del m[s[i]]
                
                m[s[r]] = r
                
            else:
                m[s[r]] = r
                res = max(res, r-l+1)
            
            r+=1
            
        return res