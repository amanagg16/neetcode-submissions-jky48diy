class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for index, value in enumerate(nums):
            lookup_value = target-value
            if lookup_value in seen:
                return [seen[lookup_value], index]
            seen[value] = index