class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n-1
        left_max, right_max = height[l], height[r]
        res = 0
        while l<r:
            if left_max < right_max:
                res += left_max-height[l]
                l += 1
                left_max = max(left_max, height[l])
            else:
                res += right_max-height[r]
                r -= 1
                right_max = max(right_max, height[r])
            
        return res