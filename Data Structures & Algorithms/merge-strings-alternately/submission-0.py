class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l, r = 0,0
        first_word = True
        while l<len(word1) and r<len(word2):
            if first_word:
                res += word1[l]
                l += 1
                first_word = False
            else:
                res += word2[r]
                r += 1
                first_word = True
        
        while l<len(word1):
            res += word1[l]
            l += 1
        while r<len(word2):
            res += word2[r]
            r += 1
        
        return res