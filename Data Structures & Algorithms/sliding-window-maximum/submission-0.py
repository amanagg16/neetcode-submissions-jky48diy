from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        dq = deque()

        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        
        l, r = 1, k

        while r < n:
            while dq and dq[0] < l:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            
            dq.append(r)
            res.append(nums[dq[0]])

            r += 1
            l += 1
        
        return res
        
        
        
