class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = ['']*2*n
        for index, val in enumerate(nums):
            res[index] = val
            res[n + index] = val
        
        return res