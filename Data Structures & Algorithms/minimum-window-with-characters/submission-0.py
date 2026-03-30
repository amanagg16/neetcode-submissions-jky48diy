from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return t
        
        ct = Counter(t)
        window = {}
        l,r = 0,0
        res, res_len = [-1,-1], math.inf
        res_found = False
        have, need = 0, len(ct)
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in ct and ct[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if (r-l+1)<res_len:
                    res_found = True
                    res_len = r-l+1
                    res = [l,r]
                window[s[l]] = window[s[l]]-1

                if s[l] in ct and ct[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
            r+=1
                
        l, r = res
        return s[l:r+1] if res_found else ""