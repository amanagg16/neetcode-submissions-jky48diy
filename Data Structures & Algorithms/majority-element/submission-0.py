class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's voting algorithm
        majority = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                count -=1
            
            if count == 0:
                majority = nums[i]
        
        return majority

        # count = 0
        # for n in nums:
        #     if n == majority:
        #         count += 1

        # return True if count >= math.floor(len(nums)/2) else False