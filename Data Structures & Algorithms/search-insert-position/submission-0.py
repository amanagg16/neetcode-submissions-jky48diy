class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l ,r, = 0, n-1
        while l<=r:
            if l == r:
                return l if nums[l] == target else l+1
            mid = math.floor((l+r)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1