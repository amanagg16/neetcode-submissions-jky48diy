class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        l, r = 0, x//2

        while l<=r:
            mid = (l+r)//2
            prod = mid*mid
            if prod == x:
                return mid
            elif prod < x:
                l = mid+1
            else:
                r = mid-1
            
        return r