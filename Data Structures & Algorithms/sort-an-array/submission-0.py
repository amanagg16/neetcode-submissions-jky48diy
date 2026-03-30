class Solution:
    def mergeTwoSortedArrays(self, nums, start, mid, end):
        temp = []
        l, r = start, mid+1
        while l<=mid and r<=end:
            if nums[l] < nums[r]:
                temp.append(nums[l])
                l += 1
            else:
                temp.append(nums[r])
                r += 1
            
        while l<=mid:
            temp.append(nums[l])
            l += 1

        while r<=end:
            temp.append(nums[r])
            r += 1
        
        l = start
        for n in temp:
            nums[l] = n
            l += 1


    def mergeSort(self, nums, start, end):
        if start >= end:
            return
        
        mid = math.floor((start+end)/2)
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid+1, end)
        self.mergeTwoSortedArrays(nums, start, mid, end)


    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.mergeSort(nums, 0, n-1)
        return nums