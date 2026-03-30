from typing import List

class Solution:
    def searchMatrix(self, matrix:List[List[int]], target:int)->bool:
        ROW, COL = len(matrix), len(matrix[0])
        l, r = 0, ROW*COL-1

        while l<=r:
            mid = (l+r)//2
            row = mid//COL
            col = mid%COL

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid-1
            else:
                l = mid+1
            
        return False