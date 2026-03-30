class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, index, curSub):

            if index >= len(nums):
                res.append(curSub.copy())
                return
            
            curSub.append(nums[index])
            backtrack(nums, index+1, curSub)
            curSub.pop()

            # basically we dont want to include any occurence of nums[i]...skipping all of those nums[i]
            while index+1<len(nums) and nums[index] == nums[index+1]:
                index+=1
            
            backtrack(nums, index+1, curSub)

        nums.sort()
        backtrack(nums, 0, [])   
        return res     