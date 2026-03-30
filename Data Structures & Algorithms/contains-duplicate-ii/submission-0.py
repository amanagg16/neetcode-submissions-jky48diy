from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occurrences = {}

        for index, val in enumerate(nums):
            if val in occurrences:
                occurrences[val].append(index)
            else:
                occurrences[val] = [index]

        
        for _,val in occurrences.items():
            if len(val) > 1:
                for i in range(0, len(val)-1):
                    if val[i+1]-val[i] <= k:
                        return True
            
        return False
    