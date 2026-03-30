class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        # left product
        for i in range(1, len(output)):
            output[i] = nums[i-1]*output[i-1]

        #right product
        right = nums[-1]
        for i in range(len(output)-2, -1, -1):
            output[i] = output[i]*right
            right = right*nums[i]

        return output