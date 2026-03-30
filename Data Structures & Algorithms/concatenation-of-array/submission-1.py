class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for _ in range(2):
            for j in nums:
                res.append(j)
            
        return res