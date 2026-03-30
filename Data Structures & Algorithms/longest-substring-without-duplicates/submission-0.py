class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            seen = set()
            cur_len = 0
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    cur_len += 1
                    res = max(res, cur_len)
                else: break

        return res