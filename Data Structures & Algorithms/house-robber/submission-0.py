class Solution:
    def rob(self, nums: List[int]) -> int:
        s1, s2 = 0, 0
        odd = True

        for num in nums:
            if odd:
                s1 += num
            else:
                s2 += num
            
            odd = not odd
            
        return max(s1, s2)
