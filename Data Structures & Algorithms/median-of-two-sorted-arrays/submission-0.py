import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        if len(a) > len(b):
            a, b = b, a
        
        m, n = len(a), len(b)
        total = m+n
        half = total // 2
        l, r = 0, m-1

        while True:
            ma = (l+r) // 2
            mb = half - ma - 2

            aleft = a[ma] if ma >= 0 else -math.inf
            bleft = b[mb] if mb >= 0 else -math.inf
            aright = a[ma+1] if ma + 1 < m else math.inf
            bright = b[mb+1] if mb + 1 < n else math.inf

            if aleft <= bright and bleft <= aright:
                if total % 2 == 0:
                    return (max(aleft, bleft) + min(aright, bright))/2
                return min(aright, bright)
            
            elif aleft > bright:
                r = ma - 1
            else:
                l = ma + 1
            