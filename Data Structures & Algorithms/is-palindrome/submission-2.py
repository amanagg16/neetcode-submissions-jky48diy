class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = set()
        for i in range(10):
            valid_chars.add(i)
            valid_chars.add(str(i))
        for i in range(97, 97+26):
            valid_chars.add(chr(i))
            valid_chars.add(chr(i).upper())

        s = s.lower()
        l, r = 0, len(s)-1
        while l < r:
            if s[l] not in valid_chars:
                l += 1
                continue
            if s[r] not in valid_chars:
                r -=1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

