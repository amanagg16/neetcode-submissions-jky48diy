class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first_str = strs[0]
        n = len(first_str)
        for i in range(n):
            test_char = first_str[i]
            for s in strs:
                if i >= len(s) or s[i] != test_char:
                    return res
            res = res + test_char

            i += 1
        return res