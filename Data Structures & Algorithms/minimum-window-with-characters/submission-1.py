from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t
        l, r = 0, 0
        ct = Counter(t)
        window = {}
        
        res, res_len = [-1,-1], math.inf
        res_found = False
        have, need = 0, len(ct)
        while r < len(s):
            window[s[r]] = window.get(s[r], 0)+1
            if s[r] in ct and window[s[r]] == ct[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1<res_len:
                    res_found = True
                    res_len = r-l+1
                    res = [l,r]
                
                window[s[l]] -= 1
                if window[s[l]] < ct[s[l]]:
                    have -= 1
                l+=1
                
            r+=1
        
        return s[res[0]:res[1]+1] if res_found else ""