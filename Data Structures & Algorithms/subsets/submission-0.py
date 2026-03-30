class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, i, curSubset):
            if i >= len(nums):
                res.append(curSubset.copy())
                return
            
            curSubset.append(nums[i])
            backtrack(nums, i+1, curSubset)

            curSubset.pop()
            backtrack(nums, i+1, curSubset)
        
        backtrack(nums, 0, [])
        return res