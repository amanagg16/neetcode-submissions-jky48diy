class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(0, n-2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            l, r = i+1, n-1

            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1
                    while l<r and nums[l-1] == nums[l]:
                        l += 1
                    while l<r and nums[r+1] == nums[r]:
                        r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1
                
        return res