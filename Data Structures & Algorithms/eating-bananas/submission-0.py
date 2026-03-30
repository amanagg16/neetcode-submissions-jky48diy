class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        def calculate_time(_k):
            s = 0
            for p in piles:
                s += math.ceil(p/_k)
            return s
        
        while l<=r:
            mid = (l+r)//2
            temp = calculate_time(mid)

            if temp<=h:
                k = mid
                r = mid-1
            else:
                l = mid+1
            
        return k