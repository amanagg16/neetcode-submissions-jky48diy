class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_cons_seq_len = 0

        for n in nums:
            if n-1 not in seen:
                sub_len = 0
                while n+sub_len in seen:
                    sub_len += 1
                
                max_cons_seq_len = max(max_cons_seq_len, sub_len)
            
        return max_cons_seq_len